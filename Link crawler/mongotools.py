import pymongo
from coloredprint import printc

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
class create_mongodb_connection:

    def __init__(self, __mongo_host, __mongo_database_name, __mongo_collection_name):
        __mongo = mongo_engine.int_client(__mongo_host)
        __database = mongo_engine.int_database(__mongo, __mongo_database_name)
        __collection = mongo_engine.int_collection(__database, __mongo_collection_name)
        self.collection = __collection
        self.mongoclient = __mongo

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

    def alllist_dictlist(self,__query):
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

    def show_content(self):
        printc.warning("Rendering list...")
        __list = self.collection.find()
        for __x in __list:
            print(__x)
        printc.success("Done!")

    def show_collection_size(self):
        return self.collection.count()

    def getObjectID_of_dictlist(self, __dictlist):
        return __dictlist.get("_id")

    def delete_dictlist_by_ObjectID(self, __objectId):
        try:
            __query = {"_id":__objectId}
            self.collection.delete_one(__query)
            print("dict list deleted!")
        except:
            printc.failed("object id not exist")
            pass

class userlist:
    def create_list(db_domain, db_url, db_starting_time, db_response_time, db_mime_type, db_html_status_code):
        __database_query = {"domain": db_domain, "URL": db_url, "starting time": db_starting_time,
                            "response time": db_response_time, "MIME type": db_mime_type,
                            "HTTP status code": db_html_status_code}
        return __database_query


#wc = create_mongodb_connection("mongodb://localhost:27017/", "kay's_database", "web_data")

# db_domain = ""
# db_url = ""
# db_st = ""
# db_rt = ""
# db_mt = ""
# db_hsc = ""

# __udata = userlist.create_list(db_domain, db_url, db_st, db_rt, db_mt, db_hsc)
# wc.add_one_dictlist(__udata)
# wc.delete_collection()
# wc.show_content()





