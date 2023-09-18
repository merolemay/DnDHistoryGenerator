import pandas as pd
from characters.Characters import Character

class Configuration:
    def __init__(self):
        pass
    
    def welcome(self):
        print("Welcome to the D&D History Generator")
        print("Please select an option:")
        print("1. Generate a new history")
        print("2. Generate a new history with a custom configuration")
        print("3. Exit")
    
    def generate_default_configuration(self):
        generate_ramdon_party()


    def generate_ramdon_party(self):
        ListOfCharacters = []
        for i in range(4):
            character = Character()
            character.generate_character()
            ListOfCharacters.append(character)
        return ListOfCharacters
 