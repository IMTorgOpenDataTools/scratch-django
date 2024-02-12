


## Basic Django Template

Start with basic django project template:

```
$ django-admin startproject foo
```

Remove either asgi.py or wsgi.py:

```
$ tree foo
foo
├── foo
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

Prepare the database and run the server with:

```
python manage.py migrate
python foo/manage.py runserver
```

Notice the new `db.sqlite3` file, and visit: `http://localhost:8000/`.