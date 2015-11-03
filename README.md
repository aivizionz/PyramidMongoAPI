# PyramidMongoapp

PyramidMongoapp ia an application built over Python, Pyramid and MongoDB. The app Web API is designed with RESTFUL interface and JSON Message Format.


## Table of contents

* [Quick start](#quick-start)
* [Documentation](#documentation)
* [Creator](#creator)



## Quick start 


### Installation Instructions for Linux

You need to install [MongoDB](https://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/) and [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) on your Linux system.


**Ubuntu Linux Execution Environment**:

    $ mkdir myproject
    $ cd myproject
    $ virtualenv myenv
    $ source myenv/bin/activate
    $ pip install pyramid pyramid_mongodb pyramid_chameleon
    $ git clone git@github.com:mathewraj/pyramidmongoapp.git
    $ cd pyramidmongoapp
    $ python setup.py develop


When the  scripts finishes executing, you should be able to access pyramid application
endpoints by invoking pserve in pyramidmongoapp directory, like so:

    $ pserve development.ini --reload
      Starting subprocess with file monitor
      Starting server in PID 27573
      serving on 0.0.0.0:6543 view at http://127.0.0.1:6543


All other required libraries bootstrap, jquery etc are included in the app.

## Documentation

### Testing the app in local machine

You could access the app Web API through browser or Linux curl command on the default view provided by pserve on localhost:6543.

Before testing ensure that you have configured the MongoDB database and collections as required by pyramidmongoapp. You can use mongo shell and create databases: usersdb and sessiondb.

Create a collection users under usersdb, for users collection schema refer USERS  in [jsondata](https://github.com/mathewraj/pyramidmongoapp/blob/master/myapp/jsondata.py).


    $ mongo
    > use usersdb
    > db.users.find({"firstname" : "amitabh"})
      { "_id" : ObjectId("563673b2a5127f48276b748c"), "city" : "mumbai", "firstname" : "amitabh", "lastname" : "bachan", "profession" : [ "actor", "producer" ], "country" : "india", "genre" : [ "film", "bollywood" ] }



Create a collection session under sessiondb, session collection schema should be as below:

    $ mongo
    > use sessiondb
    > db.session.find({"userid" : "test1"})
      { "_id" : ObjectId("56364d2d004e3e799db7ce40"), "userid" : "test1", "password" : "test4321" }



1. Web API: http://localhost:6543/login. This api authenticates a user using login/password passed in a JSON payload and verifies against a  MongoDB database sessiondb.

2. Web API: http://localhost:6543/users. This api returns all users in the MongoDB database usersdb.

3. Web API: http://localhost:6543/users/(filter: key=value) .These apis returns all users in the database filtered by url parameters (lastname, firstname, city, profession, genre etc)

        http://localhost:6543/users/lastname=cruise      # filter where lastname=cruise
        http://localhost:6543/users/proFesSion=AcTor     # api filter parameters are case-insensitive
        http://localhost:6543/v1/users/proFesSion=AcTor  # api with versioning
        http://localhost:6543/v1/users/genre=film        # filter where genre=film

4. Web API: http://localhost:6543/users/(filter: key=value)/(groupby). These apis returns all users in the database filtered by url parameters (lastname, firstname, city, profession, genre etc) and then group them by another parameter (profession, genre).

        http://localhost:6543/users/city=mumbai/genre          # filter where city=mumbai and groupby genre
        http://localhost:6543/v1/users/ciTy=CaliFornia/geNre   # api with versioning and filter parameters are case-insensitive
        http://localhost:6543/v1/users/ciTy=MumBai/ProfeSsion  # filter where city=mumbai and groupby profession

5. Web API: http://localhost:6543/status/(component).These apis checks and returns the status of the component requested.
    
        http://localhost:6543/status/mongod      # filter component mongod
        http://localhost:6543/v1/status/firefox  # api with versioning and filter component firefox 

6. Web API: http://localhost:6543/files/(directory path). These apis returns the list of files in a given directory. components 
    
        http://localhost:6543/files/pyramidmongoapp                 # filter with directory path '/pyramidmongoapp'
        http://localhost:6543/v1/files/pyramidmongoapp/myapp/static # api with versioning and filter  with directory path '/pyramidmongoapp/myapp/static'

      

### Technologies Used:

Pyramid (http://www.pylonsproject.org/) : Pyramid is a simple, fast and less opinionated web framework that can be used to build complex web applications with components of our choice, like ORMs( SQL Alchemy, Ming), templating languages(Chameleon, Mako, jinja2) etc.
Also in my case, my present org is using zope and custom web framework  and we are  migrating all our app modules to pyramid.  Pyramid will have less learning curve for people already using zope or pylons.

pyramid_chameleon (http://pyramid-chameleon.readthedocs.org/en/latest/) : No special preference on this templating system for Pyramid. Used this one as it is mentioned/used in pyramid tutorial docs by default.

pyramid_mongodb (https://github.com/niallo/pyramid_mongodb ): pyramid_mongodb is a simple scaffold for the Pyramid Web Framework. It provides URL mapping via traversal and persistence via MongoDB. This template speeds up development (for proof of concept) as it can create the base  project structure and config files (ini, setup files etc) required for the app project.

MongoDB (https://www.mongodb.org/ ) : MongoDB is a very popular NoSQL (document-oriented) database designed for ease of development. 

pymongo (http://api.mongodb.org/python/current/api/pymongo/index.html#module-pymongo) : pymongo is the recommended python driver for MongoDB


### API Versioning:

API versioning helps smoothen application changes with API version transitions where we can continue to offer older APIs for a period of time. 
I have used the url for the API versioning(most popular) starting with the letter v<version no> , ex v1 (http://localhost:6543/v1/users). it's good to avoid dot notation like 1.2 , as v1 or v2 is more readable and easy to follow.

There are other options for API versioning  like using the header for API versions or a combination of both (URL and header). 


### Pagination: 

Pagination is not implemented in the present API. But can be supported with existing design. 

Traditionally pagination data used to be send in post request  along with payload or for get request in URL query parameters.  

Better approach is to use the Link Header for Pagination as below. 

    Link: <http://localhost:6543/users/?page=2>; rel="next"
    

We can also specify how many items to receive like (users?page=3&per_page=100) but,
for technical reasons, many client side libraries/framework  misbehaves and can cause browser crashes (ex: AngularJS  with ie8 and  ie9)  hence not recommended. It is good to stick with  default records of 10 or 20 per page.


### Coding Standards and Server Side (Backend) architecture:

I have used Sublime2 as my IDE with Flake8 Lint for python which confirms to pep8 and pyflakes standards. Meaningful method/function names and variables are used in most cases. Doc strings added to each method/function.

For  server side (Backend) I have used Model and ViewController like pattern  with all routes in __init__.py file , View-Controller  together in views.py and Model (data access layer) in models.py. Further server side optimisations can be done for the existing app.
 


### Creator

**Rajesh Mathew**

* github: <https://github.com/mathewraj>
* twitter: <https://twitter.com/rajeshmathewk>

