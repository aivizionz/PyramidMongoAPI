import pymongo
# from bson.son import SON


db_uri = "mongodb://localhost:27017"


def verify_login(userid, request=None):
    """ This method will return the password for given userid"""
    try:
        conn = pymongo.MongoClient(db_uri)
        db = conn.sessiondb
        sdata = db.session.find_one({"userid": userid})
        # print "Connected successfully!!!"
    except pymongo.errors.ConnectionFailure, e:
        return "Could not connect to MongoDB: {0}".format(e)
    if sdata:
        return str(sdata.get('password'))
    else:
        return None


def users_all(request=None):
    """ This method will use the mongodb find function and return all users"""
    try:
        conn = pymongo.MongoClient(db_uri)
        db = conn.usersdb
        udata = list(db.users.find({}, {"_id": 0}))
        # print "Connected successfully!!!"
    except pymongo.errors.ConnectionFailure, e:
        print "Could not connect to MongoDB: {0}".format(e)
    return udata


def users_filterby(fkey, fvalue, request=None):
    """ This method will use the mongodb find function and return users by filter"""
    try:
        conn = pymongo.MongoClient(db_uri)
        db = conn.usersdb
        udata = list(db.users.find({fkey: fvalue}, {"_id": 0}))
        # print "Connected successfully!!!"
    except pymongo.errors.ConnectionFailure, e:
        print "Could not connect to MongoDB: {0}".format(e)
    return udata


def users_flt_groupby(fkey, fvalue, groupby, request=None):
    """ This method will use the mongodb aggregate function and return user data by filter and groupby"""
    if groupby == "profession":
        pipeline = [{"$match": {fkey: fvalue}},
                    {"$unwind": "$profession"},
                    {"$group": {"_id": "$profession", "count": {"$sum": 1}}}]
    elif groupby == "genre":
        pipeline = [{"$match": {fkey: fvalue}},
                    {"$unwind": "$genre"},
                    {"$group": {"_id": "$genre", "count": {"$sum": 1}}}]
    else:
        return "Not Implemented the  groupby : {0}".format(groupby)
    try:
        conn = pymongo.MongoClient(db_uri)
        db = conn.usersdb
        udata = list(db.users.aggregate(pipeline))
        # print "Connected successfully!!!"
    except pymongo.errors.ConnectionFailure, e:
        print "Could not connect to MongoDB: {0}".format(e)
    return udata


# print users_flt_groupby("city", "mumbai", "genre")
# print users_flt_groupby("city", "california", "profession")
# print users_flt_groupby("city", "cochin", "profession")
# print users_flt_groupby("city", "mumbai", "abc")

# print verify_login("test1")
# print verify_login("test4")
# print verify_login("test")

# print users_all()

# print users_filterby("city", "mumbai")
# print users_filterby("profession", "actor")
# print users_filterby("genre", "film")
# print users_filterby("lastname", "cruise")
# print users_filterby("firstname", "amitabh")
