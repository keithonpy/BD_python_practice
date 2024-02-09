'''
Generators can be created using generator functions or generator expressions.
'''


# Generator function
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()


# Iterating with Generators
# Iterating over values using a for loop
for value in gen:
    print(value)

# Manually calling next() function
gen = my_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3

##############################################
# Generator expression
gen_expr = (x for x in range(1, 4))

for value in gen_expr:
    print(value)

# Manually calling next() function

print(next(gen_expr))  # Output: 1
print(next(gen_expr))  # Output: 2
print(next(gen_expr))  # Output: 3
