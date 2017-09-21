# Day 8 Exercise
# Tyler Killgore

def shout1():
    '''
    01. Function without parameter and return value.
    Complete the function below:
    In the function body, concatenate the string, 'congratulations' with another string, '!!!'. Assign the result to shout_word.
    Print the value of shout_word.
    There is no explicit return statement.
    '''
    shout_word = "congratulations" + "!!!"
    print(shout_word)

def shout2(word):
    '''
    02. Function with a parameter.
    Let try shot some different words! Complete the function below:
    Assign the result of concatenating word with '!!!' to shout_word.
    Print the value of shout_word.
    There is no explicit return statement.
    '''
    shout_word = word + "!!!"
    print(shout_word)


def shout3(word):
    '''
    03. Function with a parameter and a return value
    Copy your shout2 code below first.
    Replace the print() statement with the appropriate return statement.
    The caller of shout3 will print the return value of shout3
    '''
    shout_word = word + "!!!"
    return shout_word

def sea_hawk():

# 04. reusing code
# Finish this method which draws an Ascii art like below:

 print("""

                  _                    _
                 | |                  | |
 ___  ___  __ _  | |__   __ ___      _| | __
/ __|/ _ \/ _` | | '_ \ / _` \ \ /\ / / |/ /
\__ \  __/ (_| | | | | | (_| |\ V  V /|   <
|___/\___|\__,_| |_| |_|\__,_| \_/\_/ |_|\_\
    """)

def seconds_to_hours(seconds):
    '''
    05. finish this seconds_to_hours program.
    The input is seconds as an integer.
    Your program should calculate how many 'whole' hours and 'whole' minutes based on the number of seconds given.
    Then return a string formatted as "** hour(s) ** minute(s) and ** second(s)", use plural forms when necessary.
    For example, if the input is 3671, your return value should be: "1 hour 1 minute and 11 seconds"
    '''

    hour = seconds // 3600
    minute = (seconds // 60) % 60
    seconds = seconds % 60

# check to ensure no remainders
    if hour < 1:
        hour = 0
    if minute < 1:
        minute = 0
    if seconds < 1:
        seconds = 0

# concatenate values and string for output

    if hour > 1 or hour == 0:
        hour = "{} hours".format(int(hour))
    elif hour == 1:
        hour = "{} hour".format(int(hour))
    if minute > 1 or minute == 0:
        minute = "{} minutes".format(int(minute))
    elif minute == 1:
        minute = "{} minute".format(int(minute))
    if seconds > 1 or seconds == 0:
        seconds = "{} seconds".format(int(seconds))
    elif seconds == 1:
        seconds = "{} second".format(int(seconds))

    return hour, minute, seconds


# Q1
shout1()
shout1()
print("--"*10)

# Q2
shout2("Welcome")
shout2("I can code python now!")
print("--"*10)

# Q3
thanks = shout3("Gracias")
print(thanks)
yell = shout3("Congratulations")
print("Everyone shouted '{}!'".format(yell))
print("--"*10)

# Q4
sea_hawk()
print("I can call this function multiple times but only write it once!")
sea_hawk()
print("--"*20)

# Q5
print(seconds_to_hours(22222))  # 6 hours 10 minutes 22 seconds
print(seconds_to_hours(3599))  # 0 hour 59 minutes 59 seconds
print(seconds_to_hours(119))  # 0 hour 1 minute 59 seconds
print(seconds_to_hours(0))  # 0 hour 0 minute 0 second

