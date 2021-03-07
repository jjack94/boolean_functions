# james jack
# 3/5/21

#  function that takes two inputs from a user and prints whether they are equal or not


def equal(): # creates function
    x = int(input("What is the first number you would like to use?: "))  # first var
    y = int(input("What is the second number you would like to use?: "))  # second var

    if x > y or y > x:  # if x is less than y or if y is greater than x allows a statement to be made to compare them
        print("These are not equal")
    else:
        print("These are equal")  # if the conditions above are not triggered the numbers must be equal value


equal()
