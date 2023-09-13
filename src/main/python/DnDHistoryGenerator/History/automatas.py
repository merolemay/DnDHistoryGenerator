from pyformlang.finite_automaton import DeterministicFiniteAutomaton
from pyformlang.regular_expression import Regex


class RegrexAutomataName:

    def __init__(self):
        regrex = Regex("^[A-Za-z][A-Za-z0-9 ]*$")
        automaton = regrex.to_epsilon_nfa().to_deterministic().minimize()
        self.automaton = automaton

    def avanzar(self, eleccion):   
        if self.automaton.accepts(eleccion):
            return True
        else:
            return False



class AccionAutomata:

    input_simbols={"Fight","Talk","Decieve","Hide","Dodge"}

    states = {"q0","q1","q2","q3","q4","q5"}

    initial_state = "q0"

   

    transitions = { 
        "q0": {"Fight": "q1", "Talk": "q2", "Decieve": "q3", "Hide": "q4", "Dodge": "q5"},
    }

    def set_final_states(self,final_state):
        self.automaton = DeterministicFiniteAutomaton(self.states, self.input_simbols, self.transitions, self.initial_state, final_state)
        
    def __init__(self):
        self.automaton = DeterministicFiniteAutomaton(self.states, self.input_simbols, self.transitions, self.initial_state, self.final_states)
       
    