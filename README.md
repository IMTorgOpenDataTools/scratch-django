

# List of Django Projects

* Basic template - created with `startproject` and `startapp`
* Minimal server - manually created template
* Basic structure with landing page (jinja) - app `foo/bar/templates` and project `foo/templates`
* Minimal REST API - uses `django-rest-framework`
* Basic REST API with security - ``
* Basic REST API with celery - ``



## Structure

Start with basic django project template:

```shell
$ django-admin startproject foo
$ cd foo
$ python manage.py startapp api

$ python manage.py migrate
$ python manage.py createsuperuser --username admin --email admin@example.com
```


In `foo/settings.py` add:

```python

INSTALLED_APPS = [
    ...
    'django-extensions',
    'rest_framework',
    'api.apps.ApiConfig'
    ]
...

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```



```
$ tree foo

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

```
python manage.py makemigrations
python manage.py migrate

python manage.py shell_plus --print-sql
>>> e = User(name='John Doe')
>>> e.save()
```


## Run

Prepare the database and run the server with:

```
python foo/manage.py runserver
```

Notice the new `db.sqlite3` file, and visit: `http://localhost:8000/`.