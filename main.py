"""A simple choose your own adventure story separated into 2 parts. The
first was made for practice and is therefore a bit linear, and the second 
adds more weight to your choices."""

__author__ = "Davin Benson"


# COP 1500
# Integration Project Final
# Spring 2021


def phase_one():
    """Pretty much just a test run and messing with numbers"""
    print("Welcome to the Virtual Fantasy Combat Simulator 0.1 Beta")
    play_name = input("Please enter your name: ")
    print("Hello,", play_name, "\nThe simulation begins now.")
    print(
        "Due to a lack of funding, we must ask that you rely on your "
        "imagination to visualize the upcoming events.")
    print(
        "There is also no limit to any damage values, so go overboard at your "
        "own risk.", end='\n\n')
    print(
        "Your first opponent will be a common slime enemy. You are given a "
        "sword to defend yourself.")
    dmg1 = abs(
        int(input("To begin, assign a damage number value to your sword: ")))
    print(play_name + " strikes the slime dealing ", dmg1,
          " damage. The slime is defeated.", sep='', end='\n\n')
    print("Next up, a goblin approaches holding a wooden shield.")
    dmg2 = abs(int(input(
        "Try a different attack this time. Enter another damage value: ")))
    print(
        play_name + " swings at the goblin, its shield blocking some of the "
                    "force. ",
        abs(dmg2 - 50), " damage is dealt.", sep='')
    num_hits = abs(
        int(input("It's wide open. How many times do you hit it?: ")))
    flurry_dmg = (dmg2 * num_hits)
    print(play_name + " throws a flurry of strikes at the goblin dealing ",
          flurry_dmg, " damage. Another victory.", sep='', end='\n\n')
    print("Here comes a strong knight. His armor looks sturdy.")
    dmg3 = abs(int(input(
        "Go for another technique. Enter an extra powerful damage value: ")))
    armor_hit = int(dmg3 / 3)
    print(
        play_name + " swipes at the knight, though he stands his ground and"
                    " takes only ",
        armor_hit, " damage.", sep='')
    print("It isn't enough. Time for extreme measures.")
    potion_dmg = abs(int(input(
        "You take a strength potion. Enter the potency of its effect: ")))
    enhanced_dmg = int(dmg3 ** potion_dmg)
    less_enhanced_dmg = int(enhanced_dmg / 3)
    print(play_name + " goes all out, striking the knight with ",
          less_enhanced_dmg, " damage. It is enough.", sep='', end='\n\n')
    print("You feel unstoppable. Next you challenge a giant dragon.")
    combo1 = abs(int(input(
        "Time to use everything you've learned. Try a combo of strikes,"
        " how many?: ")))
    combo2 = ((dmg1 + dmg2 + dmg3) * combo1) ** potion_dmg
    print(
        "The dragon is no match for your power. You strike relentlessly"
        " dealing ",
        combo2, " damage. Easy.", sep='', end='\n\n')
    print(
        "No worldly force can hold you back any longer. You challenge the"
        " simulation itself.")
    final_hit = abs(int(input(
        "You open the developer console and type in the largest number you"
        " can think of: ")))
    print("You swing at nothing in particular dealing ", combo2 * final_hit,
          " damage to the fabric of space-time.", sep='', end='\n\n')
    print("You have torn a hole in reality.")
    print("The simulation is over." * 20, end=" goodbye.")
    # For the sake of documentation, I kept this in here. It is not very
    # well optimised so I hope that's OK. This project should meet the
    # requirements even without it.


