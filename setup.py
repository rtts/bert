#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name = 'bert',
    version = '0.0.1',
    url = 'https://github.com/rtts/bert',
    author = 'Jaap Joris Vens',
    author_email = 'jj@rtts.eu',
    license = 'AGPL3',
    packages = find_packages(),
    include_package_data = True,
    scripts = ['manage.py'],
    python_requires='>=3.6',
    install_requires = [
        'Django==3.0.7',
        'django-extensions==3.0.1',
        'djangorestframework==3.11.0',
        'psycopg2==2.8.5',
        'pylibmc==1.6.1',
    ],
)
