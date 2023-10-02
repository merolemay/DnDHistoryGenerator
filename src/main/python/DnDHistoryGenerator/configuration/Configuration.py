import pandas as pd
from characters.Characters import Character

class Configuration:

    ListofCharacters = []

    def __init__(self):
        self.welcome()
    
    def welcome(self):
        print("Welcome to the D&D History Generator")
        print("Please select an option:")
        print("1. Generate a new history with default configuration")
        print("2. Generate a new history with a custom configuration")
        print("3. Exit")
    
    def generate_default_configuration(self):
        self.generate_ramdon_party()

        


    def generate_ramdon_party(self):
        for i in range(4):
            character = Character()
            character.generate_character()
            self.ListofCharacters.append(character)
        return self.ListofCharacters
    

    def generate_custom_configuration(self):
        print("Please select the number of characters in the party:")
        number_of_characters = input()
        for i in range(number_of_characters):
            print("Please select the name of the character:")
            name = input()
            print("Please select the race of the character:")
            race = input()
            print("Please select the alignment of the character:")
            alignment = input()
            ListofCharacters = Character(name,race,alignment)
        return ListofCharacters
    
    def exit(self):
        print("Thanks for using the D&D History Generator")
        exit()