def phase_two():
    """The real game, should be more interactive"""
    print("Welcome, adventurer, to the REAL simulator. Your task is to "
          "defeat the dragon. Take the appropriate action to "
          "avoid damage and strike most effectively")
    while True:
        try:
            weapon_choice = int(input("To start, pick a weapon. \n 1 for sword"
                                      " \n 2 for axe \n 3 for bow \n"
                                      "(Or something else if you want to be "
                                      "stubborn) \n Enter: "))
            break
        except ValueError:
            print("Error. Please enter a valid integer")
    if weapon_choice == 1:
        damage_value = 15
        print("You picked the sword. A well rounded weapon.")
    elif weapon_choice == 2:
        damage_value = 20
        print(
            "You picked the axe. You can deal a lot of damage, although it's "
            "slow and heavy.")
    elif weapon_choice == 3:
        damage_value = 10
        print("You picked the bow. You can deal damage from a range.")
    else:
        damage_value = 2
        print("No weapon? Bold choice.")
    print(
        "The battle will now begin")
    player_health = 50
    dragon_health = 50
    while player_health in range(1, 10):
        print("Watch out! Your health is low")
    # The following will loop until either the player or dragon's health
    # reaches 0
    while dragon_health > 0 and player_health > 0:
        while True:
            try:
                player_turn = int(input(
                    "You have the advantage. The dragon expects nothing \n "
                    "Enter 1 to attack \n Enter 2 to guard"
                    "\n Enter 3 to run: "))
                break
            except ValueError:
                print("Error. Please enter a valid integer")
        if player_turn == 1:
            dragon_health += -damage_value
            print("You strike at the dragon dealing", damage_value, "damage")
        elif player_turn == 2:
            player_health += -10
            print(
                "You prepare yourself for an attack that never comes. "
                "The dragon notices you right when you drop your"
                " guard, "
                "and hits you dealing 10 damage.")
        elif player_turn == 3:
            player_health += -5
            print("Where are you going? You trip and take 5 damage.")
        else:
            print("You do nothing. How productive.")
        while True:
            try:
                player_turn_2 = int(input(
                    "The dragon is about to take to the skies. "
                    "\n Enter 1 to attack \n Enter 2 to guard \n Enter 3 to "
                    "run: "))
                break
            except ValueError:
                print("Error. Please enter a valid integer.")
        # Different scenarios happen depending on what weapon the
        # player chose at the beginning
        if player_turn_2 == 1:
            if damage_value == 15 or damage_value == 20 or \
                    damage_value == 2:
                player_health += -10
                print(
                    "You try attacking the dragon but it's already too"
                    " far away. It swoops back down and you take 10 "
                    "damage.")
            else:
                dragon_health += -damage_value
                print(
                    "You shoot at the dragon and land a far shot"
                    " dealing 10 damage.")
        elif player_turn_2 == 2:
            dragon_health += -5
            player_health += -5
            print(
                "The dragon dives at you. You can't block the full "
                "force of the attack and take 5 damage, and the "
                "dragon takes 5 damage as well.")
        elif player_turn_2 == 3:
            dragon_health += -5
            print(
                "You run from the dragon's attack and miraculously"
                " dodge.The missed impact deals 5 damage to the"
                " dragon.")
        else:
            player_health += -15
        print(
            "You stand completely still and take the full force of"
            " the dragon's next attack.")
        while True:
            try:
                player_turn_3 = int(input(
                    "The dragon readies its fire breath. \n Enter 1 to attack"
                    " \n Enter 2 to guard \n Enter 3 to run: "))
                break
            except ValueError:
                print("Error. Please enter an integer.")
        if player_turn_3 == 1:
            if damage_value in range(2, 16):
                dragon_health += -damage_value
                player_health += -15
                print(
                    "You're able to get an attack in but the dragon"
                    " retaliates with fire burning you with 15 damage.")
            else:
                player_health += -15
                print(
                    "You attempt to strike with your axe but can't before"
                    " being burned, taking 15 damage.")
        elif player_turn_3 == 2:
            player_health += -10
            print(
                "It's pretty hard to guard against fire like this."
                " You take 10 damage.")
        elif player_turn_3 == 3:
            player_health += -10
            dragon_health += -5
            print(
                "You run around wildly trying to dodge the attack,"
                " but are unable to fully. The dragon burns itself trying"
                " to keep up with you.")
        else:
            dragon_health += -5
            print(
                "The dragon is so confused by your inaction that it ends"
                " up missing its attack and burning itself")
    else:
        if dragon_health < 0:
            dragon_health = 0
            print("You win!")
        if player_health < 0:
            player_health = 0
            print("You lose...")
        print("The game is over. The dragon has", dragon_health,
              "health left and you have", player_health, "health left.")
        print("Thanks for playing.")


def main():
    """Runs the program and allows you to skip the first phase."""
    while True:
        try:
            skip_phase1 = int(input(
                "The first phase of this project is, put simply, not very fun."
                "Enter '1' to skip and any other number to continue: "))
            break
        except ValueError:
            print("Error. Please enter a valid integer.")
    if skip_phase1 != 1:
        phase_one()
    phase_two()


#####################################

if __name__ == "__main__":
    main()
