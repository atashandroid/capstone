Udacity Full-Stack Developer Nanodegree Capstone Project
-----

## Introduction

This Musical Compositions is a company that responsible for creating musical compositions and managing and assigning musicians to those compositions.
This is a server only application.

## Auth0 account
```
AUTH0_DOMAIN = '***.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'casting'
```
⚠️ I updated the POSTman collection with both assistant and director accounts, also I've created two dummy accounts on my Auth0 profile, both of them are verified and functional.

Director account
```
User: director_capstone@udacity.com
password: Udacity2!
Token:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlkzbUQ0c19Tc3M5VGZXUHdReFgxMCJ9.eyJpc3MiOiJodHRwczovL2F0YXNoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGY0NDk2MjhjYjIxMjAwNjk3MmM5N2MiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNjI2NzE2NDAwLCJleHAiOjE2MjY4MDI4MDAsImF6cCI6IkZKTUVGaERCTHRzOEZaSXN3ejZOU3VIUGVyYzdEaFJ1Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Y29tcG9zaXRpb25zIiwiZGVsZXRlOm11c2ljaWFuIiwiZ2V0OmNvbXBvc2l0aW9ucyIsImdldDptdXNpY2lhbnMiLCJwYXRjaDpjb21wb3NpdGlvbnMiLCJwYXRjaDptdXNpY2lhbiIsInBvc3Q6Y29tcG9zaXRpb25zIiwicG9zdDptdXNpY2lhbiJdfQ.USFtwAAerrXxuRyWzCGlDVheCo7G9_K9qx4bmKn54JUTmRogTkIOHYJFqXsIQqXQlDdq7n43diB-myP_c8Q61lPrKej_3V2VkI6PLvquCiMsn98La8kA-my7wA1t1sIzNW6jIS3s0AdKSuU4AeZ6HxGy4rTzHyx3wSoH8nGoWKz6qhOaMg4vFMV6-nCfqx7vVS6S8S_XP_v33NtM_rkogMPOqA4GL32ywCAq4sctovZkEXvZBm7oew4QDstd8tNGfAxftJ9iFDWp2F_PT0q5HSgsi4KrRgVhj6nEytR_E_c7eNxVEQXBb7mIiHNQuT_EOamdX04NrZx3XClvqCRiIQ
```
Assistant account
```
User: assistant_capstone@udacity.com
password: Udacity2!
Token:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlkzbUQ0c19Tc3M5VGZXUHdReFgxMCJ9.eyJpc3MiOiJodHRwczovL2F0YXNoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGY0NDk2MjhjYjIxMjAwNjk3MmM5N2MiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNjI2NzE2NDAwLCJleHAiOjE2MjY4MDI4MDAsImF6cCI6IkZKTUVGaERCTHRzOEZaSXN3ejZOU3VIUGVyYzdEaFJ1Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Y29tcG9zaXRpb25zIiwiZGVsZXRlOm11c2ljaWFuIiwiZ2V0OmNvbXBvc2l0aW9ucyIsImdldDptdXNpY2lhbnMiLCJwYXRjaDpjb21wb3NpdGlvbnMiLCJwYXRjaDptdXNpY2lhbiIsInBvc3Q6Y29tcG9zaXRpb25zIiwicG9zdDptdXNpY2lhbiJdfQ.USFtwAAerrXxuRyWzCGlDVheCo7G9_K9qx4bmKn54JUTmRogTkIOHYJFqXsIQqXQlDdq7n43diB-myP_c8Q61lPrKej_3V2VkI6PLvquCiMsn98La8kA-my7wA1t1sIzNW6jIS3s0AdKSuU4AeZ6HxGy4rTzHyx3wSoH8nGoWKz6qhOaMg4vFMV6-nCfqx7vVS6S8S_XP_v33NtM_rkogMPOqA4GL32ywCAq4sctovZkEXvZBm7oew4QDstd8tNGfAxftJ9iFDWp2F_PT0q5HSgsi4KrRgVhj6nEytR_E_c7eNxVEQXBb7mIiHNQuT_EOamdX04NrZx3XClvqCRiIQ
```
POSTman
Exported collection with configured tokens can be found at: /Udacity_capstone_postman_collection.postman_collection.json
#### Login
```
https://YOUR_DOMAIN/authorize?audience=API_IDENTIFIER&response_type=token&client_id=YOUR_CLIENT_ID&redirect_uri=https://musicalcompositions.herokuapp.com/login-results
```
### Application Link
```
Heroku Link: https://musicalcompositions.herokuapp.com
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
