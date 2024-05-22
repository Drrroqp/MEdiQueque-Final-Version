# MEdiQueque-Final-Version
 MEdiQueque-Final-Version

Launch server in first time:
python -m venv venv
.\venv\Scripts\activate
cd mediqueue
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Launch in another time:
python -m venv venv
.\venv\Scripts\activate
cd mediqueue
python manage.py runserver
