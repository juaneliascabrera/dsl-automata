from .automata import Automata
from .errors import *
class DFA(Automata):
    def __init__(self, states, alphabet, initial, final, transitions):
        super().__init__(states, alphabet, initial, final, transitions)
        self.is_deterministic()
    #We should implement the method is_deterministic
    def is_deterministic(self):
        """Check if the automata is deterministic."""
        #We should check if all transitions go to a singleton set
        for (state, symbol), destinations in self._transitions.items():
            if len(destinations) > 1:
                self._raise(ERROR_AUTOMATA_IS_NOT_DETERMINISTIC.format(state=state, symbol = symbol, destinations = destinations))

        pass
    def accepts(self, word: str) -> bool:
        actual_state = self._initial
        for symbol in word:
            key = (actual_state, symbol)
            if key not in self._transitions:
                return False
            destinations = self._transitions[key]
            actual_state = next(iter(destinations))
        return actual_state in self._finals