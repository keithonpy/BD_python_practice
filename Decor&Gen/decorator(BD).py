import time
import random



# log function as a decorator
def log_function(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__}: Input={args}, Output={result}, Execution Time={end_time - start_time} seconds")
        return result
    return wrapper


# data engineering procedure
@log_function
def data_engineering_process(data: str) -> str: 
    print("Return only one characters...")
    time.sleep(2)
    return data[random.randint(0, len(data)-1)]


if __name__ == "__main__":
    data = "sample"
    res = data_engineering_process(data)
    print(res)