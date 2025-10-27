from dsl_automata.parser.parser import AutomataParser
from dsl_automata.logic.errors import *
from dsl_automata.logic.exceptions import AutomataError
import os
import pytest
def test_parser_basico():
    current_dir = os.path.dirname(__file__)
    automata_file = os.path.join(current_dir, "automata_parser_files/test.automata")

    parser = AutomataParser()
    automata = parser.parse(automata_file)

    assert automata._states == {"q0", "q1"}
    assert automata._alphabet == {"a", "b"}
    assert automata._initial == "q0"
    assert automata._finals == {"q1"}
    assert automata._transitions == {
        ("q0", "a"): {"q1"},
        ("q1", "b"): {"q0"}
    }
def test_parser_basico2():
    current_dir = os.path.dirname(__file__)
    automata_file = os.path.join(current_dir, "automata_parser_files/test2.automata")
    parser = AutomataParser()
    automata = parser.parse(automata_file)
    assert automata._states == {"q0"}
    assert automata._alphabet == {"a"}
    assert automata._initial == "q0"
    assert automata._finals == set()
    assert automata._transitions == {}

def test_parser_weirdautomata():
    # Archivo con estado vacío
    current_dir = os.path.dirname(__file__)
    automata_file = os.path.join(current_dir, "automata_parser_files/invalid.automata")

    parser = AutomataParser()

    # Verificamos que parse() lance la excepción
    with pytest.raises(Exception):
        parser.parse(automata_file)
def test_parser_complejo():
    current_dir = os.path.dirname(__file__)
    automata_file = os.path.join(current_dir, "automata_parser_files/complejo.automata")

    parser = AutomataParser()
    automata = parser.parse(automata_file)
    assert automata._states == {"q0", "q1", "q2", "q3", "q4", "q5", "q6"}
    assert automata._alphabet == {"a", "b", "c", "d", "0", "1"}
    assert automata._initial == "q0"
    assert automata._finals == {"q4", "q5", "q6"}
    assert automata._transitions == {
        ("q0", "a"): {"q1"},
        ("q2", "0"): {"q2"},
        ("q3", "c"): {"q3"},
        ("q0", "b"): {"q4"},
        ("q2", "1"): {"q5"}
    }
def test_parser_invalid_automata():
    current_dir = os.path.dirname(__file__)
    automata_file = os.path.join(current_dir, "automata_parser_files/invalid2.automata")
    parser = AutomataParser()
    #This example has an initial q2 that is not in the states set.
    with pytest.raises(AutomataError) as excinfo:
        parser.parse(automata_file)
    assert str(excinfo.value) == ERROR_INITIAL_NOT_IN_STATES.format(state="q2")
def test_parser_invalid_automata2():
    current_dir = os.path.dirname(__file__)
    automata_file = os.path.join(current_dir, "automata_parser_files/invalid3.automata")
    parser = AutomataParser()
    #This example has a final q3 that is not in the states set.
    with pytest.raises(Exception) as excinfo:
        parser.parse(automata_file)
    assert str(excinfo.value) == ERROR_FINAL_NOT_IN_STATES.format(state="q3")

def test_parser_invalid_automata3():
    current_dir = os.path.dirname(__file__)
    automata_file = os.path.join(current_dir, "automata_parser_files/invalidtransition.automata")
    parser = AutomataParser()
    #This example has a state q2 in a transition that is not in the states set.
    with pytest.raises(Exception) as excinfo:
        parser.parse(automata_file)
    assert str(excinfo.value) == ERROR_UNKNOWN_TRANSITION_TARGET.format(target="q2")

def test_parser_invalid_automata4():
    current_dir = os.path.dirname(__file__)
    automata_file = os.path.join(current_dir, "automata_parser_files/invalidtransition2.automata")
    parser = AutomataParser()
    #This example has a state q2 in a transition that is not in the states set.
    with pytest.raises(Exception) as excinfo:
        parser.parse(automata_file)
    assert str(excinfo.value) == ERROR_UNKNOWN_TRANSITION_STATE.format(state="q2")

def test_parser_invalid_automata5():
    current_dir = os.path.dirname(__file__)
    automata_file = os.path.join(current_dir, "automata_parser_files/invalidtransition3.automata")
    parser = AutomataParser()
    #This example has a transition with an character that is not in the alphabet set.
    with pytest.raises(Exception) as excinfo:
        parser.parse(automata_file)
    assert str(excinfo.value) == ERROR_SYMBOL_NOT_IN_ALPHABET.format(symbol="c")