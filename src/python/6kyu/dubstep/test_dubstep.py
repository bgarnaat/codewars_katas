import pytest
"""
TEST CASES:


Test.assert_equals(song_decoder("AWUBBWUBC"), "A B C","WUB should be replaced by 1 space")
Test.assert_equals(song_decoder("AWUBWUBWUBBWUBWUBWUBC"), "A B C","multiples WUB should be replaced by only 1 space")
Test.assert_equals(song_decoder("WUBAWUBBWUBCWUB"), "A B C","heading or trailing spaces should be removed")
"""


TEST_CASES = [
    ("AWUBBWUBC", "A B C"),
    ("AWUBWUBWUBBWUBWUBWUBC", "A B C"),
    ("WUBAWUBBWUBCWUB", "A B C"),
]


@pytest.mark.parametrize('test_input, test_output', TEST_CASES)
def test_song_decoder(test_input, test_output):
    from dubstep import song_decoder
    assert song_decoder(test_input) == test_output
