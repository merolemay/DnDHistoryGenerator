from pyformlang.fst import FST

class TransductorParty:
    fst = FST()
    
    def partyPostiveReaction(self):
        input_symbols={"Fight","Talk","Deceive","Hide","Dodge"}
        output_symbols={"Fight","Talk","Deceive","Hide","Dodge"}
        states = {"q0","q1","q2","q3","q4","q5"}
        initial_state = "q0"
        final_states = {"q1","q2","q3","q4","q5"}
        transitions = {[
            ("q0","Fight","q1",["We shall fight by your side!"]),
            ("q0","Talk","q2",["We shall talk to them!"]),
            ("q0","Deceive","q3",["We shall deceieve them!"]),
            ("q0","Hide","q4",["We shall hide!"]),
            ("q0","Dodge","q5",["We shall avoid this with you!"]),
        ]}
        fst = FST(input_symbols, output_symbols, states, initial_state, final_states, transitions)
        return fst

    def partyNegativeReaction(self):
        input_symbols={"Fight","Talk","Deceive","Hide","Dodge"}
        output_symbols={"Fight","Talk","Deceive","Hide","Dodge"}
        states = {"q0","q1","q2","q3","q4","q5"}
        initial_state = "q0"
        final_states = {"q1","q2","q3","q4","q5"}
        transitions = {[
            ("q0","Fight","q1",["We shall not fight by your side!"]),
            ("q0","Talk","q2",["We shall not talk to them!"]),
            ("q0","Deceive","q3",["We shall not deceieve them!"]),
            ("q0","Hide","q4",["We shall not hide!"]),
            ("q0","Dodge","q5",["We shall not avoid this with you!"]),
        ]}
        fst = FST(input_symbols, output_symbols, states, initial_state, final_states, transitions)
        return fst
         
   
