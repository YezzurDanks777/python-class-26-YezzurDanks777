# Starting file for PROJECT 2
# Include your course number, student first and last name, and date in the comment header
#Sergio Ortiz CS31
# 11/8/2026

def get_word(prompt):
    answer = input(prompt).strip()

    while answer == "":
        print("Dont leave anything blank por favor!!!")
        answer = input(prompt).strip()

    return answer


def get_number(prompt):
    while True:
        answer = input(prompt).strip()

        if answer == "":
            print("Enter a number for the love of god!!!")
        else:
            try:
                number = float(answer)

                if number >= 0:
                    return number
                else:
                    print("Zero or higher you nut.")

            except ValueError:
                print("That aint gonna work")


def play_game():

    story_count = 0

    print("🔧" * 33)
    print("    The Adventures of a Yezzur Mechanic!")
    print("🔧" * 33)
    print(" Welcome to thee adventures of a Yezzur Mechanic")
    print(" Where the roads go, no one knows!!!")
    print()

    play = input("Are you up for a wacky tacky adventure with a Yezzur Mechanic? (y/n): ").lower().strip()

    while play != "y" and play != "n":
        print("Your not making sense. Its a y or n type of question.")
        play = input("Are you up for a wacky tacky adventure with a Yezzur Mechanic? (y/n): ").lower().strip()

    if play == "n":
        print("Come back when your not all nutty and bolty!")
        return

    player_name = get_word("So, what they call ya?")

    print()
    print("Ready for a greasy adventure, " + player_name + "!")
    print("Get your lube and fluids ready because its time for a flush.")
    print()

    while play == "y":
        print("🔧" * 33)
        print("Which road do you want to take heaven or hell?")
        print("🔧" * 33)
        print("Heaven. The Two Apprentices")
        print("Hell. The Two 3rd degrees")
        print()

        choice = input("Which road you gonna take? (heaven/hell): ").lower().strip()

        while choice != "heaven" and choice != "hell":
            print("Choose only heaven or hell mwwhahaha!!")
            choice = input("Which road you gonna take? (heaven/hell): ").lower().strip()

        print()
        print("Alright im going to need some extremely personal and sensitive information.")
        print("MMMMWWHAHAHA")
        print()

        if choice == "heaven":

            print("The Two Apprentices")
            print()

            name = get_word("Enter man's name")
            adjective = get_word("Enter an adjective")
            body_part = get_word("Enter body part")
            tool = get_word("Enter Tool")
            verb = get_word("Enter Verb")
            insult = get_word("Enter Insult")
            type_food = get_word("Enter type of food")

            print()
            print("🔧" * 33)
            print(player_name.upper() + " 'S Yezzur Heaven Adventure")
            print("🔧" * 33)

            print()
            print("It was 8:00 AM at Big Dick's Auto Repair, where two mechanics, "
                  + name + " and his coworker were already arguing over who had "
                  "to work on a customer's car.")

            print("Listen, you " + adjective + " son of a bitch!" +
                  " said " + name + ", I've been working on engines for 20 years. I know exactly what I'm doing.")

            print("His coworker looked at him and said, "
                  "The only thing you've been doing for 20 years is confusing a dipstick with your " + body_part + ".")

            print("Shut your mouth! Hand me the " + tool + "!")

            print("Excuse me, gentlemen. My car is making a strange noise whenever I accelerate. "
                  "The second mechanic looked at the first and whispered, "
                  "\"Sounds like she's got a loose connection.\" "
                  "\"Well, get underneath it and see what's wrong,\" replied " + name + ".")

            print("The mechanic crawled under the vehicle and started " + verb +
                  " like he was trying to win a wrestling championship. "
                  "Suddenly, there was a loud bang. "
                  "\"WHAT THE HELL WAS THAT?\" screamed the customer.")

            print("Nothing, ma'am! shouted the mechanic. Just a little adjustment! "
                  "He crawled out from underneath the car covered in grease. "
                  "The first mechanic looked at him and said, "
                  "\"You look like a " + insult + " that got thrown out of a dumpster.\" "
                  "\"At least I know how to fix a car,\" he replied. "
                  "\"You couldn't fix a sandwich without calling technical support.\" "
                  "The customer shook her head. "
                  "\"Are you two seriously certified mechanics?\" "
                  "\"Absolutely,\" said " + name + ". We're ASE certified.")

            print("What's that? "
                  "Absolutely Shitty Employees. "
                  "At that moment, the second mechanic pulled out his lunch. "
                  "\"What are you eating?\" asked " + name + ". "
                  "\"" + type_food + ".\" "
                  "\"Jesus Christ. That's disgusting.\" "
                  "\"Coming from a man who drank transmission fluid because he thought it was an energy drink?\" "
                  "They both went silent. "
                  "Then the customer slowly backed toward the exit. "
                  "\"Actually, forget about fixing my car. I'll take my chances with public transportation.\" "
                  "And just like that, another customer drove away from Big Dick's Auto Repair. "
                  "Their official shop motto? "
                  "WE SCREW BOLTS, NOT CUSTOMERS.")

        elif choice == "hell":

            print("The Two 3rd Degrees")
            print()

            adjective = get_word("Enter Adjective")
            noun = get_word("Enter Noun")
            adjective2 = get_word("Enter Adjective")
            type_drug = get_word("Enter a Drug")
            verb_ing = get_word("Enter a verb ending in -ing")
            occupation = get_word("Enter an occupation")
            insult = get_word("Enter an insult")

            print()
            print("🔧" * 33)
            print(player_name.upper() + "'S Yezzur Hell Adventure")
            print("🔧" * 33)

            print()
            print("Brother Bubba and Brother Cletus were two highly respected Freemasons, mostly because nobody had bothered to check their IQ scores, which were somewhere between a broken toaster and a wet sandwich. "
                  "One Tuesday night, the two brothers were caught selling a suspicious amount of " + type_drug + " out of the back of a " + noun + " behind the lodge. "
                  "When the police arrived, Bubba panicked and yelled, "
                  "\"Don't worry! We're " + adjective + " businessmen! We have connections!\" "
                  "Cletus immediately pulled out his Masonic ring, held it up like a driver's license, and whispered, "
                  "\"We're part of a secret organization. You can't arrest us. We know the secret handshake!\" "
                  "The officer stared at him and said, "
                  "\"Sir, you're standing in a dumpster.\" "
                  "Things got worse when Bubba attempted to bribe the officer by offering him a " + noun + " and promising to start " + verb_ing + " in the police parking lot. "
                  "Cletus, trying to sound intelligent, explained, "
                  "\"Officer, this is all just a misunderstanding. We're not criminals. We're actually undercover " + occupation + ".\" "
                  "The officer asked, "
                  "\"Then why did I find $40,000 in cash, three bags of " + type_drug + ", and a handwritten bribery ledger in your car?\" "
                  "Bubba looked at Cletus. "
                  "Cletus looked at Bubba. "
                  "Then Bubba slowly whispered, "
                  "\"I told you we shouldn't have hired that " + insult + " accountant.\" "
                  "The officer finally asked them if they had anything else to say. "
                  "Cletus stood up straight, adjusted his Masonic apron, and declared: "
                  "\"YOU MAY HAVE THE EVIDENCE, BUT YOU'LL NEVER HAVE THE SACRED KNOWLEDGE OF THE THIRD DEGREE!\" "
                  "He then accidentally gave the officer the secret handshake with his foot. "
                  "Both men were arrested. "
                  "And somewhere inside the Grand Lodge, a committee was immediately formed to investigate how two men with the combined intelligence of a potato managed to become Freemasons in the first place. "
                  "THE END.")

        story_count += 1

        print()
        print("🔧" * 33)
        print("That's been", story_count, "wacky tacky adventures!!!")

        play = input("Would you like to go on another adventure? y/n): ").lower().strip()

        while play != "y" and play != "n":
            print("Please enter y or n.")
            play = input("Would you like to go on another adventure? (y/n): ").lower().strip()

        print()
        print("Hope you had a fantastic Yezzur Mechanic Adevnture, " + player_name + "!")
        print("Remember to keep those bolts tight!!, but not too tight!!!")
        print("SOOOOOO LOOONNNGGG")


play_game()


            






            

