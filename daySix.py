# Day 6 Exercise
# Tyler Killgore
import random
"""
01. What will be the values following expressions? First write what
you think the answers are, then create code to check your work.
(3 >= 3) or (5 > 17)
(5 != 7) and not (2 < 1)
not (-2 < 3) or not (1 < 5)
"""
print("True, True, and False")
print("Answers are as calculated:")
print((3 >= 3) or (5 > 17))
print((5 != 7) and not (2 < 1))
print(not (-2 < 3) or not (1 < 5))

print("--"*10)

"""
02. Small improvement to "Can you vote?" (Question 4 in Day 5 exercise)
(You can reuse you code for that question)
One issue with the Day 5 "Can you vote?" is that, if a user's age is 17, it still prints "Please come back in 1 years".
This is grammatically wrong... Instead, the program should say "Please come back in 1 year" if the user only
need to wait for one more year.

Hint: you can to use nested if-else to check the number of years that this person needs to wait.

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
-----------Test case for new requirement-----------
what's your name?
Elsa [user's input]
How old are you, Elsa?
17 [user's input]
Please come back in 1 year
"""
voter_name = input("What's your name? ")
voter_age = input("How old are you, " + voter_name)


def legal_voting_age():
    if int(voter_age) >= 18:
        print("You can vote.")
    elif int(voter_age) < 18:
        years_left = 18 - int(voter_age)
        if int(voter_age) == 17:
            print("Please come back in 1 year.")
        else:
            print("Come back in {0} years." .format(years_left))

legal_voting_age()

print("--"*10)

"""
03. Combination of logic operators
Our department chair, Dr. Guinn, has two options to come to campus: riding bicycle or driving.
Every morning, his decision is made as follow:
1) if he feels tired, he will drive.
2) if he is not tired and he need to go shopping after work, he will drive.
3) if he is not tired and he does not need to go shopping, he will ride bicycle if it's not raining.
Please write your code below. You program should print wither "riding bicycle" or "driving". 
To test your code, try different combination of variables to make sure the logic is correct.

Some test cases to consider:
tired = True
shopping_after_work = False
raining = False             ----->driving

tired = False
shopping_after_work = True
raining = False             ----->driving

tired = False
shopping_after_work = False
raining = False             ----->riding bicycle

tired = False
shopping_after_work = False
raining = True              ----->driving
"""
tired = True
shopping_after_work = False
rainy = False


def drive_or_bike():
    if tired or shopping_after_work:
        decision = "drive"
    elif rainy:
        decision = "drive"
    else:
        decision = "bike"
    return decision

decision = drive_or_bike()

print("Dr. Guinn will {} to work.".format(decision))

print("--"*10)

"""
04. Simulation of rolling a die
Use the function in random module to simulate one roll of a standard die (6 faces for 1 to 6 points).
Based on the result of a roll, print "one", "two", "three", "four", "five" or "six".

Hint: using chained elif makes your code easier to read in this question
"""
roll = random.randint(1,6)

if roll == 1:
    print("one")
elif roll == 2:
    print("two")
elif roll == 3:
    print("three")
elif roll == 4:
    print("four")
elif roll == 5:
    print("five")
else:
    print("six")

print("--"*10)



