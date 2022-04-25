# crud application
Django application for CRUD operations using postgres as backend

## To clone the project from github
* Clone the project:
```
$ git clone https://github.com/racie7/crud.git
```
* Switch to master branch
$ git switch master

* Install required packages:
```
$ pip install -r requirements.txt
```

* To Run local development  server:
```
$ python manage.py runserver
```
<p>>> The application will run on development server 127.0.0.1:8000</p>

* Make migrations to database:
```
$ python manage.py makemigrations
$ python manage.py migrate
```

* Create an admin user to access the Django Admin Site:
```
$ python manage.py createsuperuser (enter username, email, password)
```
<p>>> To access the Admin Site go to url 127.0.0.1:8000/admin</p>

## To deploy on Heroku
Follow the guide below on how to deploy the app on Heroku
[Link to developer.mozilla.](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment)

