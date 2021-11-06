# Some helpful commands
Create project env named *env*

`python -m venv env`

Create Django project

`django-admin startproject web_project .`

Create Django App

`python manage.py startapp hello`

Create Superuser

`python manage.py createsuperuser`

Collect static files (production)

`python manage.py collectstatic`

Commit data models migration

`python manage.py makemigrations`

Apply migration
`python manage.py migrate`

Show requirements (libraries installed in the activated environment)

`pip freeze`

Save requirements to file

`pip freeze > requirements.txt`

Seed data

`python manage.py seed hospital_app --number=10`

install all packages
`pip install -r requirements.txt`