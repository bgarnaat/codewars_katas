"""
TEST CASES:


Test.describe("Basic tests")
col_arr = [["6B8E23", "9ACD32","2E8B57","00008B", "00FF00","6B8E23","00FA9A"],
["CD5C5C", "8B0000", "FF0000", "F08080", "98FB98", "DC143C"],
["00BFFF", "00008B", "B22222", "000080", "87CEEB", "4169E1"]]
Test.assert_equals(get_colors(col_arr),"Green+Blue,Red+Green,Blue+Red")

col_arr = [["FF0000", "191970", "FF0000"],
["556B2F", "98FB98", "2E8B57", "00FF7F", "556B2F", "FFA07A"],
["00BFFF", "00BFFF", "4169E1", "1E90FF", "F08080", "191970"]]
Test.assert_equals(get_colors(col_arr),"Red+Blue,Green+Red,Blue+Red")

col_arr = [["FF0000", "8DC4DE", "87CEFA", "4169E1", "0000FF"],
["FF0000", "191970", "00008B"],
["CD5C5C", "F08080", "0000FF"]]
Test.assert_equals(get_colors(col_arr),"Blue+Red,Blue+Red,Red+Blue")
"""
import pytest


GET_COLORS_TEST_CASES = [
    (
        [
            ["6B8E23", "9ACD32", "2E8B57", "00008B", "00FF00", "6B8E23", "00FA9A"],
            ["CD5C5C", "8B0000", "FF0000", "F08080", "98FB98", "DC143C"],
            ["00BFFF", "00008B", "B22222", "000080", "87CEEB", "4169E1"]
        ],
        "Green+Blue,Red+Green,Blue+Red"),
    (
        [
            ["FF0000", "191970", "FF0000"],
            ["556B2F", "98FB98", "2E8B57", "00FF7F", "556B2F", "FFA07A"],
            ["00BFFF", "00BFFF", "4169E1", "1E90FF", "F08080", "191970"]
        ],
        "Red+Blue,Green+Red,Blue+Red"),
    (
        [
            ["FF0000", "8DC4DE", "87CEFA", "4169E1", "0000FF"],
            ["FF0000", "191970", "00008B"],
            ["CD5C5C", "F08080", "0000FF"]
        ],
        "Blue+Red,Blue+Red,Red+Blue"),
]


COLORIZER_TEST_CASES = [
    ("FF0000", "Red"),
    ("00FF00", "Green"),
    ("0000FF", "Blue"),
    ("FFFEFE", "Red"),
]


@pytest.mark.parametrize('test_input, test_output', GET_COLORS_TEST_CASES)
def test_get_colors(test_input, test_output):
    from arrays_and_hex_color_codes import get_colors
    assert get_colors(test_input) == test_output


@pytest.mark.parametrize('test_input, test_output', COLORIZER_TEST_CASES)
def test_colorizer(test_input, test_output):
    from arrays_and_hex_color_codes import _colorizer
    assert _colorizer(test_input) == test_output
