from dsl_automata.parser.parser import AutomataParser
import os
import pytest
def test_parser_basico():
    current_dir = os.path.dirname(__file__)
    automata_file = os.path.join(current_dir, "test.automata")

    parser = AutomataParser()
    automata = parser.parse(automata_file)

    assert automata._states == {"q0", "q1"}
    assert automata._alphabet == {"a", "b"}
    assert automata._initial == "q0"
    assert automata._final == {"q1"}
    assert automata._transitions == {
        ("q0", "a"): "q1",
        ("q1", "b"): "q0"
    }
def test_parser_basico2():
    current_dir = os.path.dirname(__file__)
    automata_file = os.path.join(current_dir, "test2.automata")

    parser = AutomataParser()
    automata = parser.parse(automata_file)
    assert automata._states == {"q0"}
    assert automata._alphabet == {"a"}
    assert automata._initial == "q0"
    assert automata._final == set()
    assert automata._transitions == {}

def test_parser_weirdautomata():
    def test_parser_states_invalid():
        # Archivo con estado vacío
        current_dir = os.path.dirname(__file__)
        automata_file = os.path.join(current_dir, "ejemplo_estado_invalido.automata")

        parser = AutomataParser()

        # Verificamos que parse() lance la excepción
        with pytest.raises(Exception):
            parser.parse(automata_file)
def test_parser_complejo():
    current_dir = os.path.dirname(__file__)
    automata_file = os.path.join(current_dir, "complejo.automata")

    parser = AutomataParser()
    automata = parser.parse(automata_file)
    assert automata._states == {"q0", "q1", "q2", "q3", "q4", "q5", "q6"}
    assert automata._alphabet == {"a", "b", "c", "d", "0", "1"}
    assert automata._initial == "q0"
    assert automata._final == {"q4", "q5", "q6"}
    assert automata._transitions == {
        ("q0", "a"): "q1",
        ("q2", "0"): "q2",
        ("q3", "c"): "q3",
        ("q0", "b"): "q4",
        ("q2", "1"): "q5"
    }

