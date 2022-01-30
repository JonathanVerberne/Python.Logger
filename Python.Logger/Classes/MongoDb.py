class MongoDb:
    
    def __init__(self):
        # Get the database
        self.get_database()
        
    # gets the mongo db name and sets the collection
    @classmethod
    def get_database(self):
        from pymongo import MongoClient
        #import pymongo

        # Provide the mongodb atlas url to connect python to mongodb using pymongo
        CONNECTION_STRING = "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/DemoDatabase"

        # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient        
        client = MongoClient(CONNECTION_STRING)
        
        # Create the database for our example (we will use the same database throughout the tutorial
        self.dbname = client['ErrorLogger']

        #set collection name
        self.collection_name = self.dbname["Logs"]

    # insert json object into mongo db
    def log_error(self, json_object):
        
        self.collection_name.insert_one(json_object)



