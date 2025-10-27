from dsl_automata.logic.automaton import Automaton
from dsl_automata.logic.dfa import DFA
class AutomataParser:
    def parse(self, file_path: str) -> Automaton:
        #Vamos a armar un array de lineas con una lista por comprensión
        with open(file_path, "r") as file:
            lines = [line.strip() for line in file if line.strip() and not line.startswith('//')]
        #Esto debería armarme correctamente un array donde cada elemento es una línea del archivo
        #Ahora podemos armar el autómata.
        automaton = {
            'states': set(),
            'alphabet': set(),
            'initial': '',
            'final': set(),
            'transitions': {}
        }
        section = None
        for line in lines:
        #Primero
            if ':' in line:
                key, value = [s.strip() for s in line.split(':', 1)]
                section = key
                if key in {'states', 'alphabet', 'final'}:
                    values = [v.strip() for v in value.split(',')]
                    #Caso especial, final vacio
                    if key == 'final' and value.strip() == "":
                        automaton[key] = set()
                        continue
                    #Chequeo sintáctico
                    if not values or any(token == '' for token in values):
                        raise Exception(f"[Parser] Error en la sección '{key}': elemento vacío o mal formado.")
                    automaton[key] = set(values)
                elif key == 'initial':
                    automaton['initial'] = value.strip()
            elif section == 'transitions':
                left, right = [s.strip() for s in line.split('->')]
                left = left.strip('()')
                state, symbol = [s.strip() for s in left.split(',')]
                key = (state, symbol)
                if key not in automaton['transitions']:
                    automaton['transitions'][key] = set()
                automaton['transitions'][key].add(right)
        return DFA(automaton['states'], automaton['alphabet'], automaton['initial'], automaton['final'], automaton['transitions'])