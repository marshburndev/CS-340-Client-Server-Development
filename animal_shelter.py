from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        self.client = MongoClient(
            'mongodb://%s:%s@localhost:27017/?authMechanism=DEFAULT&authSource=AAC' % (username, password))
        self.database = self.client['AAC']

    def create(self, data):  # Create
        if data is not None:
            # data should be dictionary
            inserted = self.database.animals.insert_one(data)
            if inserted is not None:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, query):  # Read
        if query is not None:
            # data should be dictionary
            result = self.database.animals.find(query, {"_id": False})
        else:
            result = self.database.animals.find({}, {'_id': False})
        return result

    def update(self, searched, changed):  # Update
        if searched is not None:
            # data should be dictionary
            changed_result = self.database.animals.update_many(
                searched, {"$set": changed})
            result = changed_result.raw_result
        else:
            raise Exception(
                "Nothing to update, because data parameter is empty")
        return result

    def delete(self, query):  # Delete
        if query is not None:
            # data should be dictionary
            delete_result = self.database.animals.delete_many(query)
            result = delete_result.raw_result
        else:
            raise Exception(
                "Nothing to delete, because data parameter is empty")
        return result
