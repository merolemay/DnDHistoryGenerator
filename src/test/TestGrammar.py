import unittest
from main.history.Grammar import Grammar
from main.characters.Characters import Character

class TestGrammar(unittest.TestCase):
    def setUp(self):
        # initialize the class
        self.grammar = Grammar()

        party = []
        
        self.character = Character()
        self.character.name = "LuciusShadowflame"
        self.character.race = "Elf"
        self.character.alignment = "Lawful-Good"

        party.append(self.character)

        self.character.name = "DamienBloodthorn"
        self.character.race = "Human"
        self.character.alignment = "True-Neutral"

        party.append(self.character)

        

    def test_generate_description(self):
        # Validate for correct input
        self.assertEqual(self.grammar.generate_description(self.party), "\na Elf of Lawful-Good alignment named LuciusShadowflame, \na Human of True-Neutral alignment named DamienBloodthorn.")

if __name__ == '__main__':
    unittest.main()