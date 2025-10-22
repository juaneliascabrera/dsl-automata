from dsl_automata.parser.parser import AutomataParser
import os
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