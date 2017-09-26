# Day 9 Exercise
# Tyler Killgore


def draw_a_line_of_plus(length):
    """
    01: Draw a line of +
    Input length is a integer.
    Finish this function which draws given number of "+"
        For example, if this function is called like draw_a_line_of_plus(3),
        Your code should print "+++" on the console.
    There is no explicit return value for this function
    """
    # print("+" * length)

    for i in range(length):
        print("+", end="")
    print()


def draw_a_square_of_plus(n):
    """
    02: Draw a square of +
    Input n is a integer.
    Finish this function which draws n lines of "+", each line should contain n "+".
        For example, if this function is called like draw_a_square_of_plus(3),
        Your code should print 3 lines of "+++" on the console (ignore the indentations):
        +++
        +++
        +++
    There is no explicit return value for this function
    """
    for i in range(n):
        for j in range(n):
            print("+", end="")
        print()

def draw_a_rectangle_of_plus(xlength, ylength):
    """
    03: Draw a rectangle of +
    Input xlength and ylength are integers.
    Finish this function which draws ylength lines of "+", each line should contain xlength "+".
        For example, if this function is called like draw_a_rectangle_of_plus(3,5),
        Your code should print 3 lines of "+++++" on the console (ignore the indentations):
        +++++
        +++++
        +++++
    There is no explicit return value for this function
    """
    for i in range(xlength):
        for j in range(ylength):
            print("+", end="")
        print()

def draw_a_trangle_of_plus(n):
    """
    04: Draw a triangle of +
    Input n is a integer.
    Finish this function which draws a right triangle of "+"
        For example, if this function is called like draw_a_trangle_of_plus(4),
        Your code should print 3 lines of "+++++" on the console (ignore the indentations):
        +
        ++
        +++
        ++++
    There is no explicit return value for this function
    """
    for i in range(n):
        print(i * "+")


def count_i_j_in_string(str):
    """
    05. Count the occurrences of letter "i" and "j" in a string.
    Input str is a string.
    Finish this function which loop all the characters and count the occurrences of letter "i" and "j".
    (You do not need to count the upper cases)
    The return value should be the occurrences as an integer.
    """

    if len(str) == 0:
        print("0")
    else:
        sentence = str
        number = sentence.count("i") + sentence.count("j")
        print(number)


# ------------The code below is for testing purpose----------------------

# tests for Q1
draw_a_line_of_plus(9)
draw_a_line_of_plus(29)
draw_a_line_of_plus(0)
print("--"*20)

# tests for Q2
draw_a_square_of_plus(5)
draw_a_square_of_plus(9)
draw_a_square_of_plus(1)
draw_a_square_of_plus(0)
print("--"*20)

# tests for Q3
draw_a_rectangle_of_plus(4,8)
draw_a_rectangle_of_plus(1,2)

# tests for Q4
draw_a_trangle_of_plus(9)
draw_a_trangle_of_plus(1)

# tests for Q5
print(count_i_j_in_string("python"))
print(count_i_j_in_string('''
A Right Triangle's Hypotenuse. The hypotenuse is the largest side in a right triangle and is always opposite the right angle.
'''))

