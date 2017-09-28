# Day 10 Exercise
# Tyler Killgore

def draw_an_isosceles_trangle_of_plus(n):
    """
    01: Draw a triangle of +
    Input n is a integer.
    Finish this function which creates an isosceles triangle of plus.
        For example, if this function is called like draw_a_trangle_of_plus(4),
        Your code should print 3 lines of "+++++" on the console (ignore the indentations):
           +
          +++
         +++++
        +++++++
    There is no explicit return value for this function
    """
    count = 0
    while count <= n:
        print("+" * count, end="")
        count += 1
        print()

def count_upper_letters(str):
    """
    02: Count upper letters in a string
    Input str is a string.
    Finish this function which counts the number of upper letters in this string. You should do this with a while loop.
    This function returns the number of upper letters in the string as an integer.
    Be careful: make sure your code works for empty strings and strings do not have any upper letters.
    """
    count = 0
    upper_case_letters = 0

    for i in str:
        if i.isupper():
            upper_case_letters += 1
        count += 1
    print(upper_case_letters)


def you_are_taking_csc131():
    """
    03: Keep asking untill you say "CSC131"
    This function has no input parameter.
    Finish this function which keeps on asking the user "what course are you taking this semester" and
    wait for user's input. If the user's input does not contain "csc 131" or "csc131", or upper cases
    of the same strings, ask the user again.
    Otherwise, output "csc131, I knew it!" and quit the loop.
    This function has no explicit return value.

    Hint: you can use "in" to test whether a string contains a substring.
    Hint: make use of the variable defined below. =)
    """
    input_has_131 = False

    while input_has_131 == False:
        course_name = input("What course are you taking semester? ")

        if ("csc" or "CSC" and "131") in course_name:
                input_has_131 = True

        else:
                print()
    print("I knew it!")

def string_of_vowels(str):
    """
    04: Return a string of all the vowels in a string.
    Input str is a String.
    Your function should return a string of vowels in this string, in the sequence they appear, including the duplicates.
    For example, if the input parameter is "Casablanca", the return value should be "aaaa".
    Be careful: you should count the vowels a, e, i, o, u and their upper letters
    """

    count = 0

    for i in str:
        if i.islower():
            if i in "aeiou":
                print(i, end="")

        elif i.isupper():
            if i in "AEIOU":
                print(i, end="")
    print()



# test for Q1
draw_an_isosceles_trangle_of_plus(10)
draw_an_isosceles_trangle_of_plus(1)
draw_an_isosceles_trangle_of_plus(0)

print("--"*10)

# test for Q2
print(count_upper_letters('''
Casablanca is a 1942 American romantic drama film directed by Michael Curtiz and based on Murray Burnett and 
Joan Alison's unproduced stage play Everybody Comes to Rick's. 
'''))
print(count_upper_letters(""))

print("--"*10)

# test for Q3
you_are_taking_csc131()

print("--"*10)

# test for Q4
print(string_of_vowels('Casablanca'))
print(string_of_vowels('''
Casablanca is a 1942 American romantic drama film directed by Michael Curtiz and based on Murray Burnett and 
Joan Alison's unproduced stage play Everybody Comes to Rick's. 
'''))


