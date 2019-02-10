
# politico
[![Build Status](https://travis-ci.com/Muart-C/politico.svg?branch=develop)](https://travis-ci.com/Muart-C/politico)
[![Coverage Status](https://coveralls.io/repos/github/Muart-C/politico/badge.png?branch=develop)](https://coveralls.io/github/Muart-C/politico?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/71270642743b6a0883b3/maintainability)](https://codeclimate.com/github/Muart-C/politico/maintainability)


# Install this requirements
- [Python 3.6](https://www.python.org/)


# Politico API Endpoints

| Method  | Endpoint                                   | What the endpoint does                            |
| ------- | ------------------------------------------ | --------------------------------------------------|
| `POST`  | `/api/v1/parties`                          | creates a political party                         |
| `GET`   | `/api/v1/parties`                          | returns all political parties                     |
| `GET`   | `/api/v1/parties/party_id>`                | returns a specific political party                |
| `PATCH` | `/api/v1/parties/<party_id>/name`          | updates the name of the political party           |
| `DELETE`| `/api/v1/parties/party_id>`                | deletes a specific political party                |
| `POST`  | `/api/v1/offices`                          | creates a government office                       |
| `GET`   | `/api/v1/offices`                          | returns all the government offices                |
| `GET`   | `/api/v1/parties/party_id>`                | returns a specific government office              | 


# steps to setup the application locally

- clone the git repo
```
$ git clone https://github.com/Muart-C/politico.git
```
- cd into the project directory
```

$ cd politico
```

- create the virtual environment and activate it
```
$ virtualenv venv
$ source .env
```
- install dependencies
```
$ pip install -r requirements.txt
```

# How to run the Application

- Then execute the following app to run the app
```
$ export FLASK_APP = "run.py"
$ export FLASK_ENV="development"
$ flask run
```

# How to Test the Application
------------------------------------------------------------------
## How to run the unit tests
 On your terminal execute the following command
 
 ```
 $ pytest --cov=api tests/
 ```

# Testing The API Endpoints
Use any API Test Client 
Insomnia is preferred since it is lightweight
Get it here => [Insomnia Test Client](https://insomnia.rest/download/)

or 

You can use Postman get it here => [Postman](https://www.getpostman.com/downloads/)

# Here is a collection of endpoints open via postman
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/55e0954df1faa13e63ad)

# Credits
[Andela Bootcamp](https://andela.com/)


# Author
Charles Muathe Ndirangu
