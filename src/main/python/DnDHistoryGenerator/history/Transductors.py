from pyformlang.fst import FST

class TransductorParty:
    fst = FST()
    
    def partyPostiveReaction(self) 
        input_simbols={"Fight","Talk","Decieve","Hide","Dodge"}
        output_simbols={"Fight","Talk","Decieve","Hide","Dodge"}
        states = {"q0","q1","q2","q3","q4","q5"}
        initial_state = "q0"
        final_states = {"q1","q2","q3","q4","q5"}
        transitions = {[
            ("q0","Fight","q1",["We shall fight by your side!"]),


        ]}
        fst = FST(input_simbols, output_simbols, states, initial_state, final_states, transitions)
        return fst

    def partyNegativeReaction(self)
         
   
    