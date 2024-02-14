

# List of Django Projects

* Basic template - created with `startproject` and `startapp`
* Minimal server - manually created template
* Basic structure with landing page (jinja) - app `foo/bar/templates` and project `foo/templates`
* Minimal REST API - uses `django-rest-framework`
* Advanced ORM REST API - uses the django orm
* Basic REST API with security - ``
* Basic REST API with celery - ``



## Structure

Install

```shell
pipenv install django-cors-headers
```


Start with basic django project template:

```shell
$ pipenv install
$ pipenv shell

$ django-admin startproject foo
$ cd foo
$ python manage.py startapp api

$ python manage.py migrate
$ python manage.py createsuperuser --username admin --email admin@example.com
```


In `foo/settings.py` add:

```python
#ALLOWED_HOSTS = ['localhost']

CORS_ALLOW_ALL_ORIGINS = False

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173'
]

INSTALLED_APPS = [
    ...
    'django-extensions',
    'rest_framework',
    'api.apps.ApiConfig',
    'corsheaders'
    ]
...
MIDDLEWARE = [
    ...
    'corsheaders.middleware.common.CorsMiddleware'
]
...
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

The directory structure:

```
$ tree foo
foo
├── api
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_rename_user_examiner.py
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
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
├── load_data.py
└── manage.py
```


## Models


__Meta__

* UserDocumentGroup - groups assigned to User

__User__

* Examiner ~~User~~ - basic level (`User` is used by the system)
* Note - associated with User's DocumentGroups
* DocumentHistory - docs within DocumentGroups that were previously accessed by User
* SearchHistory - category and pattern of each search

__App__

* DocumentGroup - basic group of documents
* Document - file blobs
* Index - created from files


To interact with the models, directly, the `shell_plus` command from `django-extensions` which automatically loads the models defined in the project and displays the generated SQL.

```shell
python manage.py makemigrations
python manage.py migrate

python manage.py shell_plus --print-sql

>>> e = User(name='John Doe')
>>> e.save()
```

Load the test data into the `db.sqlite` file with:

```shell
python load_data.py

sqlite3 db.sqlite 
sqlite> .headers on
sqlite> .mode columns
sqlite> select * from api_examiner;
sqlite> .exit
```

Or, in a single line: `sqlite3 db.sqlite3  -header -column 'select * from api_examiner;'`


## Run

Run the backend server with:

```shell
$ cd foo
$ python manage.py runserver
```

Run the frontend server with:

```shell
$ cd client
$ npm run dev
```

Now visit: `http://localhost:8000/`.



## TODO

* [joins](https://www.pythontutorial.net/django-tutorial/django-one-to-one/)
* [py create uint8array from file](https://stackoverflow.com/questions/71036800/how-to-write-file-with-data-is-uint8array)


## References

* [Django REST Framework](https://www.youtube.com/watch?v=cJveiktaOSQ)
* [Basic structure with landing page (jinja)](https://www.youtube.com/watch?v=-qUoCBExAvY)
* [Minimal REST API](https://www.youtube.com/watch?v=DvNBQm_M6q8)