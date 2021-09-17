# crypto_tracker

I am building this application to be able to search and track current crypto-currencies by entering in their crypto symbol. You can access the code inside of the crypto_tracker directory. Within that directory, there is 2 programs; 

1. [cli]: main.py -> python main.py <symbol>
2. [gui]: gui.py -> python main.py




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

Start CLI file

    python python main.py <SYMBOL>

Start GUI file

    python python gui.py


## Built With

  - [Python](https://www.python.org/) - Used
    for the Code of Conduct
  - [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/) - Used to choose
    the license


## Authors

  - **Jacob Short** 


  - **Billie Thompson** - *Provided README Template* -
    [PurpleBooth](https://github.com/PurpleBooth)






