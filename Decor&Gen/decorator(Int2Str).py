## Nest fucntion
def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
result = add_five(6)
print(result)


# Decorator
def makeResStr(func):
    def operate(*args, **kwargs):
        print("Let's make the result display as String data type")
        result = str(func(*args)) 
        
        return result
    return operate

@makeResStr
def inc(x):
    return x + 1

arg = int(input("Enter a number: "))
res = inc(arg)
print(f"The result of {res}")
print(f"Data type of the \"result\": {type(res)}")
