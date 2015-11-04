import pymongo
# from bson.son import SON


class LoginModel(object):
    """ LoginModel Class
    """
    def __init__(self, request=None):
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
        sdata = self.db.session.find_one({"userid": userid})
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
