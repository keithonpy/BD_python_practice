def snack_generator(snack_list):
    yield snack_list

# Using the generator
if __name__ == "__main__":
    machine = snack_generator(["Chips", "Cookies", "Chocolate"])
    input("Press Enter to insert coins")
    print(next(machine))  # Output: Chips
    input("Press Enter to insert coins")
    print(next(machine))  # Output: Chocolate
    input("Press Enter to insert coins")
    print(next(machine))  # Output: Cookies