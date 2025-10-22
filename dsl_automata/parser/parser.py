from dsl_automata.logic.automata import Automata

class AutomataParser:
    def parse(self, file_path: str) -> Automata:
        #Vamos a armar un array de lineas con una lista por comprensión
        with open(file_path, "r") as file:
            lines = [line.strip() for line in file if line.strip() and not line.startswith('//')]
        #Esto debería armarme correctamente un array donde cada elemento es una línea del archivo
        #Ahora podemos armar el autómata.
        automata = {
            'states': set(),
            'alphabet': set(),
            'initial': '',
            'final': set(),
            'transitions': {}
        }
        section = None
        for line in lines:
        #Primero procesamos el states
            if ':' in line:
                key, value = [s.strip() for s in line.split(':', 1)]
                section = key
                if key in {'states', 'alphabet', 'final'}:
                    values = [v.strip() for v in value.split(',')]
                    #Caso especial, final vacio
                    if key == 'final' and value.strip() == "":
                        automata[key] = set()
                        continue
                    #Chequeo sintáctico
                    if not values or any(token == '' for token in values):
                        raise Exception(f"[Parser] Error en la sección '{key}': elemento vacío o mal formado.")
                    automata[key] = set(values)
                elif key == 'initial':
                    automata['initial'] = value.strip()
            elif section == 'transitions':
                left, right = [s.strip() for s in line.split('->')]
                left = left.strip('()')
                state, symbol = [s.strip() for s in left.split(',')]
                automata['transitions'][(state, symbol)] = right
        return Automata(automata['states'], automata['alphabet'], automata['initial'], automata['final'], automata['transitions'])