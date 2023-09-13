import pandas as pd
from src.main.python.DnDHistoryGenerator.Characters.characters import Character
class configuration:
    def __init__(self):
        pass
    
    def welcome(self):
        print("Welcome to the D&D History Generator")
        print("Please select an option:")
        print("1. Generate a new history")
        print("2. Generate a new history with a custom configuration")
        print("3. Exit")
    
    def generate_default_configuration(self):
        pass

    def generate_ramdon_party(self):
        ListOfCharacters = []
        for i in range(4):
            character = Character()
            character.generate_character()
            ListOfCharacters.append(character)
        return ListOfCharacters
