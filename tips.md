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

Production shell
`heroku logs -tail -a quarantine-camp`

`heroku pg:info -a quarantine-camp`

`heroku ps:restart -a quarantine-camp`

`heroku ps:stop run.7036 -a quarantine-camp`

`heroku config -s | grep DATABASE_URL -a quarantine-camp`

`heroku pg:reset DATABASE_URL -a quarantine-camp`

`heroku run python manage.py createsuperuser -a quarantine-camp`

`heroku run python manage.py migrate -a quarantine-camp`

`heroku run python manage.py makemigrations -a quarantine-camp`