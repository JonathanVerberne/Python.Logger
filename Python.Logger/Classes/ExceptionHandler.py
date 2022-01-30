from datetime import datetime
from Classes.MongoDb import MongoDb
from Classes.FileWriter import FileWriter

class ExceptionHandler(Exception):
    
    # constructor
    def __init__(self, error):
        self.error = error
        self.set_error_json()

    def __str__(self): 
        return "Error: %s" % self.error

    # sets json object variable to use in file and database logging
    def set_error_json(self):
        error_date =  str(datetime.now().isoformat())
        self.error_json = {
            "date" : error_date,
            "method" : "method",
            "type" : 2,
            "description" : self.error
        }

    # writes error to file and database
    def log_error(self):
        self.log_error_to_file()
        # move to after file write method
        # changes error_json and adds _id to the json string
        self.log_error_to_db()

    # write error to json file
    def log_error_to_file(self):
        FileWriter().log_error(self.error_json)

    # insert error to mongo db
    def log_error_to_db(self):
        db = MongoDb()
        db.log_error(self.error_json)