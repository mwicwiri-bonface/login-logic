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
python manage.py runserver
```