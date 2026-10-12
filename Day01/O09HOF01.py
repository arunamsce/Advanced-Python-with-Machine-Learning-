
def sum(x, y):
    return x + y

def diff(x, y):
    return x - y


def log_details(fnc):
    logInfo = "Logging into done....."

    def innerFun(*args):
        print(logInfo)
        print(fnc(*args))
        print("-" * 60)

    return innerFun

sumlogger = log_details(sum)
difflogger = log_details(diff)

sumlogger(10, 20)
difflogger(30, 12)




# Key Concepts
# Higher-Order Function: A function that takes other functions as arguments or returns functions
# Function Wrapping: Adding behavior around an existing function without modifying it
# *args: Allows the wrapper to accept any number of arguments and pass them to the original function
# Decorator Pattern: This is the foundation of Python decorators - the @decorator syntax is syntactic sugar for this pattern


