from dsl_automata.parser.parser import AutomataParser
from dsl_automata.logic.dfa import DFA
from dsl_automata.logic.exceptions import AutomataError
from dsl_automata.logic.errors import *
import os
import pytest
def test_dfa_simple_accept_expected_words():
    current_dir = os.path.dirname(__file__)
    automata_file = os.path.join(current_dir, "automata_dfa_files/simple_dfa.automata")
    parser = AutomataParser()
    dfa = parser.parse(automata_file)
    should_accept = [
        "a",
        "aba",
        "ababa"
    ]
    for word in should_accept:
        assert dfa.accepts(word)
    should_reject = [
        "b",
        "ab",
        "",
        "ababab"
    ]
    for word in should_reject:
        assert not dfa.accepts(word)
def test_complex_dfa_accept_expected_words():
    """Automaton that accepts strings with even 0's"""
    current_dir = os.path.dirname(__file__)
    automata_file = os.path.join(current_dir, "automata_dfa_files/complex_dfa.automata")
    parser = AutomataParser()
    dfa = parser.parse(automata_file)

    should_accept = [
        "1",
        "100",
        "100100",
        "1001001000000",
        "00000011001100"
    ]
    should_reject = [
        "01",
        "0100",
        "0100100",
        "10010001000000",
        "0000011001100"
    ]
    for word in should_accept:
        assert dfa.accepts(word)
    for word in should_reject:
        assert not dfa.accepts(word)
def test_nondeterminism():
    current_dir = os.path.dirname(__file__)
    automata_file = os.path.join(current_dir, "automata_dfa_files/nondeterministic.automata")
    parser = AutomataParser()

    with pytest.raises(AutomataError) as excinfo:
        dfa = parser.parse(automata_file)
    assert str(excinfo.value) == ERROR_AUTOMATA_IS_NOT_DETERMINISTIC.format(state="q0", symbol = "a", destinations = "{'q0', 'q1'}")

    pass