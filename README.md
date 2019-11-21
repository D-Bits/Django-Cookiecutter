
## About

A basic, Django template project, meant to be used in conjunction with Cookiecutter, and PostgreSQL.

## Addtion libaries used.

* *psycopg2*
* *Crispy Forms*

## Initial Setup

After the template has been scaffolded, and you have Pipenv installed, run *pipenv install* to create a virtualenv and install dependencies.

IMPORTANT: A *SECRET_KEY* is not provided. You must generate that yourself, and store in an env var named *PROJECT_NAME_SECRET_KEY*

Also, the timezone in *settings.py* is set to Pacific Standard Time. If you are in a different timezone, please remember to edit that variable.

## The *tasks.py* file

The file called *tasks.py* is used to automate *manage.py*, and other tasks. Simply run it from the terminal (with your virtualenv running), and follow the prompts. 