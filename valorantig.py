# Made by Eshaan Kumar on 9/7/2020
# Last updated 9/7/2020 by Eshaan Kumar

# Import modules
import random

# Set dictionary for guns and numbers
gun_dict = {1: "Classic", 2: "Shorty", 3: "Frenzy", 4: "Ghost", 5: "Sherrif", 6: "Stinger", 7: "Spectre", 8: "Bucky", 9: "Judge", 10: "Bulldog", 11: "Guardian", 12: "Phantom", 13: "Vandal", 14: "Marshal", 15: "Operator", 16: "Ares", 17: "Odin"}

# Make function
def main_func():
    '''main function for valorant 1v1s gun combos'''
    gun_num = random.randrange(1, 18)
    print(gun_dict[gun_num])

# Make func for gun or not input
def output_or_not_func():
    '''asks if user wants another gun or not'''
    output_or_not = input("Do you want a new gun [y/n]: ")

    if output_or_not == "y":
        main_func()
        output_or_not_func()
    elif output_or_not == "n":
        exit()
    else:
        print("Please enter y or n")
        output_or_not_func()

output_or_not_func()
