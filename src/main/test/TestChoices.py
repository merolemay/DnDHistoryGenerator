# test all the methods in class Choices from package interaction using unit test
import unittest
from interaction.Choices import Choices

class TestChoices(unittest.TestCase):

    def setUp(self):
        # initialize the class
        self.choices = Choices()

    def test_validateInputRegrex(self):
        # Validate for correct input
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

        # Validate for incorrect input
        self.assertFalse(self.choices.validateInputRegrex("f"))
        self.assertFalse(self.choices.validateInputRegrex("t"))
        self.assertFalse(self.choices.validateInputRegrex("d"))
        self.assertFalse(self.choices.validateInputRegrex("fighting"))

    def test_validateInputYesorNo(self):
        # Validate for correct input
        self.assertTrue(self.choices.validateInputYesorNo("Y"))
        self.assertTrue(self.choices.validateInputYesorNo("N"))
        self.assertTrue(self.choices.validateInputYesorNo("y"))
        self.assertTrue(self.choices.validateInputYesorNo("n"))

        # Validate for incorrect input
        self.assertFalse(self.choices.validateInputYesorNo("Yes"))
        self.assertFalse(self.choices.validateInputYesorNo("No"))
        self.assertFalse(self.choices.validateInputYesorNo("yes"))
        self.assertFalse(self.choices.validateInputYesorNo("no"))

if __name__ == '__main__':
    unittest.main()