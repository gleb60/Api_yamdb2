# Api YAMDB

## Описание проекта
Апи разработано для проекта YAMDB. 
Оно позволяет выставлять рейтинги контенту, оставлять отзывы и комментировать их.

## Технологии
- Python 3.9
- Django 3.2
- Django REST framework 3.12.4

### Как запустить проект:
 
Клонировать репозиторий и перейти в него в командной строке:
 
```
git clone git@github.com:Gromtag/api_yamdb.git
```
 
```
cd api_yamdb
```
 
Cоздать виртуальное окружение на Linux:
 
```
python3 -m venv venv
```
 
Или на Windows:
 
```
python -m venv venv
```
 
И активировать виртуальное окружение на Linux:
```
. venv/bin/activate
```
Или на Windows:
```
source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:
 
```
python3 -m pip install --upgrade pip
```
 
```
pip install -r requirements.txt
```
Зайти в папку приложения:
```
cd api_yamdb
```
Выполнить миграции:
 
```
python3 manage.py migrate
```
 
Запустить проект:
 
```
python3 manage.py runserver
```
