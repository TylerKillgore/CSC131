# Day 12 Exercise
# Tyler Killgore
import random

def die_rolling_cheater(n):
    """
    01. Skip the current round if you do not get 6 ;-)
    Finish this function which simulates a cheater in die rolling: this cheater will roll a die again if (s)he does not
    get a six. The aim of the cheater is to roll n numbers of 6 in a row, (but with cheating).
    The parameter n is the number of 6 that this cheater is going to roll "consecutively".
    There is no explicit return value in this function.
    For example, if the function is called with die_rolling_cheater(4), the expected output should be:

    Roll number 1, I get 6.
    Roll number 2, I get 6.
    Roll number 3, I get 6.
    Roll number 4, I get 6.

    Hint: use randint to create random integers.
    Hint: if the cheater does not get a 6, you can simply use "continue" to re-roll the die.
    """
    i = 0
    while i < n:
        rolled_die_number = random.randint(1, 6)
        if rolled_die_number != 6: continue
        else:
            i =+ 1
            print("Roll number {0} , I get {1}" .format(i, rolled_die_number))
    print("")
def probability_of_honest_man(n):
    """
    02. Estimate the probability of rolling n 6 in a row (for an honest man).
    Finish this function to simulate the probability of rolling n 6 with one die in a row, for a non-cheater.
    You are required to SIMULATE, instead of calculate the possibility mathematically.
    For example, if the function is called with probability_of_honest_man(2), what you can do is to do
    100,000 simulations: in each simulation, you simulate 2 rolls and see whether you get two 6.
    The returned number is the probability based on your simulation, namely:
    (# of simulations that you get n 6 consecutively)/(# of simulations in total)

    Hint: your function is called with probability_of_honest_man(2), the return number should be very closed to 0.0278
    """

def print_num_digits_and_letters(str):
    """
    03. Count the numbers, letters and other characters in a string.
    Finish this function which counts the number of 1) numbers, 2) English letters and 3) other characters (as the
    3rd category) in a given string str as parameter.
    This function does not have an explicit return value.
    You should use "continue" at least once in the char-by-char processing.

    For example, if this function is called with print_num_digits_and_letters("Python rocks")
    The output produced by this function should be:

    There are 0 number, 11 letters and 1 special character in this string.
    """

#------------------------The code below is for testing purpose---------------------

# Q1
die_rolling_cheater(3)
die_rolling_cheater(10)
print("-------------")

# Q2
print(probability_of_honest_man(2))
print(probability_of_honest_man(10))
print("-------------")

# Q3
print_num_digits_and_letters("Walden is a book by noted transcendentalist Henry David Thoreau. ")
print_num_digits_and_letters("""
Walden Pond is a lake in Concord, Massachusetts in the United States. A famous example of a kettle hole, it was formed by retreating glaciers 10,000–12,000 years ago.
""")



