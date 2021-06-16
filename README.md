# SocialNetworkAPI
A simple REST API, using Django Rest Framework.
## Basic models:
* • User
* • Post (always made by a user)
## Basic Features:
* • User signup
* • User login
* • User logout
* • Users list
* • User detail (shows time of user's last login and request to the service)
* • Post creation
* • Posts list
* • Post detail
* • Post like
* • Post unlike
* • Analytics about how many likes was made, aggregated by day  
Example url:  
>/api/analitics/?date_from=2020-02-02&date_to=2020-02-15
## Running locally
* • Clone the repository, create virtual environment.
* • Install requirements:  
```
pip install -r requirements.txt
```
* • Apply migrations:  
```
python manage.py migrate
```
* • Run the server:  
```
python manage.py runserver
```
## API Endpoints
[POSTMAN Documentation](https://documenter.getpostman.com/view/16211699/TzeWH87k)
