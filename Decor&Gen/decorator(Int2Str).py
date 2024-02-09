def makeResStr(func):
    def operate(*args, **kwargs):
        print("Let's make the result display as String data type")
        result = str(func(*args)) 
        
        return result
    return operate




@makeResStr
def inc(x):
    return x + 1

if __name__ == "__main__":
    arg = int(input("Enter a number: "))
    res = inc(arg)
    print(f"The result of {res}")
    print(f"Data type of the \"result\": {type(res)}")
