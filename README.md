
# politico
[![Build Status](https://travis-ci.com/muathendirangu/politico.svg?branch=develop-V2)](https://travis-ci.com/Muart-C/politico)[![Coverage Status](https://coveralls.io/repos/github/muathendirangu/politico/badge.svg?branch=develop-V2)](https://coveralls.io/github/Muart-C/politico?branch=develop-V2)
[![Maintainability](https://api.codeclimate.com/v1/badges/71270642743b6a0883b3/maintainability)](https://codeclimate.com/github/muathendirangu/politico/maintainability)


# Install this requirements
- [Python 3.6](https://www.python.org/)


# Politico API Endpoints

| Method  | Endpoint                                   | What the endpoint does                            |
| ------- | ------------------------------------------ | --------------------------------------------------|
| `POST`  | `/api/v2/auth/signup`                      | create a new user                                 |
| `POST`  | `/api/v2/auth/login`                       | login user                                        |
| `POST`  | `/api/v2/parties`                          | creates a political party                         |
| `GET`   | `/api/v2/parties`                          | returns all political parties                     |
| `GET`   | `/api/v2/parties/party_id>`                | returns a specific political party                |
| `PATCH` | `/api/v2/parties/<party_id>/name`          | updates the name of the political party           |
| `DELETE`| `/api/v2/parties/party_id>`                | deletes a specific political party                |
| `POST`  | `/api/v2/offices`                          | creates a government office                       |
| `GET`   | `/api/v2/offices`                          | returns all the government offices                |
| `GET`   | `/api/v2/offices/<office_id>`              | returns a specific government office              | 
| `POST`  | `/api/v2/offices/<candidate_id>/register`  | register a candidate                              |
| `POST`  | `/api/v2/votes/`                           | vote for a candidate                              |
| `POST`  | `/api/v2/offices/<office_id>/results`      | return results of an election                     |


# steps to setup the application locally

- clone the git repo
```
$ git clone https://github.com/Muart-C/politico.git
```
- cd into the project directory
```

$ cd politico

$ git checkout develop-V2
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
