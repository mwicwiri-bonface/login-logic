# Login Logic APp

## Setup & Configurations

Create a `settings.ini` file in the core folder.


Add SECRET_KEY and Set DEBUG mode


Create a virtual environment to install dependencies in and activate it:

```sh
$ pip install virtualenv
$ virtualenv venv
$ venv/bin/activate
```

Then install the dependencies:

```sh
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
```sh
python manage.py createsuperuser
```

Login in the admin with the created username and password to created normal users and receive account creation requests.