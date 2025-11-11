from .automaton import Automaton
from .errors import *
class NFA(Automaton):
    def accepts(self, word: str) -> bool:
        pass

    def check_determinism(self):
        pass

    def __init__(self, states, alphabet, initial, final, transitions):
        super().__init__(states, alphabet, initial, final, transitions)