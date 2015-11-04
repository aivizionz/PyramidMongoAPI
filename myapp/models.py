import pymongo
# from bson.son import SON


# db_uri = "mongodb://localhost:27017"


class LoginModel(object):
    """ LoginModel Class
    """
    def __init__(self, request=None):
        # import pdb; pdb.set_trace()
        self.request = request
        # self.settings = request.registry.settings
        try:
            self.db = request.conn['sessiondb']
        # print "Connected successfully!!!"
        except pymongo.errors.ConnectionFailure, e:
            print "Could not connect to MongoDB: {0}".format(e)

    def verify_login(self, userid):
        """ This method will return the password for given userid
        """
        # import pdb; pdb.set_trace()
        sdata = self.db.session.find_one({"userid": userid})
        # try:
        #     # conn = pymongo.MongoClient(db_uri)
        #     # db = conn.sessiondb
        #     # sdata = db.session.find_one({"userid": userid})
        #     sdata = self.db.session.find_one({"userid": userid})
        #     # print "Connected successfully!!!"
        # except pymongo.errors.ConnectionFailure, e:
        #     return "Could not connect to MongoDB: {0}".format(e)
        if sdata:
            return str(sdata.get('password'))
        else:
            return None


class UserModel(object):
    """ UserModel Class
    """
    def __init__(self, request=None):
        self.request = request
        try:
            self.db = request.conn['usersdb']
            # print "Connected successfully!!!"
        except pymongo.errors.ConnectionFailure, e:
            print "Could not connect to MongoDB: {0}".format(e)

    def users_all(self):
        """ This method will use the mongodb find function and return all users
        """
        udata = list(self.db.users.find({}, {"_id": 0}))
        return udata

    def users_filterby(self, fkey, fvalue, request=None):
        """ This method will use the mongodb find function and return users by filter
        """
        udata = list(self.db.users.find({fkey: fvalue}, {"_id": 0}))
        return udata

    def users_flt_groupby(self, fkey, fvalue, groupby, request=None):
        """ This method will use the mongodb aggregate function and return user data by filter and groupby
        """
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
        udata = list(self.db.users.aggregate(pipeline))
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
