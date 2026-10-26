# Starting file for PROJECT 1
# Include your course number, student first and last name, and date in the comment header
# Sergio Ortiz
# 10/25/26
# Project 01

# Section 1 Program Introduction

import random

print("7*******$*******7*******$*******7")
print("   Yezzur Kustom Kraps Tables")
print("7*******$*******7*******$*******7")

print("Winner winner chicken dinner!!!")
print("Need something to roll your dice on?!?!")
print()

# Section 2 Initial Customer Interaction

print("Check out our tables!")
print("Roll the dice. Must land 7 or 11 to proceed.")

roll = input("Press Enter to roll or enter 2,3, or 12 to opt out: ")

won = False

while roll != "2" and roll != "3" and roll != "12":
    dice = random.randint(1, 6) + random.randint(1, 6)
    print("You rolled:", dice)

    if dice == 7 or dice == 11:
        print("Winner! You can proceed to our products!")
        print()
        print("Welcome to our product selections!")
        print("7*******$*******7*******$*******7")
        
        won = True
        break

    else:
        print("Try again! You need a 7 or 11.")
        print()

        roll = input("Press Enter to roll again or enter 2, 3, or 12 to opt out: ")


# Section 3: Product Presentation
        

if won == True:
        print("Yezzur Kustom Kraps Table now available in different football team themes.")
        print("All tables are hand crafted from pure African Blackwood and line with 24K gold.")
        print("7*******$*******7*******$*******7")

#Section 4: Purchase Decision

        purchase = input("Interested is this fine piece of treasure, Captain? (yes/no): ")
        if purchase.lower() == "yes":

# Section 5 Customer Information

            print("SIGN YOUR LIFE AWAY!!!")
            print("7*******$*******7*******$*******7")
            print()

            first_name = input("Enter your first name: ")
            last_name = input( "Enter your last name: ")
            email = input("Enter your email address: ")
            phone = input("Enter your phone number: ")
            football_team = input("Enter your Football Team: ")
            print("7*******$*******7*******$*******7")
            print()


# Section 6: Purchase Calculations

            price = 77777 
            print("Each table is $77,777",)
            quantity = int(input("How many tables do you need? Limited tables made per year. "))

            subtotal = quantity * price
            tax_rate = 0.07
            sales_tax = round(subtotal * tax_rate, 2)
            total = subtotal + sales_tax
            print()

#Section 7: Customer Receipt

            print("7*******$*******7*******$*******7")
            print("         Purchase Receipt")
            print("7*******$*******7*******$*******7")
            print()

            print("Customer:", first_name, last_name)
            print("Email:", email)
            print("Phone:" , phone)
            print("7*******$*******7*******$*******7")
            print()

            print("Yezzur Kustom Kraps Tables (Desired Team)" )
            print("Desired Team:", football_team)
            print("Quantity:", quantity)
            print("Price per item: $", price)
            print("7*******$*******7*******$*******7")
            print()

            print(f"Subtotal: ${subtotal:,.2f}")
            print("Sales Tax (7%): $", sales_tax)
            print("Total Amount Due: $", total)
            print("7*******$*******7*******$*******7")
            print()

#Section 8 Closing Message

            print("Thank you for the gold, Captain!")
            print("Gamble responsibly and have fun!")
        else:
            print("What you broke bro!?!")
            print("Later!!!")

else:
    print("Happy Sailing!!!")
    print("YO HO HO AND A BOTTLE OF RUM!!!")



    

    
    

    
   



