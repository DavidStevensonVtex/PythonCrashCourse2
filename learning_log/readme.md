# Chapter 18: Getting Started with Django

## Specification

We'll write a web app called Learning Log that allows users to log the topics they're
interested in and to make journal entries as they learn about each topic. The Learning Log
home page will describe the site and invite users to either register or login. Once
logged in, a user can create new topics, add new entries, and read and
edit existing entries.

## Creating a Virtual Environment

python -m venv .venvhi

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

### Adding Topics

![](AddingTopics.JPG)

### Defining an Entry Model

Here's the code for the Entry model. Put the code in your models.py file.

```
class Entry(models.Model):
    """Something specific learned about a topc."""
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."
```

### Migrating the Entry Model

```
$ python manage.py makemigrations learning_logs
Migrations for 'learning_logs':
  learning_logs\migrations\0002_entry.py
    - Create model Entry
```

```
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, learning_logs, sessions
Running migrations:
  Applying learning_logs.0002_entry... OK
```

### Registering Entry with the Admin Site

Modify the admin.py file as follows:

```
from django.contrib import admin
from learning_logs.models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)
```

![](AddingAnEntryForTheChessTopic.JPG)

### The Django Shell

```
$ python manage.py shell
Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from learning_logs.models import Topic
>>> Topic.objects.all()
<QuerySet [<Topic: Chess>, <Topic: Rock Climbing>]>
>>> topics = Topic.objects.all()
>>> for topic in topics:
...     print(topic.id, topic)
...
1 Chess
2 Rock Climbing
>>> t = Topic.objects.get(id=1)
>>> t.text
'Chess'
>>> t.date_added
datetime.datetime(2023, 7, 31, 15, 44, 29, 839993, tzinfo=datetime.timezone.utc)
>>> t.entry_set.all()
<QuerySet [<Entry: The opening is the first part of the game, roughly...>]>
```

## Making Pages: The Learning Log Home Page

Making web pages with Django consists of three stages:

1. defining URLs
1. Writing views
1. Writing templates

You can do these in any order, but starting with defining the ULR pattern may be best.

### Mapping a URL

The contents of the urls.py file, after the learning_logs line is added:

```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('learning_logs.urls'))
]
```

### Writing a View

The modifications to learning_logs/views.py are as follows:

```
from django.shortcuts import render

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')
```

### Writing a Template

The contents of learning_logs/templates/learning_logs/index.html

```
<p>Learning Log</p>

<p>
  Learning Log helps you keep track of your learning, for any topic you're
  learning about.
</p>
```

## Building Additional Pages

### Template Inheritance

#### The Parent Template

The contents of learning_logs/templates/learning_logs/base.html

```
<p>
    <a href=""{% url 'learning_logs:index' %}">Learning Log</a>
</p>

{% block content %}{% endblock content %}
```

#### The Child Template

```
{% extends "learning_logs/base.html" %}

{% block content %}

<p>
  Learning Log helps you keep track of your learning, for any topic you're
  learning about.
</p>

{% endblock content %}

```

### The Topics Page

#### The Topics URL Pattern

```
"""Defines URL patterns for learning logs."""

from django.urls import path
from . import views

app_name = "learning_logs"
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    # Page that shows all topics.
    path("topics/", views.topics, name="topics"),
]
```

#### The Topics View

learning_log/learning_logs/urls.py

```
from django.shortcuts import render
from learning_logs.models import Topic

...

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by("date_added")
    context = {"topics": topics}
    return render(request, "learning_logs/topics.html", context)

```

#### The Topics Template

learning_log/learning_logs/templates/learning_logs/topics.html

```
{% extends "learning_logs/base.html" %}

{% block content %}

<p>Topics</p>

<ul>
    {% for topic in topics %}
        <li>{{ topic }}</li>
    {% empty %}
        <li>No topics have been added yet.</li>
    {% endfor %}
</ul>

{% endblock content %}
```

### Invidual Topic Pages

#### The Topic URL Pattern

learning_log/learning_logs/urls.py

```
...
urlpatterns = [
...
    # Detail page for a single topic.
    path("topics/<int:topic_id>/", views.topic, name="topic"),
]
```

#### The Topic View

Add the following code to: learning_log/learning_logs/views.py

```
def topic(rquest, topid_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "learning_logs/topic.html", context)
```

#### The Topic Template

learning_log/learning_logs/templates/learning_logs/topic.html

```
{% extends 'learning_logs/base.html' %}

{% block content %}

<p>Topic: {{ topic }} </p>

<p>Entries:</p>
<ul>
    {% for entry in entries %}
        <li>
            <p>{{ entry.date_added|date:'M d, Y H:i' }}</p>
            <p>{{ entry.text|linebreaks }}</p>
        </li>
    {% empty %}
        <li>There are no entries for this topic yet.</li>
    {% endfor %}
</ul>


{% endblock content %}
```

