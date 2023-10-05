import random
import os
import re

class Choices:
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
            print("You decide to fight")
        elif action == "Talk":
            print("You decide to talk")
        elif action == "Deceive":
            print("You decide to deceive")
        elif action == "Hide":
            print("You decide to hide")
        elif action == "Dodge":
            print("You decide to dodge")
        
    def list_actions(self):
        print("Fight")
        print("Talk")
        print("Deceive")
        print("Hide")
        print("Dodge")


    #Validates that the input matches one of the list_actions() options
    def validateInputRegrex(self,eleccion):
        if re.match(r'fight|talk|deceive|hide|dodge|Fight|Talk|Deceive|Hide|Dodge|', eleccion):
            self.print_action(eleccion)
            return True
        else:
            print("Please select a valid option")
            return False

   

        
        
        
        

        
    
       


