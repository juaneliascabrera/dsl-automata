from .automaton import Automaton
from .errors import *
class DFA(Automaton):
    def __init__(self, states, alphabet, initial, final, transitions):
        super().__init__(states, alphabet, initial, final, transitions)
        self.check_determinism()
    """Determinism checker"""
    def check_determinism(self):
        for(state, symbol), dest in self._transitions.items():
            if len(dest) > 1:
                self._raise(ERROR_AUTOMATA_IS_NOT_DETERMINISTIC)
    """DFA accept"""
    def accepts(self, word: str) -> bool:
        actual_state = self._initial
        for symbol in word:
            key = (actual_state, symbol)
            if key not in self._transitions:
                return False
            destinations = self._transitions[key]
            actual_state = next(iter(destinations))
        return actual_state in self._finals