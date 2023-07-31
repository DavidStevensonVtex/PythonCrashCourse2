# Chapter 18: Getting Started with Django

## Specification

We'll write a web app called Learning Log that allows users to log the topics they're
interested in and to make journal entries as they learn about each topic. The Learning Log
home page will describe the site and invite users to either register or login. Once
logged in, a user can create new topics, add new entries, and read and
edit existing entries.

## Creating a Virtual Environment

python -m venv .venv

source .venv/Scripts/activate

To stop using a virtual environment, enter **deactivate**.

deactivate

## Installing Django

pip install django

## Creating a Project in Django

django-admin startproject learning_log .

ls learning_log

\_\_init\_\_.py asgi.py settings.py urls.py wsgi.py

## Creating the Database

python manage.py migrate

Running the ls command shows that Django created another file called db.sqlite3.

## Viewing the Project

python manage.py runserver

## Starting an App

A Django project is organized as a group of individual apps that work toether to make
the project work as a whole.

Leave the development server running and open a new terminal window.

source .venv/Scripts/activate

python manage.py startapp learning_logs

## Defining Models

Open the file models.py.

```
from django.db import models

# Create your models here.
```

A module called models is being imported and we can create our models here.

```
from django.db import models

class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text
```

## Activating Models

Open _settings.py_ in the learning*log/learning_log directory. Modify \_settings.py* as follows:

```
INSTALLED_APPS = [
    # My apps
    'learning_logs',

    # Default Django apps.
```

Tell Django to modify the database so it can store information about the topic.

python manage.py makemigrations learning_logs

Apply the migration (learning_logs/migrations/001_initial.py) using the following command:

python manage.py migrate

## The Django Admin Site

### Setting Up a Superuser

To create a superuser in Django, enter the following command and enter the required information:

```
$ python manage.py createsuperuser
Username (leave blank to use 'drste'): ll_admin
Email address:
Password:
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
(.venv)
```

### Registering a Model with the Admin Site

Open admin.py in the learning_logs folder.
