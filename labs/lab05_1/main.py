# Starting file for LAB 5-1
# Include your course number, student first and last name, and date in the comment header
# Starting file for LAB 5-1
# Include your course number, student first and last name, and date in the comment header
# Sergio Ortiz CS31 October 28, 2026

import nameformat

nameformat.hello_world()

def main():
    # program title
    print("Welcome to the Name Format Module program")
    print()

    # ask for first/last name
    firstName = input("What is your first name?")
    lastName = input("What is your last name?")

    # menu system
    while True:
        print("* * Menu * *")
        print("1 - Say Hello")
        print("2 - Output Full Name")
        print("3 - Output Last Name, First Name")
        print("4 - Read Module Documentation")
        print("5 - Exit Program")
        menuChoice = input("What would you like to do?")

        # if else block based on the choice input
        if menuChoice == "1":
            # call sayHello
            nameformat.sayHello(firstName)
        elif menuChoice == "2":
            # call fullName
            nameformat.fullName(firstName, lastName)
        elif menuChoice == "3":
            # call lastNameFirst
            nameformat.lastNameFirst(firstName, lastName)
        elif menuChoice == "4":
            print("Documentation Placeholder")
            help(nameformat.sayHello)
            help(nameformat.fullName)
            help(nameformat.lastNameFirst)
        elif menuChoice == "5":
            print("Thank you for using our program")
            break

        else:
            print("Sorry, invalid input. Please try again.")

if __name__ == "__main__":
    main()
