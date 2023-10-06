from history.Automatas import MainHistoryAutomata

class Finals:
    
    def obtener_final(self, eleccion_usuario):
        automata = MainHistoryAutomata()
        if automata.check(eleccion_usuario):
            return "good"
        else:
            return "bad"
        
    
    def good_ending(self):
        print("You have completed the quest and kept your party alive")
        print("You have won the game")

    def bad_ending(self):
        print("You have died and your party has been defeated")
        print("You have lost the game")
    
    def neutral_ending(self):
        print("You have completed the quest but your party has been defeated")
        print("You have lost the game")

    
    def present_ending(self, eleccion_usuario):
        if self.obtener_final(eleccion_usuario) == "good":
            self.good_ending()
        elif self.obtener_final(eleccion_usuario) == "bad":
            self.bad_ending()
        elif self.obtener_final(eleccion_usuario) == "neutral":
            self.neutral_ending()
        else:
            print("You have lost the game")
            print("You have lost the game")

        
        