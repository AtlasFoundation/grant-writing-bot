# grant-writing-bot

# Grant Writing Bot

A program to help with grant writing.

## Requirements

- Python 3.6 or higher
- requests
- pymongo (if you are using MongoDB)
- mysql-connector-python (if you are using MySQL)
- nltk

## Installation
```
pip install -r requirements.txt
```

## Usage
```
grant-writing-bot --config path/to/config.py
```

## Configuration

The program uses a configuration file (config.py) to set the various settings.
You need to provide the following information in the config file

- login_url: url to the funding organization's login page
- submit_url: url to the funding organization's submit page
- username: username to login to the funding organization's portal
- password: password to login to the funding organization's portal
- database_url: url of the database
- database_name: name of the database
- collection_name: name of the collection

## Features

- Search and recommend grants that match the user's criteria
- Automated proposal generation
- Submission automation to funding organizations via their online portals
- Reporting and analytics to track the progress of grant applications
- User management to allow multiple users to use the program and access the information stored in the database

## License

This project is licensed under the [MIT License](LICENSE).

```
grant-writing-bot/
|-- README.md
|-- LICENSE
|-- requirements.txt
|-- setup.py
|
|-- src/
    |-- main.py
    |-- config.py
    |-- data/
        |-- grants.sql (replace with database file)
        |-- organizations.sql (replace with database file)
    |-- modules/
        |-- grant_finder.py
        |-- grant_writer.py
        |-- grant_submitter.py
        |-- NLP_module.py (new module for NLP capabilities)
    |-- api/
       |-- funding_org.py (integration with funding organization databases)
    |-- auth/
       |-- user_management.py (User management system)
    |-- analytics/
       |-- reporting.py (Reporting and analytics feature)
```