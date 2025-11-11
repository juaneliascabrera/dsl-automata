from dsl_automata.logic.automaton import Automaton
from dsl_automata.logic.dfa import DFA
from dsl_automata.logic.nfa import NFA


class AutomataParser:
    @staticmethod
    def parse(file_path: str) -> Automaton:
        # Leemos líneas válidas (sin comentarios ni vacías)
        with open(file_path, "r") as file:
            lines = [line.strip() for line in file if line.strip() and not line.startswith("//")]

        automaton = {
            "type": "",
            "states": set(),
            "alphabet": set(),
            "initial": "",
            "final": set(),
            "transitions": {},
        }

        section = None
        for line in lines:
            # Detectar nuevas secciones
            if ":" in line:
                key, value = [s.strip() for s in line.split(":", 1)]
                section = key
                if section == "type":
                    automaton["type"] = value.upper()
                elif key in {"states", "alphabet", "final"}:
                    values = [v.strip() for v in value.split(",") if v.strip()]
                    if key == "final" and not value.strip():
                        automaton[key] = set()
                        continue
                    if not values or any(token == "" for token in values):
                        raise Exception(f"[Parser] Error en la sección '{key}': elemento vacío o mal formado.")
                    automaton[key] = set(values)
                elif key == "initial":
                    automaton["initial"] = value.strip()

            # Procesar líneas de transiciones
            elif section == "transitions":
                if "->" not in line:
                    raise Exception(f"[Parser] Línea de transición mal formada: '{line}'")

                left, right = [s.strip() for s in line.split("->", 1)]
                left = left.strip("()")

                if "," not in left:
                    raise Exception(f"[Parser] Formato inválido en transición: '{line}'")

                state, symbol = [s.strip() for s in left.split(",", 1)]
                key = (state, symbol)

                # Diferenciar según tipo
                if automaton["type"] == "DFA":
                    if key in automaton["transitions"]:
                        raise Exception(f"[Parser] Transición duplicada en DFA: {key}")
                    automaton["transitions"][key] = {right}

                elif automaton["type"] == "NFA":
                    destinations = {v.strip() for v in right.split(",") if v.strip()}
                    automaton["transitions"].setdefault(key, set()).update(destinations)

                else:
                    raise Exception("[Parser] No se especificó un tipo de autómata válido antes de 'transitions:'.")

        # --- Construcción final ---
        if automaton["type"] == "DFA":
            return DFA(
                automaton["states"],
                automaton["alphabet"],
                automaton["initial"],
                automaton["final"],
                automaton["transitions"],
            )
        elif automaton["type"] == "NFA":
            raise NotImplementedError("[Parser] Soporte para NFA aún no implementado.")
        else:
            raise Exception(
                f"[Parser] Tipo de autómata desconocido: '{automaton['type']}'. "
                "Debe ser 'DFA' o 'NFA'."
            )
