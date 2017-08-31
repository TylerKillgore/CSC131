# Day 5 Exercise
# Tyler Killgore

"""
01 Even or odd?
Write a program, which asks user "Give me an integer", then take users' input.
Then the program should print "Even" or "Odd" based on the input.
"""

answer = input("Give me an integer: ")
answer = int(answer)

if(answer%2 == 0):
        print("Even")
else:
        print("Odd")
print("--"*10)

"""
02. Course levels
Write a program which ask user to input a course number such as "CSC131"
Your program should print "freshman course", "sophomore course", "junior course" and "senior course" 
based on the course number
You can assume that 100 level courses are freshman courses, 200 level courses are sophomore courses, etc.
You can assume that the input is always a string of 3 letters followed by 3 digits.
If the input is a course number beyond [100, 499], your program should print "I don't know this course".
Hint: the key is to access a specific character with a correct index. You don't need to use chained or nested if-else.
"""

print("--"*10)

"""
03. Boolean operators
The code below uses two different ways to test if the value of variable b is between the value of a and c.
Try to test different values of a, b and c.
ARE THOSE TWO APPROACHES EQUIVALENT? (answer with print function)
"""
a = 10
b = 11
c = 20
# approach 1
if b >= a and b <= c:
	print("in approach 1: b is between a and c")
# approach 2
if not (b < a or b > c):
	print("in approach 2: b is between a and c")

print("--"*10)

"""
04. Can you vote?
Write a program which asks user "what's your name?".
Based on the user's input, the program should ask "How old are you, ***?" in which *** is the user's name.
Then print "You can vote" or "Please come back in XX years" based on user's age 
(XX is the number of years that user need to wait before getting 18 years old).

The process of your program should be: 
-----------First test case-----------
what's your name?
harley quinn [user's input]
How old are you, harley quinn?
20 [user's input]
You can vote
-----------Another test case-----------
what's your name?
Anna [user's input]
How old are you, Anna?
16 [user's input]
Please come back in 2 years
 """

print("--"*10)


