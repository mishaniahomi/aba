# aba
Нужно установить следующие пакеты<br>
sudo apt install mysql-server mysql-client<br>
sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3<br>

В MySQL выполнить команды<br>
create database django_db;<br>
create user 'django_user'@'%' IDENTIFIED BY '12345678';<br>
GRANT ALL PRIVILEGES ON django_db . * TO 'django_user'@'%';<br>

Из директории проекта в командной строке выполнить<br>
python manage.py makemigrations<br>
python manage.py migrate<br>
apt install python3.10-venv<br>
<br>
<br>python3 -m venv venv
<br>source venv/bin/activate
<br>pip install -r reque
<br>
<br>



