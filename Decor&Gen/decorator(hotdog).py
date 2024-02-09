def add_bread(func):
    def wrapper(*args, **kwargs):
        print("Preparing the bread...")
        hotdog = func(*args, **kwargs)
        print("Adding sauce...")

        return hotdog
    return wrapper

@add_bread
def make_hotdog(ingredients):
    return f"A hotdog with {' and '.join(ingredients)}"

hotdog = make_hotdog(["sausage", "onions", "cheese"])
print(hotdog)