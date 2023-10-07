from pyformlang.fst import FST

class TransductorParty:
    fst = FST()
    
    def partyPostiveReaction(self,action):
        if action == "Fight":
            action = "f"
        else:
            action = "h"

        fst = FST()
        fst.add_transitions([
            ("q0","f","q1",["We shall fight by your side!"]),
            ("q0","h","q4",["We shall hide!"]),
        ])

        fst.add_start_state("q0")
        fst.add_final_state("q1")
        fst.add_final_state("q4")

        return "The party says:"+"".join(list(fst.translate(action))[0])

   
    def partyNegativeReaction(self,action):
        if action == "Fight":
            action = "f"
        else:
            action = "h"

        fst = FST()

        fst.add_transitions([
        ("q0","f","q1",["We shall not fight by your side!"]),
        ("q0","h","q4",["We shall not hide!"]),
        ])


        fst.add_start_state("q0")
        fst.add_final_state("q1")
        fst.add_final_state("q4")
            
        return "The party says:"+"".join(list(fst.translate(action))[0])
         
   
