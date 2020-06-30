Bert's coffee, bedding and more!
================================

_Welcome to Bert's webshop! Bert sells fresh coffee beans in a variety
of tastes, as well as limited edition bedding!_

This repository contains all of Bert's backend, written in
[Django](http://www.djangoproject.com/) using [Django REST
Framework](https://www.django-rest-framework.org/).

Installation
------------

Before installing Bert's backend, it is highly recommended to setup a
[Python Virtual Environment](https://docs.python.org/3/tutorial/venv.html):

    mkdir -p ~/.virtualenvs
    python3 -m venv ~/.virtualenvs/bert
    . ~/virtualenvs/bert/bin/activate

Then, simply install this package with pip:

    python3 -m pip install git+https://github.com/rtts/bert

Setup
-----

To get up and running, first create a PostgreSQL database with owner
`bert` and name `bert`:

    sudo su postgres
    createuser bert
    createdb -O bert bert

(Or use whatever database management tools you're comfortable with!)

Then, run the following Django management commands (note that pip has
installed `manage.py` in your `PATH`):

    manage.py migrate
    manage.py createsuperuser
    manage.py runserver

All done! Visit https://localhost:8000/admin/ in your browser and start
adding some products for Bert's webshop!
