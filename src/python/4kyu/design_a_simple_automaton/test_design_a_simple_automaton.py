"""
TEST CASES:


Test.assert_equals(my_automaton.read_commands(["1"]), True)
Test.assert_equals(my_automaton.read_commands(["1", "0", "0", "1"]), True)
"""
import pytest


TEST_CASES = [
    (["0"], False),
    (["1"], True),
    (["0", "0"], False),
    (["0", "1"], True),
    (["1", "0"], False),
    (["1", "1"], True),
    (["1", "0", "0"], True),
    (["1", "0", "1"], True),
    (["1", "1", "0"], False),
    (["1", "1", "1"], True),
    (["1", "0", "0", "1"], True),
]


@pytest.mark.parametrize('test_input, test_output', TEST_CASES)
def test_read_commands(test_input, test_output):
    from design_a_simple_automaton import Automaton
    new_automaton = Automaton()
    assert new_automaton.read_commands(test_input) == test_output
