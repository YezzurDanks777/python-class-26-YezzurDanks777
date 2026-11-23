# Sergio Ortiz
# 11/22/2026
# Project 3

import random


def generate_character(name, faction):

    ranks = [
        "Boss",
        "Underboss",
        "Capo",
        "Lieutenant",
        "Enforcer",
        "Soldier",
        "Recruit"
    ]

    backgrounds = [
        "Street Strategist",
        "Former Boxer",
        "Business Operator",
        "Veteran Fighter",
        "Neighborhood Leader",
        "Tactical Specialist"
    ]

    character = {
        "name": name,
        "faction": faction,
        "rank": random.choice(ranks),
        "background": random.choice(backgrounds),
        "strength": random.randint(5, 20),
        "defense": random.randint(5, 20),
        "intelligence": random.randint(5, 20),
        "influence": random.randint(5, 20),
        "reputation": random.randint(5, 20),
        "hp": 100,
        "max_hp": 100
    }

    return character


def display_character(character):

    print("\n" + "🐍" * 40)
    print("          Gangster Profile")
    print("🐍" * 40)

    print("Name:", character["name"])
    print("Gang:", character["faction"])
    print("Rank:", character["rank"])
    print("Background:", character["background"])

    print("\n" + "🐍" * 40)

    print("Strength:", character["strength"])
    print("Defense:", character["defense"])
    print("Intelligence:", character["intelligence"])
    print("Influence:", character["influence"])
    print("Reputation:", character["reputation"])
    print("Health:", character["hp"])

    print("\n" + "🐍" * 40)


def choose_attack(character):

    attacks = [
        ("Punch", 5, 12),
        ("Kick", 7, 15),
        ("Gash", 8, 16),
        ("Heavy Blow", 10, 18),
        ("Quick Strike", 4, 10),
        ("Power Strike", 12, 20),
        ("Special Move", 14, 22)
    ]

    attack = random.choice(attacks)

    attack_name = attack[0]
    minimum_damage = attack[1]
    maximum_damage = attack[2]

    damage = random.randint(minimum_damage, maximum_damage)

    damage += character["strength"] // 5

    return attack_name, damage


def battle(player, opponent):

    player["hp"] = player["max_hp"]
    opponent["hp"] = opponent["max_hp"]

    print("\n" + "🐍" * 40)
    print("           Get Ready to Rumble")
    print("🐍" * 40)

    print(player["name"], "VS", opponent["name"])

    for round_number in range(1, 6):

        print("\n🐍🐍🐍 ROUND", round_number, "🐍🐍🐍")

        # Player attacks

        attack_name, damage = choose_attack(player)

        damage = max(1, damage - opponent["defense"] // 4)

        opponent["hp"] -= damage

        print("\n" + player["name"], "uses", attack_name + "!")
        print("Damage dealt:", damage)

        if opponent["hp"] <= 0:
            opponent["hp"] = 0
            print(opponent["name"], "has been defeated!")
            break

        # Opponent healing

        if random.randint(1, 5) == 1:

            healing = random.randint(5, 12)

            opponent["hp"] = min(
                opponent["max_hp"],
                opponent["hp"] + healing
            )

            print(opponent["name"], "recovers", healing, "health!")

        # Opponent attacks

        attack_name, damage = choose_attack(opponent)

        damage = max(1, damage - player["defense"] // 4)

        player["hp"] -= damage

        print("\n" + opponent["name"], "uses", attack_name + "!")
        print("Damage dealt:", damage)

        if player["hp"] <= 0:
            player["hp"] = 0
            print(player["name"], "has been defeated!")
            break

        # Player healing

        if random.randint(1, 5) == 1:

            healing = random.randint(5, 12)

            player["hp"] = min(
                player["max_hp"],
                player["hp"] + healing
            )

            print(player["name"], "recovers", healing, "health!")

        # Display score

        print("\n🐍🐍🐍 SCORE 🐍🐍🐍")

        print(player["name"], "Health:", player["hp"])
        print(opponent["name"], "Health:", opponent["hp"])

    # Determine winner

    print("\n" + "🐍" * 40)
    print("           Winner Winner Chicken Dinner")
    print("🐍" * 40)

    if player["hp"] > opponent["hp"]:

        print(player["name"], "VICTORY!")

    elif opponent["hp"] > player["hp"]:

        print(opponent["name"], "VICTORY!")

    else:

        print("NO WINNER! BOTH ARE LAMES!")

    print("\nFinal Health:")
    print(player["name"] + ":", player["hp"])
    print(opponent["name"] + ":", opponent["hp"])

    print("\n" + "🐍" * 40)


def main():

    print("\n" + "🐍" * 40)
    print("       Bloods & Crips Fair Fade")
    print("🐍" * 40)

    start_game = input(
        "\nWould you like to catch a fair fade? (yes/no): "
    )

    while start_game.lower() in ["yes", "y"]:

        name = input("\nEnter your hood name: ")

        if name.strip() == "":
            name = "Unknown Character"

        print("\nChoose your hood:")
        print("1. Bloods")
        print("2. Crips")

        faction_choice = input("Enter 1 or 2: ")

        if faction_choice == "1":

            faction = "Bloods"
            opponent_faction = "Crips"

        elif faction_choice == "2":

            faction = "Crips"
            opponent_faction = "Bloods"

        else:

            print("Invalid selection. Bloods selected by default.")

            faction = "Bloods"
            opponent_faction = "Crips"

        player = generate_character(name, faction)

        print("\nYour Main Head has been created!")

        display_character(player)

        battle_again = "yes"

        while battle_again.lower() in ["yes", "y"]:

            opponent_names = [
                "Shadow",
                "Razor",
                "Ghost",
                "Kingpin",
                "Ace",
                "Viper",
                "Tank",
                "Smoke"
            ]

            opponent_name = random.choice(opponent_names)

            opponent = generate_character(
                opponent_name,
                opponent_faction
            )

            print("\nYour enemy has been created!")

            display_character(opponent)

            battle(player, opponent)

            battle_again = input(
                "\nWould you like to catch another fade? (yes/no): "
            )

        start_game = input(
            "\nWould you like to create a new Main Head? (yes/no): "
        )

    print("\nThanks for playing Bloods & Crips Fair Fade!")


main()

# Starting file for PROJECT 3
# Include your course number, student first and last name, and date in the comment header
