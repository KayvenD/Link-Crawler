import pymongo
from coloredprint import cprint

mongo_host = "mongodb://localhost:27017/"
database_name = "kay's_database"
collection_name = "web_data"



class create_connection:
    def __init__(self):
        self.mongo_collection()

class mongo_engine:
    def int_client(__host):
        __my_client = pymongo.MongoClient(__host)
        return __my_client

    def int_database(__client_handle,__database_name):
        __my_db = __client_handle[__database_name]
        return __my_db

    def int_collection(__database_handle, __collection_name):
        __my_collection = __database_handle[__collection_name]
        return __my_collection

class mongo_collection:

    def __init__(self,mongo_hos):
        mongo = mongo_engine.int_client(mongo_host)
        database = mongo_engine.int_database(mongo, database_name)
        collection = mongo_engine.int_collection(database, collection_name)
        self.collection = collection

    def add_key_and_value(self,__one_key, __one_value):
        __dict = {__one_key:__one_value}
        return self.collection.insert_one(__dict)

    def add_one_dict_in_one_list(self,__one_key, __one_value):
        __dict = {__one_key:__one_value}
        return self.collection.insert_one(__dict)

    def add_one_dictlist(self,__dictslist):
        self.collection.insert_one(__dictslist)

    def add_many_dictlist(self,__dictslists):
        self.collection.insert_many(__dictslists)

    def getlist_with_key(self,__key):
        return self.collection.find().sort(__key)

    def getvalue_in_dictlist(self, __dictlist, __key):
        return __dictlist.get(__key)

    def get_one_dictlist_in_list_of_dictlist(self, __list_dictlist, __index):
        return __list_dictlist[__index]

    def findlist_dictlist(self,__query):
        __list = self.collection.find(__query)
        __item = []
        for __x in __list:
            __item.append(__x)
        return __item

    def delete_key_and_value(self,__key,__value):
        __query = {__key:__value}
        return self.collection.delete_one(__query)

    def delete_dictlist(self, __query):
        return self.collection.delete_one(__query)

    def delete_collection(self):
        return self.collection.drop()

    def update_dict(self,__referencevalues,__newvalues):
        self.collection.update_one(__referencevalues,__newvalues)


    ##def update_one(self,__old_dict, __new_dict):