# Chapter 19: User Accounts

## Allowing Users to Enter Data

### Adding New Topics

#### The Topic ModelForm

learning_log/learning_logs/forms.py

```
from django import forms
from learning_logs.models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["text"]
        labels = {"text": ""}
```

#### The new_topic URL

learning_log/learning_logs/urls.py

```
...
urlpatterns = [
...
    path("new_topic/", views.new_topic, name="new_topic"),
]

```

#### The new_topic() View Function

learning_log/learning_logs/views.py

```
def new_topic(request):
    """Add a new topic."""
    if request.method != "POST":
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("learning_logs:topics")

    # Display a blank or invalid form.
    context = {"form": form}
    return render(request, "learning_logs/new_topic.html", context)
```

#### GET and POST Requests

#### The new_topic Template

learning_log/learning_logs/templates/learning_logs/new_topic.html

```
{% extends "learning_logs/base.html" %}

{% block content %}
<p>Add a new topic.</p>

<form action="{% url 'learning_logs:new_topic' %}" method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button name="submit">Add topic</button>
</form>

{% endblock content %}
```

#### Linking to the new_topic Page

learning_log/learning_logs/templates/learning_logs/topics.html change:

```
{% extends "learning_logs/base.html" %}

{% block content %}

<p>Topics</p>

<ul>
    -- snip
</ul>

<a href="{% url 'learning_logs:new_topic' %}">Add a new topic</a>

{% endblock content %}
```

### Adding New Entries

### The Entry ModelForm

learning_log/learning_logs/forms.py added code

```
class EntryForm(froms.ModelForm):
    class Meta:
        model = Entry
        fields = ["text"]
        labels = {"text": ""}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}
```

#### The new_entry URL

Changes to learning_log/learning_logs/urls.py

```
    # Page for adding a new entry
    path("new_entry/<int:topic_id>/", views.new_entry, name="new_entry"),
```

#### The new_entry() View Function

Changes to learning_log/learning_logs/views.py

```
from learning_logs.forms import TopicForm, EntryForm

def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != "POST":
        # No ddata submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect("learning_logs:topic", topic_id=topic_id)

    # Display a blank for invalid form.
    context = {"topic": topic, "form": form}
    return render(request, "learning_logs/new_entry.html", context)

```

#### The new_entry Template

learning_log/learning_logs/templates/learning_logs/new_entry.html

```
{% extends "learning_logs/base.html" %}

{% block content %}

<p>
    <a href="{% url 'learning_logs:topic' topic.id % }">{{ topic }}</a>
</p>

<p>Add a new entry:</p>
<form action="{% url 'learning_logs:new_entry' topic.id %}" method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button name="submit">Add entry</button>
</form>

{% endblock content %}
```

#### Linking to the new_entry Page

Changes to learning_log/learning_logs/templates/learning_logs/topic.html

```
<p>Topic: {{ topic }} </p>

<p>Entries:</p>
<p>
    <a href="{% url 'learning_logs:new_entry' topic.id %}">Add new entry</a>
</p>
```

### Editing Entries

#### The edit_entry URL

Addition for learning_log/learning_logs/urls.py

```
    # Page for editing an entry.
    path("edit_entry/<int:entry_id>/", views.edit_entry, name="edit_entry"),
```


#### The edit_entry() View Function

learning_log/learning_logs/views.py

```
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != "POST":
        # Initial request; pre-fil form with the current enntry.
        form = EntryForm(instance=entry)
    else:
        # PSOT data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("learning_logs:topic", topic_id=topic.id)

    context = {"entry": entry, "topic": topic, "form": form}
    return render(request, "learning_logs/edit_entry.html", context)

```

#### The edit_entry Template

learning_log/learning_logs/templates/learning_logs/edit_entry.html

```
{% extends "learning_logs/base.html" %}

{% block content %}

<p><a href="{ url 'learning_logs:topic' topic.id %}">{{ topic }}</a></p>

<p>Edit entry:</p>

<form action="{% url 'learning_logs:edit_entry' entry.id %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button name=""submit">Save changes</button>
</form>

{% endblock content %}
```

#### Linking to the edit_entry Page

learning_log/learning_logs/templates/learning_logs/topic.html

```
    {% for entry in entries %}
        <li>
            <p>{{ entry.date_added|date:'M d, Y H:i' }}</p>
            <p>{{ entry.text|linebreaks }}</p>
            <p>
                <a href="{% url 'learning_logs:edit_entry' entry.id %}">Edit Entry</a>
            </p>
        </li>
    {% empty %}
        <li>There are no entries for this topic yet.</li>
    {% endfor %}
```

