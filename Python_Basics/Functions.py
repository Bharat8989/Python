""" functions in Python 
    functions manage ek code block jo specific task kar karto and garj padlyas punha use karay yeto 
    def = function define karto 
 """
def hello():
    print("welcome ")
hello()

#functions with parameters 
# parameters mhanje functions la dilelya value
def greet(name):
    print(f"Hello {name}")
greet("bharat")

#multiple parameters 
def add(a,b):
    return a+b
print(add(23,21))

#Default Parameters 

def default(b,a=1):
    print(a+b)
default(23)

#Types of Functions 
# 1 no parameter  , no return 
def show():
    print("hello")
# show()
#2 parameter ,no return
def greet1(name):
    print(name)
# greet1()
#3 parameter return
def add1(a,b):
    return a+b
# add1()
#4 no parameter ,return
def get_name():
    return "Bharat"

