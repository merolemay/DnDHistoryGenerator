from pyformlang.finite_automaton import DeterministicFiniteAutomaton
from pyformlang.regular_expression import Regex


class RegrexAutomataName:

    regrex = Regex("^[A-Za-z][A-Za-z0-9 ]*$")

    automaton = regrex.to_epsilon_nfa().to_deterministic().minimize()

    def __init__(self):
        pass

    def avanzar(self, eleccion):   
        if self.automaton.accepts(eleccion):
            return True
        else:
            return False



    def generar_automata(self, eleccion):
        pass


