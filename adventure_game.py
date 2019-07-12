import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


choices = ["1. Go left and get out of this place!.",
           "2. Go right towards the shiny and take your chances.",
           "3. Do nothing...", ""]


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
    return response


def die_roll():
    return random.randint(1, 6)


def intro():
    print_pause("You rise from the ashes and take a deep breath...")
    print_pause("You look around...  a graveyard?!")
    print_pause("As you begin to walk through the fog and darkness,")
    print_pause("You come to a fork in the path.")
    print_pause("To the left you see the path exiting towards "
                "the mountains. ")
    print_pause("To the right you see something shiny in the distance")
    print_pause("But it looks scary and dangerous.")
    print_pause("You stop and ponder... ")


def act_one(items):
    print_pause("Please enter a number for your next action:")
    act_one_action = input('\n'.join(choices))
    if act_one_action == '2':
        scenario_two(items)
    elif act_one_action == '3':
        scenario_three(items)
    elif "death stone" in items:
        alternate_scenario_one(items)
    elif act_one_action == '1':
        scenario_one(items)
    else:
        print_pause("Not a valid selection.")
        act_one(items)


def scenario_one(items):
    print_pause("You head left towards the mountains.")
    print_pause("All of a sudden, you are rushed")
    print_pause("By a ghoul wearing a long black cloak!")
    print_pause("He draws a broken sword and strikes at you!!")
    roll_outcome(items)


def roll_outcome(items):
    roll = die_roll()
    roll_one = valid_input("Would you like to roll the dice to "
                           "see what happens: "
                           "Yes or No\n", "yes", "no")
    if "yes" in roll_one:
        roll
        print(f"You rolled a {roll}")
        if roll > 3:
            print_pause("That's a good roll.")
            print_pause("Without thinking, you dodge roll to the right")
            print_pause("You pick up a rock and smash it on the ghouls head.")
            print_pause("He falls dead to the ground.")
            print_pause("You pick up the Broken Sword")
            print_pause("Once a great sword, now useless and forgotten.")
            print_pause("You advance towards the mountains.")
            items.append("Broken Sword")
            boss_scenario(items)
        else:
            print_pause("Lady luck is not on your side.")
            print_pause("You try to run but the ghoul stabs you in the back.")
            print_pause("YOU DIED!")
            items.append("death stone")
            alternate_intro(items)
    elif "no" in roll_one:
        print_pause("YOU DIED!")
        alternate_intro(items)
    else:
        print_pause("Not a valid selection.")
        roll_outcome(items)


def scenario_two(items):
    print_pause("You summon your inner courage and head right.")
    print_pause("You reach down through the fog.")
    print_pause("Your shaky hand makes contact with something cold "
                "and hard.")
    print_pause("You grasp it with your hand and lift up the "
                "Wolf Knight\'s Greatsword!")
    items.append("Wolf Knight Greatsword")
    print_pause("A fine weapon indeed.")
    print_pause("As you advance towards the mountains through the shadows")
    print_pause("You see a ghoul... but he hasn\'t seen you....")
    sneak_action = valid_input("What will be your next action: "
                               "attack or sneak?\n",
                               "attack", "sneak")
    if "attack" in sneak_action:
        print_pause("Without hesitation you go for backstab, the "
                    "ghoul never saw you coming!!")
        print_pause("Filled with adrenaline, you march towards the "
                    "mountains.")
        boss_scenario(items)
    else:
        print_pause("You swiftly make your way around the ghould and "
                    "head towards the mountains.")
        boss_scenario(items)


def scenario_three(items):
    print_pause("You stand there doing nothing.")
    print_pause("The darkness grows stronger and consumes you.")
    print_pause("YOU DIED!")
    alternate_intro(items)


def alternate_intro(items):
    print_pause("You rise from the ashes again.")
    print_pause("You're back to where you started.")
    print_pause("You walk towards the fork in the road")
    act_one(items)


def alternate_scenario_one(items):
    print_pause("Cautiously, you begin heading left, "
                "trying to avoid the ghoul.")
    print_pause("step")
    print_pause("step")
    print_pause("SNAP!!!!")
    print_pause("The ghoul hears you and charges towards you!!")
    print_pause("The broken sword is still in his hand!")
    roll_outcome(items)


def boss_scenario(items):
    print_pause("As you exit the graveyard, you feel a cold breeze "
                "coming from the mountain pass.")
    print_pause("You stop for a moment and close your eyes..")
    print_pause("You take a deep breath and as you open them...")
    print_pause("An Abysswalker stands in front of you wielding a "
                "corrupted long sword.")
    print_pause("You firmly grasp your weapon and brace yourself.")
    print_pause("The monster lunges at you screeching in madness!!!!")
    if "Wolf Knight Greatsword" in items:
        print_pause("It thrust its sword at you, you dodge roll to the left.")
        print_pause("It turns and swings its sword in a horizontal motion.")
        print_pause("You parry his attack and in one swift swing")
        print_pause("The monster falls to the ground headless.")
        print_pause("GAME OVER")
        new_game()
    else:
        print_pause("It thrust its sword at you, you dodge roll to the left.")
        print_pause("It turns and swings its sword in a horizontal motion.")
        print_pause("You attempt to parry but the Broken Sword is "
                    "not enough..")
        print_pause("Your guard is broken, you lose your balance.")
        print_pause("The monster impales its sword through your heart "
                    "and grins in your face.")
        print_pause("YOU DIED!")
        new_game()


def new_game():
    new_game = valid_input("Would you like to play again: "
                           "Yes or No\n", "yes", "no")
    if "yes" in new_game:
        play_game()
    elif "no" in new_game:
        print_pause("Thank you for playing.")
    else:
        print_pause("Not a valid selection.")
        new_game()


def play_game():
    items = []
    intro()
    act_one(items)


play_game()
