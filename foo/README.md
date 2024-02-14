

# List of Django Projects

* Basic template - created with `startproject` and `startapp`
* Minimal server - manually created template
* Basic structure with landing page (jinja) - app `foo/bar/templates` and project `foo/templates`
* Minimal REST API - uses `django-rest-framework`
* Basic REST API with security - ``
* Basic REST API with celery - ``






## Basic Django Template

Start with basic django project template:

```
$ django-admin startproject foo
$ python foo/manage.py startapp bar
$ mkdir foo/bar/templates
$ mkdir foo/templates
```

```
$ tree foo
foo
├── README.md
├── bar
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── templates
│   │   ├── index.html
│   │   └── news.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── foo
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── templates
    ├── main.html
    └── navbar.html
```

Prepare the database and run the server with:

```
python manage.py migrate
python foo/manage.py runserver
```

Notice the new `db.sqlite3` file, and visit: `http://localhost:8000/`.