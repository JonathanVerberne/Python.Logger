#x=10
#y=20
#ans=x*y
#print(ans)
#print("test")
#t=6
#t=8
#print(t)
#name=input("what's your name ? ")
#print("hello " + name)

#========================================================================================
#                           Error handling
#========================================================================================
## try catch example ##
#https://betterprogramming.pub/handling-errors-in-python-9f1b32952423
#try:
#    x = int(input("Please enter a number: "))
#    y = 100 / x
#except ValueError:
#    print("Error: there was an error")
#except ZeroDivisionError:
#    print("Error: 0 is an invalid number")
#except Exception:
#    print("Error: another error occurred")
#finally:
#    print("Cleanup can go here")


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