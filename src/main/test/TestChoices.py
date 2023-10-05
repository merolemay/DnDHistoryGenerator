# test all the methods in class Choices from package interaction using unit test
import unittest
from interaction.Choices import Choices

class TestChoices(unittest.TestCase):

    def setUp(self):
        # initialize the class
        self.choices = Choices()
        
    def test_present_choices(self):
        self.assertTrue(True)

    def test_validateInputRegrex(self):
        self.assertTrue(self.choices.validateInputRegrex("Fight"))
        self.assertTrue(self.choices.validateInputRegrex("Talk"))
        self.assertTrue(self.choices.validateInputRegrex("Deceive"))
        self.assertTrue(self.choices.validateInputRegrex("Hide"))
        self.assertTrue(self.choices.validateInputRegrex("Dodge"))
        self.assertTrue(self.choices.validateInputRegrex("fight"))
        self.assertTrue(self.choices.validateInputRegrex("talk"))
        self.assertTrue(self.choices.validateInputRegrex("deceive"))
        self.assertTrue(self.choices.validateInputRegrex("hide"))
        self.assertTrue(self.choices.validateInputRegrex("dodge"))

        self.assertFalse(self.choices.validateInputRegrex("f"))
        self.assertFalse(self.choices.validateInputRegrex("t"))
        self.assertFalse(self.choices.validateInputRegrex("d"))
        self.assertFalse(self.choices.validateInputRegrex("fighting"))

if __name__ == '__main__':
    unittest.main()