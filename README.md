# PyramidMongoapp

PyramidMongoapp ia an application built over Python, Pyramid and MongoDB. The myapp Web API is designed with RESTFUL interface and JSON as Message Format.


## Table of contents

* [Quick start](#quick-start)
* [Documentation](#documentation)
* [Creators](#creators)



## Quick start 


### Installation Instructions for Linux

You need install [MongoDB](https://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/) and [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) on your Linux system.


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

You could access the myapp Web API through browser or Linux curl command on the default view provided by pserve on localhost:6543.

Before testing ensure that you have configured the MongoDB database and collections as required by pyramidmongoapp. You can use mongo shell and create databases: usersdb and sessiondb.

Create a collection users under usersdb, refer USERS collection  in [jsondata](https://github.com/mathewraj/pyramidmongoapp/blob/master/myapp/jsondata.py).
 
Create a collection session under sessiondb, structure should be as below:

    $ mongo
    > use sessiondb
    > db.session.find({"userid" : "test1"})
      { "_id" : ObjectId("56364d2d004e3e799db7ce40"), "userid" : "test1", "password" : "test4321" }



1. Web API: http://localhost:6543/login. This api authenticates authenticates a user using login/password passed in a JSON payload and verifies against a simple data structure , MongoDB

2. Web API: http://localhost:6543/users. This api   returns all users in the MongoDB database usersdb.
3. Web API: http://localhost:6543/users/<key=value> .These api returns all users in the database filtered by url parameters (lastname, firstname, city, profession, genre etc)

        http://localhost:6543/users/lastname=cruise
        http://localhost:6543/users/proFesSion=AcTor      # apis filter parameters are case-insensitive
        http://localhost:6543/v1/users/proFesSion=AcTor   # apis with versioning
        http://localhost:6543/v1/users/genre=film

4. Web API: http://localhost:6543/users. This api   returns all users in the MongoDB database usersdb.
5. Web API: http://localhost:6543/users. This api   returns all users in the MongoDB database usersdb.



## Creators

**Rajesh Mathew**

* <https://github.com/mathewraj>

