import os, sys

sys.path.append('/home/homi/PycharmProjects/aba/server/aba')
os.environ['DJANGO_SETTINGS_MODULE'] = 'apkaba.settings'
import django
django.setup()
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests




from models import Post
for page in range(26, 0, -1):
    print(page)
    html = urlopen("https://apkaba.ru/novosti/page/{}".format(page))
    soup = BeautifulSoup(html.read(), 'html.parser')
    quotes = soup.find_all('div', style="padding: 0px 0px 10px 0px; margin: 0px 0px 20px 0px; font-size: 12px; border-bottom: 1px solid #909090;")
    for i in quotes:
        title = i.find('a').text
        slug = i.find('a')['href'].split('/')[3]

        picture_url = '_'.join(i.find('img')['src'].split('/')[5::])
        picture_url = 'media/news_image/{}'.format(picture_url)

        img_data = requests.get(i.find('img')['src']).content
        with open(picture_url, 'wb') as handler:
            handler.write(img_data)
        picture_url = '/{}'.format(picture_url)
        print(picture_url)
        post_html = urlopen(i.find('a')['href'])
        post_soup = BeautifulSoup(post_html.read(), 'html.parser')
        content = post_soup.find_all('td', width=690)
        # print("""
        # from main.models import Post
        # new_post=(title='{}', content=\"\"\"{}\"\"\", image = '{}', slug='{}', picture_url='{}')
        # """.format(title, 'content', picture_url, slug, picture_url))
        print(Post.objects.all())
        break
    break


