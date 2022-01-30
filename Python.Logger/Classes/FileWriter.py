from datetime import date
import json

class FileWriter:
    
    def log_error(self, json_object):
        
        file_date = date.today()
        file_name = "error_log_" + str(file_date) + ".json"
        
        with open(file_name, "a") as write_file:
            json.dump(json_object, write_file, indent=4)