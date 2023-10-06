from pyformlang.fst import FST

class TransductorParty:
    fst = FST()
    
    def partyPostiveReaction(self,action):
        fst = FST()
        fst.add_transitions([
            ("q0","Fight","q1",["We shall fight by your side!"]),
            ("q0","Talk","q2",["We shall talk to them!"]),
            ("q0","Deceive","q3",["We shall deceieve them!"]),
            ("q0","Hide","q4",["We shall hide!"]),
            ("q0","Dodge","q5",["We shall avoid this with you!"]),
        ])

        fst.add_start_state("q0")
        fst.add_final_state("q1,q2,q3,q4,q5")

        return "The party says:"+fst.translate(action.__str__())[0][0]

   
    def partyNegativeReaction(self,action):
        fst = FST()

        fst.add_transitions([
            ("q0","Fight","q1",["We shall not fight by your side!"]),
            ("q0","Talk","q2",["We shall not talk to them!"]),
            ("q0","Deceive","q3",["We shall not deceieve them!"]),
            ("q0","Hide","q4",["We shall not hide!"]),
            ("q0","Dodge","q5",["We shall not avoid this with you!"]),
        ])

        fst.add_start_state("q0")
        fst.add_final_state("q1,q2,q3,q4,q5")
            
        return "The party says:"+fst.translate(action.__str__())[0][0]
         
   
