# Django_CRUD
The project contains the code for performing Create, Read, Update, and Delete Operation using Django-rest.

Here, I have created 2 models: Author and Article.
Article uses Author as foreign key.

Using Django-rest with Serializers, I have performed CRUD operations on Article model.

There is also basic implementation of validators.

The code is unit tested using APIRequestFactory and APIClient under tests.py module.


#Steps to run project:

Pre requisites:
1. Python 3 and above
2. Django 

Steps:
1. cd my_project.
2. Run command: python manage.py runserver

The server will start running on localhost:8000

You can hit the apis using postman.
Django_apis.postman_collection.json file is attached in the same directory. You can import the collection in postamn to view all supported APIs.
