from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State
from pyformlang.regular_expression import Regex

class MainHistoryAutomata:

    automaton = DeterministicFiniteAutomaton

    def __init__(self):
        input_symbols = {"True", "False"}
        q0 = State("q0")
        q1 = State("q1")
        q2 = State("q2")
        q3= State("q3")
        q4 = State("q4")
        q5 = State("q5")
        q6 = State("q6")
        q7= State("q7")
        q8 = State("q8")
        q9= State("q9")
        q10 = State("q10")
        q11 = State("q11")
        q12 = State("q12")
        q13 = State("q13")
        states = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11,q12,q13}
        initial_state = q0
        final_states = {q7,q8, q12, q13}
        transitions = [
            (q0, "True", q1),
            (q0, "False", q2),

            (q1, "True", q3),
            (q1, "False", q4),

            (q2, "True", q9),
            (q2, "False", q10),

            (q3, "True", q5),
            (q3, "False", q6),

            (q4, "True", q5),
            (q4, "False", q6),

            (q5, "True", q7),
            (q5, "False", q8),

            (q6, "True", q7),
            (q6, "False", q8),

            (q9, "True", q3),
            (q9, "False", q4),

            (q10, "True", q7),
            (q10, "False", q13),

            (q11, "True", q12),
            (q11, "False", q13)
        ]
        
        self.automaton = DeterministicFiniteAutomaton(states, input_symbols, transitions, initial_state, final_states)

    def check(self, eleccion):   
        if self.automaton.accepts(eleccion):
            return True
        else:
            return False
        
    