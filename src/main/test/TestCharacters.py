# # test all the methods in class characters from package interaction using unit test
import unittest
from characters.Characters import Character

class TestCharacters(unittest.TestCase):
    
        def setUp(self):
            # initialize the class
            self.character = Character()
            self.character.generate_character()
            
        def test_generate_character(self):
            self.assertTrue(len(self.character.name) > 0)
            self.assertTrue(len(self.character.race) > 0)
            self.assertTrue(len(self.character.alignment) > 0)

if __name__ == '__main__':
    unittest.main()