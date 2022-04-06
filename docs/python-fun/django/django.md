# Intro to Django

## Usage notes
Django says the difference according to Django is an "app" is a web application that does something. 

A "project" is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects

The `include()` function allows referencing other URLconfs
- Whenever Django encounters `include()`, it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing
- The idea behind `include()` is to make it easy to plug-and-play URLs.
- You should always use `include()` when you include other URL patterns. `admin.site.urls` is the only exception to this.

The `path()` function is passed four arguments, two required, **route** and **view**, and two optional: **kwargs**, and **name**. 
- `path(route)` is a string that contains a URL pattern.
  - When processing a request, Django starts at the first pattern in `urlpatterns` and makes its way down the list, comparing the requested URL against each pattern until it fines one that matches.
  - Patterns don't search GET and POST parameters, or the domain name.
- `path(view)` is when Django finds a matching pattern, it calls the specified view function with an `HttpRequest` object as the first argument and any "captured" values from the route as keyword args

## Database setup
By default, the configuration uses SQLite which is included in Python. When starting your first project you may want to use a more scalable db like PostgreSQL.

If you want to install a different db than SQLite, install the appropriate database bindings and change the following keys in the DATABASES 'default' item to match your database connection settings:
- ENGINE – Either 'django.db.backends.sqlite3', 'django.db.backends.postgresql', 'django.db.backends.mysql', or 'django.db.backends.oracle'. Other backends are also available.
- NAME – The name of your database. If you’re using SQLite, the database will be a file on your computer; in that case, NAME should be the full absolute path, including filename, of that file. The default value, os.path.join(BASE_DIR, 'db.sqlite3'), will store the file in your project directory.
- For db's other than SQLite
  - make sure you've created a database by this point. Do that with "CREATE DATABASE database_name;" within your db's interactive prompt

To migrate to SQL db you need to:
- Change your models in models.py
- Run `python manage.py makemigrations` to create migrations for those changes
  - To check if it's creating the write tables, run `python manage.py sqlmigrate polls 0001`
- Run `python manage.py migrate` to apply those changes to the database

## Start development server
The Django admin site is activated by default. To start the development server run:
```
python manage.py createsuperuser
```
You'll be prompted to enter a username and password, then run:
```
python manage.py runserver
```

## What is it?
Django is a Python based web framework that enables rapid development of secure and maintainable websites. 
- It's "complete" in that it comes with built in tools that is as comphrehensive as possible
- It's versatile in that it's used to build almost any type of website. 
  - It can work with any client-side framework, and can deliver content in almost any format ie HTML, RSS feeds, JSON, XML. 
- It comes with built in security like handling session information and password and account management. It can directly store passwords rather than using a hash.
  - Password hash is a fixed-length value created by sending the password through a cryptographic hash function. Django checks if  an enetered password is correct by running it through the hash function and comparing the output  to the stored hash value. 
    - Due to the "one way nature" of the function, even if a sotred hash value is compromised it is hard for an attacker to work out the original password
  - Django enables protection against SQL injection, cross-site scripting, cross-site request forgery and clickjacking.
- It's scalable in that it uses a component-based architecture. Each part of the architecture is independent of the others. 
- It's maintainable by using the DRY principle so there is no unnecessary duplication.
  - Django also promotes the grouping of related functionality into reusable applications and at a lower level groups related code into modules following the MVC pattern

Django is a "somewhat opinionated" framework. Meaning it provides a set of components to handle most web development tasks and one or two preferred ways to use them. It's decoupled architecture means you can usually pick and choose from a  number of different options, or add support for completely new ones

## How does it work?
Django web applications typically group the code that handles HTTP requests into separate files:
- Model View Template (MVT) architecture

### URLS
Django handles URL's using a URL mapper which redirects HTTP requests to the appropriate view based on the request URL
- The URL mapper is typically stored in a file named `urls.py`
- The mapper itself can be a variable that stores a list of paths per route and corresponding view functions. 
- When an HTTP request is received that matches a specific pattern, then the associated view function will be called and passed the request.

URL mapper example:
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
    path('catalog/', include('catalog.urls')),
    re_path(r'^([0-9]+)/$', views.best),
]
```

The first argument to both methods is a route pattern that will be matched.
  - The `path()` method uses angle brackets to define parts of a URL domain that will be captured and passed through to the view function as named arguments
  - The `re_path()` function uses regex 

The second argument is another function that will be called when the pattern is matched.
  - The notation `views.book_detail` indicates that the function is called `book_detail()` in the `views` module (in a file named views.py)

### Views
View is a request handler function which receives HTTP requests and returns HTTP responses
- Views access the data needed to satisfy requests via _models_, and delegate the formatting of the response to _render templates_
  - Handled by a `index()` view function
  - Receives an `HttpRequest` object as a parameter (request) and returns `HttpResponse` object. 
```
# filename: views.py (Django view functions)

from django.http import HttpResponse

def index(request):
    # Get an HttpRequest - the request parameter
    # perform operations using information from the request.
    # Return HttpResponse
    return HttpResponse('Hello from Django!')
```


### Models
Python objects that define the structure of the applications data, provide mechanisms to manage (add, modify, delete), and delegate the formatting of the reponse to _templates_
- Models define the structure of stored data, including the field types and their size,
  - default values,
  - selection list options,
  - help text for documentation,
  - label text for forms, etc

Once you've chosen what database you want to use, you don't need to talk to it directly at all, you just write your model structure and other code, and Django handles communicating with the database. 

Model example:
```
# filename: models.py

from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=40)

    TEAM_LEVELS = (
        ('U09', 'Under 09s'),
        ('U10', 'Under 10s'),
        ('U11', 'Under 11s'),
        ...  #list other team levels
    )
    team_level = models.CharField(max_length=3, choices=TEAM_LEVELS, default='U11')
```
The Model provides a simple query API for searching the associated database.
- It can match against a number of fields at a time using different criteria

Taking the `views.py` code snippet above, it could do this when importing the models module:
```
## filename: views.py

from django.shortcuts import render
from .models import Team

def index(request):
    list_teams = Team.objects.filter(team_level__exact="U09")
    context = {'youngest_teams': list_teams}
    return render(request, '/best/index.html', context)
```
The `render()` function creates the `HttpResponse` that is sent back to the browser

### Templates
A text file defining the structure or layout of a file, with placeholders used to represent actual content. 
- Template systems allow you to specify the output of the document, using placholders for data that will be filled in when a page is generated.
- Django supports both its native templating system and another Python library called Jinja2
- The `render()` function above will call a template that could like this:
```
## filename: best/templates/best/index.html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Home page</title>
</head>
<body>
  {% if youngest_teams %}
    <ul>
      {% for team in youngest_teams %}
        <li>{{ team.team_name }}</li>
      {% endfor %}
    </ul>
  {% else %}
    <p>No teams are available.</p>
  {% endif %}
</body>
</html>
```



### Resources
- [Getting Started](https://www.djangoproject.com/start/)
- [How Django Works Behind the Scenes](https://wsvincent.com/how-django-works-behind-the-scenes/)
- [What is Django](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction)
- [First Django App Part one](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)
  - [Part Two](https://docs.djangoproject.com/en/3.0/intro/tutorial02/)

 (../index.md)
