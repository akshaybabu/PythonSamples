

def greet():
    print("Hello")
    print("Good Morning")

greet()

# adding parameters/arguments to the
# function can return something
# we can return multiple values
def add(a,b):
    c=a+b
    return c

def add_sub(x,y):
    c= x+y
    d=x-y
    return c,d

result1,result2=add_sub(5,4)

result =add(5,4)
print(result)
print(result1,result2)

