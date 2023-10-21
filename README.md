[![Gitlab Badge](https://gitlab.crja72.ru/django_2023/students/47717-stepapetruk-yandex.ru-47231/badges/main/pipeline.svg)]


# Запуск проекта в dev-режиме
	1. Установите python и pip, если они не установлены
	2. Рекомендуется создать виртуальное окружение и активировать его
```
python -m venv venv
#Linux
soutse venv/bin/activate
#Windows
venv\Scripts\activate
```
	3. Установите зависимости проекта для разработки
```
pip install -r requirements/prod.txt #Windows
pip install -r requirements\prod.txt #Linux
```
	4. Если это необходимо установите так же и зависимости, для разработки
```
pip install -r requirements/dev.txt #Windows
pip install -r requirements\dev.txt #Linux
```
	5. Если это необходимо установите так же и зависимости, для тестирования
```
pip install -r requirements/test.txt #Windows
pip install -r requirements\test.txt #Linux
```
	6. Устанавливаем .env
Переименуйте Файл 'example.env' в '.env' и заполните переменные окружения необходимой информацией
	7. Запустите сервер
```
python manage.py runserver
```
	8. В браузере перейдите по адрессу http://127.0.0.1:8000 для доступа к приложению