
'''
1. создаем вертуальное окружение 
    python3 -m venv venv 

2. устанавливаем нужные зависимости
    django 
    dgangorestframework
    psycopg2-binary

    pip install -r requirements.txt
    pip install django djanfprestframework
    psycopg2-binary
    
3. создаем проект 
    python3 manage.py startproject <name> .

4. регистрация rest_framework в INSTALED_APPS, если создали лоп приложения, то их тоже регистрируем

5. создаем приложение
    python3 manage.py startapp <name>

6. настраеваем базу данных 

7. миграция в базеданных
    7.1 -> создание миграции 
        python3 manage.py makemigration
    7.2 -> применение файлов миграции к базеданных
        python3 manage.py migrate

8. создание суперпользователя
    python3 manage.py createsuperuser

9. запуск
    python3 manage.py runserver
    python3 manage.py runserver 8001

fuser -k 8000/tcp -> убиваем 8000 порт
'''

'''
создать 5 проектов , настроить бд (пройтись по верзнему списку ) и залить на гидхаб
'''