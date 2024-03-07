MyNotes
==============================

MyNotes Backend

## Getting up and running

Install Virtual env

```
pip install virtualenv
```
```
Once a virtualenv is created you can switch to that using

```
```

Minimum requirements: **pip, python3, & [postgres][install-postgres]**, setup is tested on Mac OSX only.

```
brew install libmagic postgres python3 postgis
```

Create the database 

```
createdb notes_db
```

Once you have created/activated virtual environment. Install all the python requirements

```
pip install -U -r requirements.txt
```

Install pre-commit

```
pre-commit install
```

Update db and Start local server and visit localhost:8000

```
python manage.py migrate
python manage.py runserver
```

If using linux/ubuntu follow: http://stackoverflow.com/a/34631976/1906584

For API documentation plese run following commands

```
mkdocs serve
```
Once mkdocs is running, browse to http://127.0.0.1:8000/ 

## Contributing

Golden Rule:

> Anything in **master** is always **deployable**.

Avoid working on `master` branch, create a new branch with meaningful name, send pull request asap. Be vocal!

[install-postgres]: http://www.gotealeaf.com/blog/how-to-install-postgresql-on-a-mac
