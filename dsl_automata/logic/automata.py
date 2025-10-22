class Automata:
    def __init__(self, states, alphabet, initial, final, transitions):
        #self.valid_automata(states, alphabet, initial, final, transitions)
        self._states = states
        self._alphabet = alphabet
        self._initial = initial
        self._final = final
        self._transitions = transitions

    #def valid_automata(self, states, alphabet, initial, final, transitions):

