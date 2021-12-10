# crypto_tracker

Application for friends to be able to be able to search and save crypto-currencies as weekly/monthly favorites. At the duration of the 'term' of the, the member with the most 'winnings' will earn points. The idea of the game stems from wanting to learn more about crypto currency and to gain the ability to automate real-time tracking using Python.

## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on deploying the project on a live system.

### Prerequisites

Requirements for the software and other tools to build, test and push

- [Poetry](https://python-poetry.org/)
- [Python](https://www.python.org/)

### Installing

A step by step series of examples that tell you how to get a development
environment running

Download and install poetry

    Windows

        (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -

    Mac OS/ Linux

        curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

Avtivate virtual environment

    poetry shell

Install dependencies

    poetry install

Run server

    python manage.py runserver

## Built With

- [Python](https://www.python.org/)

- [Django](https://www.djangoproject.com/)
