from .exceptions import AutomataError
from .errors import *
from abc import ABC, abstractmethod
class Automata(ABC):
    """Abstract class for automata, next time I'll add DFA and NFA"""
    def __init__(self, states, alphabet, initial, finals, transitions):
        self.valid_automata(states, alphabet, initial, finals, transitions)
        self._states = states
        self._alphabet = alphabet
        self._initial = initial
        self._finals = finals
        self._transitions = transitions
    def _raise(self, message):
        raise AutomataError(message)
    def valid_automata(self, states, alphabet, initial, final, transitions):
        """Check if automata is valid."""
        #First, we're going to check if all final and the initial state are in the states set.
        self.validate_initial_state_in_states_set(initial, states)
        self.validate_final_states_in_states_set(final, states)
        #Next, we're going to check that all the transitions states are in states set.
        #and the character used is in alphabet.
        self.validate_all_transitions_states_in_states_set_and_all_symbols_in_alphabet(alphabet, states, transitions)
    @abstractmethod
    def accepts(self, word: str) -> bool:
        """Check if word is accepted by this automata."""
        pass
    def validate_all_transitions_states_in_states_set_and_all_symbols_in_alphabet(self, alphabet, states, transitions):
        for (state, symbol), targets in transitions.items():
            if state not in states:
                self._raise(ERROR_UNKNOWN_TRANSITION_STATE.format(state=state))
            for target in targets:
                if target not in states:
                    self._raise(ERROR_UNKNOWN_TRANSITION_TARGET.format(target=target))
            if symbol not in alphabet:
                self._raise(ERROR_SYMBOL_NOT_IN_ALPHABET.format(symbol=symbol))

    def validate_final_states_in_states_set(self, final, states):
        for state in final:
            if state not in states:
                self._raise(ERROR_FINAL_NOT_IN_STATES.format(state=state))

    def validate_initial_state_in_states_set(self, initial, states):
        if initial not in states:
            self._raise(ERROR_INITIAL_NOT_IN_STATES)

