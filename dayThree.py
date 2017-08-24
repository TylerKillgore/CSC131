# Day 3 Exercise
# ADD YOUR NAME HERE
"""
0. an integer divides another integer.
Run the code below, if it is an integer division, the result should be 3; or
if it is a float division, the result should be 3.5.
WHAT DID YOU GET? (use print function to answer)
WHY? (use print function to answer)
"""
print(7/2)
print("The answer given after running the 7/2 was a float number." 
      "\n Python is a dynamic language and when possible will use the most precise data type to complete a function.")
"""
1. Indentation.
The code below is not indented correctly. Try to run it.
print(5/2)
 print(5+2)
WHAT ERROR MESSAGE DID YOU GET? (use print function to answer)
FIX THE CODE.
"""
print(5/2)
print(5+2)
print("The error message given was IndentationError: unexpected indent. Fixed code by removing indent in second math problem.")

print("--"*10)

"""
2. Comment your code.
Write a program which asks "What's your name?" and gets user's input.
The users input should be stored as a string with variable name "user_input"
Then print "Hola ****" in which "****" should be the name input by the user.
HINT: try print("Hola " + user_input)
USE # TO COMMENT EACH LINE OF YOUR CODE TO EXPLAIN THIS WORK PROCESS.
"""
#Receive user's name and assign to user_input
user_input = input("What's your name?")
#return the string Hola followed by the value of user_input which should be user's name
print("Hola " + user_input)
print("--"*10)

"""
3. Calculations
Do the calculation below with a pen, remember to handle the operators in the correct order:
3 * 2 ** 5 / 10
9 // 10 + - 11 // 10
9 % 10 + - 11 % 10
THEN PRINT THE RESULTS OUT AND CHECK YOUR ANSWERS.
"""
print(3 * 2 ** 5 / 10)
print(9 // 10 + - 11 // 10)
print(9 % 10 + - 11 % 10)

print("--"*10)

"""
4. More calculations
CHANGE THE CODE BELOW INTO SHORTER FORMS WITH "+=", "-=" ETC.
Make sure your code still produce the same result.
"""
y = 100
y += 1
y -= 10
x = y // 5
x **= 2
y %= 3
print(x, y)   # should print "324 1"
print("--"*10)

"""
5. Comparison results
Try to figure out the result (True or False) of the code below:
EXPLAIN THE SEQUENCE OF THE OPERATORS PROCESSED? (Answer using print function)
"""
print(5 / 2 == 5//2 + 5 % 2 / 2)
print("The answer given is 'True' due to the division and remainder problems holding precedent. "
      "\nWhich results in the addition of .5 and 2 which is equal to the answer of 5/2.")
print("--"*10)

"""
6. More calculations
What are the results of the following expressions? First write down what
you think the answers are, then create code to check your work.
7%3
7//3
7%-2
7//-2
-15//6
"""
print(7%3)
print(7//3)
print(7%-2)
print(7//-2)
print(-15//6)

print("--"*10)
