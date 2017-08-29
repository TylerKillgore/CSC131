# Day 4 Exercise
# Tyler Killgore

"""
01. Printing Strings
Use triple double quotes to print the content below (you should use only one print function):

I learned about things like...
triple quotes
and displaying text on multiple lines.
"""

print("--"*10)

"""
02. Printing Strings
Use single quotes to print the content below:

Single quotes protect "double quotes" in output.
"""

print('Single quotes protect "double quotes" in output.')
print("--"*10)

"""
03. Printing Strings
Use double quotes to print the content below:

Double quotes protect 'single quotes' in output.
"""
print("Double quotes protect 'single quotes' in output.")
print("--"*10)

"""
04. Printing with escape sequence
Use double quotes to print the content below:

A backslash protects "double quotes" in output.
"""
print("A backslash protects \"double quotes\" in output.")
print("--"*10)

"""
05. Printing with escape sequence
Use single quotes to print the content below:

A backslash protects 'single quotes' in output.
"""
print('A backslash protects \'single quotes\' in output.')
print("--"*10)

"""
06. Printing with escape sequence
Use single quotes to print the content below, use escape characters when necessary 
(you should use only one print function):

The backslash character \ is an escape character.
Use escape sequences to 
insert a linefeed.
"""
print("The backslash character \ is an escape character. \nUse escape sequences to \ninsert a linefeed.")
print("--"*10)

"""
07. Give me 3 different solutions!
Use single quotes, double quotes and triple double quotes to print the content below 3 times.

The shop owner said "No, no, 'e's uh,... he's resting" 
"""
print(""""No, no, 'e's uh,... he's resting" """)
print("--"*10)

"""
08. Formatting strings
The code below defines an integer bowling_score and a string name.
Use .format() to format a output string to print out "Ross's bowling score is 190".
Then use % to format another output string to print the same content.
"""

bowling_score = 190
name = "Ross"

print("{0}'s bowling score is {1}".format(name, bowling_score))
print("%s's bowling score is %d" % (name, bowling_score))
print("--"*10)
