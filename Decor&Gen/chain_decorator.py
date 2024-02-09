def bold_decorator(func):
    def wrapper(*args, **kwargs):
        return "<b>" + func(*args, **kwargs) + "</b>"
    return wrapper

def italic_decorator(func):
    def wrapper(*args, **kwargs):
        return "<i>" + func(*args, **kwargs) + "</i>"
    return wrapper

@bold_decorator
@italic_decorator
def greet(name):
    return f"Hello, {name}!"

print(greet("Keith"))