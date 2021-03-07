# james jack
# 3/5/21

# a function that takes a year as a parameter and returns True if the year is a leap year, False if it is otherwise.


def leap_year(year):  # creates the func
    if year % 400 == 0:  # checks if divisible by 400 returning value of true
        return True
    if year % 100 == 0:  # checks if divisible by 100 returns value of false if it is
        return False
    if year % 4 == 0:  # checks if divisible by 4 and returns value of true if it is
        return True
    return False


# function returns false or true depending on whether or not all the conditions are met

print("Is the year leap?:", leap_year(2024))
