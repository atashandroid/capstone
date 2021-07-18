Udacity Full-Stack Developer Nanodegree Capstone Project
-----

## Introduction

This Musical Compositions is a company that responsible for creating musical compositions and managing and assigning musicians to those compositions.
This is a server only application.

### Application Link
```
Heroku Link: https://musicalcomposition.herokuapp.com
Locally running: http://localhost:5000
```
## Application Stack

###  Dependencies
Tech stack will include the following:
 * **Flask** lightweight backend microservices framework. Flask is required to handle requests and responses
 * **SQLAlchemy ORM** is the Python SQL toolkit and ORM library
 * **PostgreSQL** is a relational database
 * **Auth0** is the authentication and authorization system
 * **Flask-Migrate** for creating and running schema migrations
 * **Heroku** is the cloud platform for deployment

## Development Setup
* **Clone the Repository**
```
https://github.com/atashandroid/capstone.git
```
* **Initialize and activate a virtualenv using:**
```
python -m virtualenv env
source env/bin/activate
```
>**Note** - In Windows, the `env` does not have a `bin` directory. Therefore, you'd use the analogous command shown below:
```
source env/Scripts/activate
```

* **Install the dependencies:**
```
pip install -r requirements.txt
```

* **Run the development server:**
```
export FLASK_APP=app.py
export FLASK_ENV=development # enables debug mode
flask run
```
## API Reference
### Roles
The application has two types of roles:

   * **Assistant**
   
        can only view the list of Compositions and Musicians
        has get:compositions, get:musicians permissions
        
   * **Director**
   
        can perform all the actions that Assistant can
        can create, update information and delete musicians and compositions
        has post:compositions, post:musician, delete:compositions, delete:musician, 
        patch:compositions, patch:musician permissions in addition to all the permissions that Assistant has
        
### The endpoints are as follows:

* **GET '/compositions'** This endpoint fetches all the compositions in the database and displays them as json

* **GET '/musicians'** This endpoint fetches all the musicians in the database and displays them as json

* **POST '/compositions/create'** This endpoint will create a new composition in the database

* **POST '/musicians/create'** This endpoint will create a new musician in the database

* **DELETE '/compositions/delete/int:composition_id'** This endpoint will delete the composition

* **DELETE '/musicians/delete/int:musician_id'** This endpoint will delete the musician

* **PATCH '/compositions/patch/int:composition_id'** This endpoint will update the composition 

* **PATCH '/musicians/patch/int:musician_id'** This endpoint will update the musician information
