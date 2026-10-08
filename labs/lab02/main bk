# Starting file for LAB 2
# Include your course number, student first and last name, and date in the comment header
# CS 31 Sergio 0. 10/7/2026

# Print out title
print()
print("Better Get it Right or Else! Quiz")
print("\033[31mHAHAHAH\033[0m")
print(">:)")

print()
username = input("What is your name? ")
print(f"Hello, {username}!")

print()
start_quiz = input("Do you want to take me awesome quiz? Y/N ")
if start_quiz == "Y":
    print("Great! Lets get started!")
    counter = 0
    q1 = int(input("How would Python solve 5 * 5? "))
    if q1 == 25:
        counter += 1
        print("Yes! You are correct. Python would solve this as 25.")
    else:
        print("Sorry. That is not correct. ")

    print("What is the function that we use to output something to the terminal?")
    print("  A - output()")
    print("  B - print()")
    print("  C - format()")
    print("  D - None of the above")
    q2 = input("Your Answer - Choose A/B/C/D: ")
    if q2.upper() == "B":
        counter += 1
        print("Yes! You are correct. Python would use the print() function to output something to the terminal")
    else:
        print("Sorry. This is not correct.")



    print("* * * * YOUR FINAL SCORE * * * *")
    print(f"Your final score is: {counter} out of 5.")

    if counter == 5:
        print("You are a rockstar! You got them all correct1")
    elif counter >= 3 and counter < 5:
        print("Great work!")
    elif counter <3:
        print("You failed the Dark Lord! Get back in your cage!")

elif start_quiz == "N":
    print("Sorry. maybe next time!")

else:
    print("Sorry. That is an invalid response. Try again.")