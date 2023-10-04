from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State
from pyformlang.regular_expression import Regex

class MainHistoryAutomata:

    automaton = DeterministicFiniteAutomaton

    def __init__(self):
        input_symbols = {"1", "2"}
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
            (q0, "1", q1),
            (q0, "2", q2),

            (q1, "1", q3),
            (q1, "2", q4),

            (q2, "1", q9),
            (q2, "2", q10),

            (q3, "1", q5),
            (q3, "2", q6),

            (q4, "1", q5),
            (q4, "2", q6),

            (q5, "1", q7),
            (q5, "2", q8),

            (q6, "1", q7),
            (q6, "2", q8),

            (q9, "1", q3),
            (q9, "2", q4),

            (q10, "1", q7),
            (q10, "2", q13),

            (q11, "1", q12),
            (q11, "2", q13)
        ]
        
        self.automaton = DeterministicFiniteAutomaton(states, input_symbols, transitions, initial_state, final_states)

    def check(self, eleccion):   
        if self.automaton.accepts(eleccion):
            return 1
        else:
            return 2
        
    