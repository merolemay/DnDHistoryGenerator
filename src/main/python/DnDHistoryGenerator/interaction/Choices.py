from history.Automatas import AccionAutomata
import random
import os

class Choices:
    def present_introduction(self):
        print(self.load_ramdon_scenario())
    

    def load_ramdon_scenario(self):
        with open(os.path.join(os.path.dirname(__file__),'../data/Story_Scenario_Introuction.txt'), 'r') as f:
            textos = f.read().split(';')
            return random.choice(textos)
    
    def present_choices(self):
        print("Please select an option:")
        AccionAutomata().list_actions()
        
        
        
        

        
    
       


