# Day 7 Exercise
# Tyler Killgore
import random

def coin_toss():
    """
    01: Fix the code below:
    The code below has several errors, try to uncomment and fix it and print the results of
    three tosses.
    Hint: the Pycharm can help you highlight the potential syntax errors, but may not be the
    exact places to change the code.
    """
    print("Uncomment the code below before fixing it:")
    if random.randint(0, 1):  # randint(0,1) returns either 0 or 1
        return 'Head'
    else:       # 0 is considered as false
        return 'Tails'


def dog_barking(breed, bark):
    """
    02. Optional arguments
    Finish this dog_barking function.
    This function expects two parameters: breed and bark, both as strings.
    This function does NOT have explicit return values.
    The default value for breed is "border collie", the default value for bark is "bark bark bark"
    The output should be "A chihuahua barks like 'bark bark bark bark bark bark bark'" if the function is called like:
    dog_barking("chihuahua","bark bark bark bark bark bark bark")
    """
    print("Add your solution here")
    if breed == None:
        breed = "border collie"
    if bark == None:
        bark = "bark bark bark"
    elif breed == "chihuahua":
        bark = "bark bark bark"
    return dog_barking(breed, bark)


def swap_value(a, b):
    """
    03. Swapping values: does this work for the know data types?
    Finish this swap_values function.
    This function takes two arguments and swap their values.
    The input value, a and b may have same or different data types, including int, float, string or bool.
    This function does not have explicit return values.
    Hint: you may need a third variable to help you when swapping the values.
    """
    print("Add your solution here")

def even_or_odd(x):
    """
    04. if-else inside a function.
    Finish this even_or_odd function which takes an integer x and return a string saying whether it's even or odd.
    In addition to the information of even and odd, if this number is divisible by 3 (if x is odd)
    or 4 (if x is even), the output from this function should also print this information.
    The argument x should be an integer.
    This function return strings.
    Please find the sample input/return values from the comments of the callers below.
    """
    print("Add your solution here")


# tests for Q1
print(coin_toss())
print(coin_toss())
print(coin_toss())
print("--"*20)

# tests for Q2
dog_barking()           # should use the default argument values
dog_barking("greyhound", "I am shy.. I don't bark")
dog_barking("chihuahua")        # should use default argument value for bark
print("--"*20)

# tests for Q3
bool_a = True
bool_b = False
swap_value(bool_a,bool_b)
print("After calling swap_value function, bool_a is {}, bool_b is {}".format(bool_a,bool_b))

int_a = 2017
float_a = 10.50
swap_value(int_a, float_a)
print("After calling swap_value function, int_a is {}, float_a is {}".format(int_a,float_a))

string_a = "hello world"
swap_value(string_a, float_a)
print("After calling swap_value function, string_a is {}, float_a is {}".format(string_a,float_a))
print("--"*20)

# tests for Q4
print(even_or_odd(19))     # expected output: 19 is an odd number
print(even_or_odd(15))     # expected output: 15 is an odd number, it is divisible by 3
print(even_or_odd(12))     # expected output: 12 is an even number
print(even_or_odd(16))     # expected output: 16 is an odd number, it is divisible by 4


