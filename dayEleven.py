# Day 11 Exercise
# Tyler Killgore
import random

def number_guessing_game(max):
    """
    01. A number guessing game with loop
    The input max is the max number possible.
    Finish this function which generates a random integer between 1 and max (both inclusive).
    The program ask user to guess the number,
    should tell players 1) if they guess correctly, 2) the correct answer is lower/higher.
    If input is 0, quit the game.
    This function has no explicit return value.

    Sample input/output for max = 18, with correct number (7) guessed:
    Please guess a number between 1 and 18
    10
    try smaller number
    5
    try larger number
    8
    try smaller number
    7

    Sample input/output for max =18, forced quit:
    Please guess a number between 1 and 18
    9
    try smaller number
    0
    existing this game

    Hint: use random.randomint(min,max) to create the random number.
    Hint: to test whether your program behaves correctly, you can print the random number when you are testing.
    """


def process_ip_address(ip_string):
    """
    02. Process ip addresses
    Create a program that takes an ip address as parameter is_string.
    Prints out the number of segments it contains, and the length of each segments.
    An IP address consists of 4 numbers, separated from each other with a full stop.
    But your program should just count however many are entered: your program should be robust! =)
    There is no explicit return value for this function.

    For ip_string "192.1.1.20", expected content below should be printed:

    Number 1 segment: 192, length is 3
    Number 2 segment: 1, length is 1
    Number 3 segment: 1, length is 1
    Number 4 segment: 20, length is 2
    Hint: you should still process the string character by character.
    Hint: you may want to use the variables created below. ;)
    """
    segment_counter = 1
    current_segment_length = 0

    for i in ip_string:
        if i != ".":
            current_segment_length += 1
        if i == ".":
            current_segment_length = 0
            segment_counter += 1
    print(segment_counter)
    
# test for Q1
number_guessing_game(10)

print("--"*10)

# test for Q2
process_ip_address("10.0.123456.255")
print("--"*10)
process_ip_address("172.16")
print("--"*10)
process_ip_address("225")
