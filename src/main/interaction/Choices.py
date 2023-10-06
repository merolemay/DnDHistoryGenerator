import random
import os
import re

class Choices:

    #validates that the input matches 1 or 2
    def validatedInputNumber(self,eleccion):
        return re.match(r'1|2', eleccion)
    
    def present_introduction(self):
        print(self.load_ramdon_scenario())
    

    def load_ramdon_scenario(self):
        with open(os.path.join(os.path.dirname(__file__),'../data/Story_Scenario_Introuction.txt'), 'r') as f:
            textos = f.read().split(';')
            return random.choice(textos)
    
    def present_choices(self):
        print("Please select an option:")
        self.list_actions()

    def print_action(self,action):
        if action == "Fight":
            print("You've decided to fight")
        elif action == "Talk":
            print("You've decided to talk")
        elif action == "Deceive":
            print("You've decided to deceive")
        elif action == "Hide":
            print("You've decided to hide")
        elif action == "Dodge":
            print("You've decided to dodge")
        
    def list_actions(self):
        print("Fight")
        print("Talk")
        print("Deceive")
        print("Hide")
        print("Dodge")


    #Validates that the input matches one of the list_actions() options
    def validateInputRegrex(self,eleccion):
        if re.match(r'fight|Fight|Hide|hide', eleccion):
            self.print_action(eleccion)
            return True
        else:
            print("Please select a valid option")
            return False
        
    def validateInputYesorNo(self,eleccion):
        if re.match(r'Y|N|y|n', eleccion):
            return True
        else:
            print("Please select a valid option")
            return False


   

        
        
        
        

        
    
       


