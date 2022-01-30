#===========================================================================
                        ### TO DO ###
#===========================================================================
#1. add database credentials to a config/ini file
#2. add readme file
#3. get mongo db id and add to file json (so json obkects are the same)
#4. add error handling to exception handler and validation i.e. check if json object is not null etc,,

from Classes.ExceptionHandler import ExceptionHandler

try:
    a=1
    b=0
    c=a/b
    print("the value of c = " + str(c))
except Exception as e:
    print(repr(e))
    ExceptionHandler(repr(e)).log_error()
finally:
    print("exiting program...")