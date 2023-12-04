# This is a sample Python script.
# The purpose of this script is to demonstrate some key feature of what Python can do.
# Link for online testing - https://www.online-python.com/

"""
########################################################################################################
# Basic Print Statement
########################################################################################################
print("Hellow World")
"""

"""
########################################################################################################
# Basic Print Statement being call by a method
########################################################################################################
def print_hello_world():
    print("Hello World")


if __name__ == '__main__':
    print_hello_world()
"""


"""
########################################################################################################
# String Example
########################################################################################################
def string_example():
    name = "John Doe"
    school = "Mae Jemison High School"
    address = "5000 Pulaski Pike NW, Huntsville, AL 35810"
    print("My name is " + name + ". " + "I attend " + school + " Located at " + address)


if __name__ == '__main__':
    string_example()
"""

"""
########################################################################################################
# String Example - Pass full name
########################################################################################################
def string_example(name):
    school = "Mae Jemison High School"
    address = "5000 Pulaski Pike NW, Huntsville, AL 35810"
    print("My name is " + name + ". " + "I attend " + school + " Located at " + address)


if __name__ == '__main__':
    fullname = "John Doe" # Replace with your name
    string_example(fullname)
"""

"""
########################################################################################################
# String Example - Get input from the users.
########################################################################################################
def string_example(name):
    school = "Mae Jemison High School"
    address = "5000 Pulaski Pike NW, Huntsville, AL 35810"
    print("Your name is " + name + ". " + "You attend " + school + " Located at " + address)

def get_full_name():
    # Get full name from user
    user_full_name = input('Enter your full name and press the enter key: ')
    return user_full_name

if __name__ == '__main__':
    fullname = get_full_name()
    string_example(fullname)
"""

"""
########################################################################################################
# Variables with Logic Example - Get info from user and show how old they are
########################################################################################################
from datetime import datetime
from datetime import date
def get_data():
    fullname = input("What is your name?: ")
    date_of_birth = input("What is your date of birth? ex - 01-01-2022 (Month-Day-Year): ")
    display_age(date_of_birth)

def display_age(input_date):
    age = 0  #initialize varible
    format = "%m-%d-%Y"

    # Validate date from user
    # using try-except to check for truth value
    try:
        results = bool(datetime.strptime(input_date, format))
    except ValueError:
        results = False
    # Calculate Age

    if results:
        print("Valid Date")
        print("You entered: " + input_date)
        input_date_converted = datetime.strptime(input_date, format)
        current_date = datetime.now()
        print("Current Date: ", current_date)
        difference = current_date - input_date_converted
        print(difference)
        age = difference.days/365
        print("Your are " + str(age) + " year old")
    else:
        print("Invalid Date")

if __name__ == '__main__':
    get_data()
"""