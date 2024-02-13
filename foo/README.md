


## Basic Django Template

Start with basic django project template:

```
$ django-admin startproject foo
$ cd foo
$ python manage.py startapp bar
```

Remove either asgi.py or wsgi.py:

```
$ tree foo
foo
├── README.md
├── bar
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── foo
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

Prepare the database and run the server with:

```
python manage.py migrate
python manage.py runserver
```

Notice the new `db.sqlite3` file, and visit: `http://localhost:8000/`.