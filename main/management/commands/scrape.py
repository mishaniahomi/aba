from typing import Any
from django.core.management.base import BaseCommand

from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
from main.models import Post
# import os, sys

# sys.path.append('C:\\Users\\Misha\Desktop\\aba\\html')
# os.environ['DJANGO_SETTINGS_MODULE'] = 'apkaba.settings'
#
# import django
# django.setup()

class Command(BaseCommand):
    help = "collect jobs"

    def handle(self, *args, **options):
        

        for page in range(26, 0, -1):
            print(page)

            html = urlopen("https://apkaba.ru/novosti/page/{}".format(page))
            soup = BeautifulSoup(html.read(), 'html.parser')
            quotes = soup.find_all('div', style="padding: 0px 0px 10px 0px; margin: 0px 0px 20px 0px; font-size: 12px; border-bottom: 1px solid #909090;")

            for i in quotes:
                title = i.find('a').text
                slug = i.find('a')['href'].split('/')[3]

                image_name = '_'.join(i.find('img')['src'].split('/')[5::])
                picture_url = '/aba/media/news_image/{}'.format(image_name)

                img_data = requests.get(i.find('img')['src']).content
                with open(picture_url, 'wb') as handler:
                    handler.write(img_data)
                picture_url = '/news_image/{}'.format(image_name)
                print(picture_url)
                post_html = urlopen(i.find('a')['href'])
                post_soup = BeautifulSoup(post_html.read(), 'html.parser')
                content = post_soup.find_all('td', width=690)
                content = content
                try:
                    new_post = Post.objects.create(title=title, content=content, image=picture_url, slug=slug[:50], picture_url=picture_url)
                    new_post.save()
                except Exception as e:
                    file = open('error.txt', 'a+')
                    print("Ошибка", slug, e, file=file)
             


