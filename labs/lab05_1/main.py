# Starting file for LAB 5-1
# Include your course number, student first and last name, and date in the comment header
# Module file for Lab 5 - nameformat.py

def hello_world():
    print("Greetings Earthling!")

def sayHello(firstName):
    """Definition: A simple function that takes a firstName input and says hello to that name"""
    print(f"Hello there {firstName}. Mighty fine day we're have!")
    print()

def fullName(firstName, lastName):
    """Definition: A simple function that takes firstName and lastName input and outputs the first and last name."""
    print(f"{firstName} {lastName}")
    print()

def lastNameFirst(firstName, lastName):
    """Definition: A simple function that takes firstName and lastName input and outputs the last and first name with a comma."""
    print(f"{lastName}, {firstName}")
    print()
