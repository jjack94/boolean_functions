# james jack
# 3/5/21

# a function that takes two inputs from a user and prints whether
# the sum is greater than 10, less than 10, or equal to 10

def input_equal():  # create function
    x = int(input("What is the first number you would like to add?: "))  # first var/input
    y = int(input("What is the second number you would like to add?: "))  # first var / input
    ans = x + y  # creates the ans to be evaluated

    # compares answers to see if larger than or equal to 10
    if ans > 10:
        print("This sum is greater than 10")
    elif ans < 10:
        print("This sum is less than 10")
    elif ans == 10:
        print("This sum is equal to 10")
    else:
        print("this condition shouldn't have been executed")


input_equal()