### Setting Up User Accounts

#### The users App

```
python manage.py startapp users
```

#### Adding users to settings.py

```
INSTALLED_APPS = [
    # My apps
    'learning_logs',
    'users',
```

#### Including the URLs from users

Changes to urls.py

```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('learning_logs.urls')),
]
```

### The Login Page

adding users/urls.py

```
"""Defines URL patterns for users"""

from django.urls import path, include

app_name = 'users'
urlpatterns = [ 
    # Include default auth urls.
    path('', include('django.contrib.auth.urls'))
]
```

[Using the Django authentication system](https://docs.djangoproject.com/en/4.2/topics/auth/default/)

#### The login template

learning_log/users/templates/registration/login.html

```
{% extends 'learning_logs/base.html' %}

{% block content %}

{% if form.errors %}
    <p>Your username and password didn't match. Please try again.</p>
{% endif %}

<form method="post" action="{% url 'users:login' %}">
    {% csrf token %}
    {{ form.as_p }}

    <button name="submit">Log in</button>
    <input type="hidden" name="next" value="{% url 'learning_logs:index' %}" />
</form>
```

#### Linking to the Login Page

learning_logs\templates\learning_logs\base.html

```
    {% if user.is_authenticated %}
        Hello, 
    {% else %}
        <a href="{% url 'users:login' %}">Log in</a>
    {% endif %}
```

### Logging Out

#### Adding a Logout Link to base.html

learning_log/learning_logs/templates/learning_logs/base.html

```
    {% if user.is_authenticated %}
        Hello, {{ user.username }}
        <a href="{% url 'users:logout' %}">Log out</a>
    {% else %}
        <a href="{% url 'users:login' %}">Log in</a>
    {% endif %}
```

#### The Logout Confirmation Page

learning_log/users/templates/registration/logged_out.html

```
{% extends "learning_logs/base.html" %}

{% block content %}
<p> You have been logged out. Thank you for visiting.</p>
{% endblock content %}
```

### The Registration Page

#### The register URL

users/urls.py

```
"""Defines URL patterns for users"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [ 
    # Include default auth urls.
    path('', include('django.contrib.auth.urls'))
    # Registration page.
    path('register/', views.register, name='register')
]
```

#### The register() View Function

users/views.py

```
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display a blank registration form.
        form = UserCreationForm()
    else:
        # Process completed forms.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to the home page.
            login(request, new_user)
            return redirect('learning_logs:index')
        
        # Display a b lank or invalid form.
        context = { 'form': form }
        return render(request, 'registration/register.html')
```

#### The register template

users/templates/registeration/register.html

```
{% extends "learning_logs/base.html" %}

{% block content %}

    <form method="post" action="{% url 'users:register' %}">
        {% csrf_token %}
        {{ form.as_p }}

        <button name="submit">Register</button>
        <input type="hidden" name="next" value="{% url 'learning_logs:index' %}" />
    </form>

{% endblock content %}
```

#### Linking to the Registration Page

learning_log/learning_logs/templates/learning_logs/base.html

```
<p>
    <a href="{% url 'learning_logs:index' %}">Learning Log</a>
    <a href="{% url 'learning_logs:topics' %}">Topics</a>
    {% if user.is_authenticated %}
        Hello, {{ user.username }}
        <a href="{% url 'users:logout' %}">Log out</a>
    {% else %}
        <a href="{% url 'users:register' %}">Register</a>
        <a href="{% url 'users:login' %}">Log in</a>
    {% endif %}
</p>

{% block content %}{% endblock content %}
```

#### Identifying existing users

```
$ python manage.py shell
Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.contrib.auth.models import User
>>> User.objects.all()
<QuerySet [<User: ll_admin>]>
>>> for user in User.objects.all():
...     print(user.username, user.id)
... 
ll_admin 1
```

#### Migrating the database

```
$ python manage.py makemigrations learning_logs
It is impossible to add a non-nullable field 'owner' to topic without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option: 1
Please enter the default value as valid Python.
The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
Type 'exit' to exit this prompt
>>> 1
Migrations for 'learning_logs':
  learning_logs\migrations\0003_topic_owner.py
    - Add field owner to topic
```

```
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, learning_logs, sessions
Running migrations:
  Applying learning_logs.0003_topic_owner... OK
```

Verify that the migration worked as expected.

```
$ python manage.py shell
Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from learning_logs.models import Topic
>>> for topic in Topic.objects.all():
...     print(topic, topic.owner)
... 
Chess ll_admin
Rock Climbing ll_admin
```

### Restricting Topics Access to Approriate Users

