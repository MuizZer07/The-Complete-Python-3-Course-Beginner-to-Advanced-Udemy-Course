

# Without Arguments:
def my_function():  # recommended style: snake case
    print("This is my function!")


my_function()  # This is my function


# With Arguments:
def my_function2(str1, str2):
    print(str1, str2)


my_function2("Argument 1", "Argument 2")  # Argument 1 Argument 2
my_function2("Hello", "World!")  # Hello World!


# Default Arguments
def print_something(name="Unknown", age="Unknown"):
    print("My name is ",  name,  " and my age is ", age)


print_something("Muiz", 23)  # My name is Muiz and my age is 23
print_something()  # My name is Unknown and my age is Unknown
print_something("Muiz")  # My Unknown is Unknown and my age is Unknown


# Keyword Arguments
print_something(age = 23)  # My name is  Unknown  and my age is  23
print_something(name="Muiz", age=23)  # My name is Muiz and my age is 23


# Infinite Arguments:
def print_people(*people):
    for person in people:
        print("This is " + person)


print_people("Muiz", "Sakib", "Fahad")
# This is Muiz
# This is Sakib
# This is Fahad


# Functions with return values:
def do_math(n1, n2):
    return n1 + n2


print(do_math(1,2))  # 3