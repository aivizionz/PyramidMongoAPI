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



1. Web API: http://localhost:6543/login. This api authenticates a user using login/password passed in a JSON payload and verifies against a  MongoDB database sessiondb.

2. Web API: http://localhost:6543/users. This api returns all users in the MongoDB database usersdb.

3. Web API: http://localhost:6543/users/(filter: key=value) .These apis returns all users in the database filtered by url parameters (lastname, firstname, city, profession, genre etc)

        http://localhost:6543/users/lastname=cruise      # filter where lastname=cruise
        http://localhost:6543/users/proFesSion=AcTor     # api filter parameters are case-insensitive
        http://localhost:6543/v1/users/proFesSion=AcTor  # api with versioning
        http://localhost:6543/v1/users/genre=film        # filter where genre=film

4. Web API: http://localhost:6543/users/(filter: key=value)/(groupby). These apis returns all users in the database filtered by url parameters (lastname, firstname, city, profession, genre etc) and then group them by another parameter (profession, genre).

        http://localhost:6543/users/city=mumbai/genre          # filter where city=mumbai and groupby genre
        http://localhost:6543/v1/users/ciTy=CaliFornia/genre   # api with versioning and filter parameters are case-insensitive
        http://localhost:6543/v1/users/ciTy=MumBai/profession  # filter where city=mumbai and groupby profession

5. Web API: http://localhost:6543/status/(component).These apis checks and returns the status of the component requested.
    
        http://localhost:6543/status/mongod      # filter component mongod
        http://localhost:6543/v1/status/firefox  # api with versioning and filter component firefox 

6. Web API: http://localhost:6543/files/(directory path). These apis returns the list of files in a given directory. components 
    
        http://localhost:6543/files/pyramidmongoapp                 # filter with directory path '/pyramidmongoapp'
        http://localhost:6543/v1/files/pyramidmongoapp/myapp/static # api with versioning and filter  with directory path '/pyramidmongoapp/myapp/static'

      

## Creators

**Rajesh Mathew**

* <https://github.com/mathewraj>

