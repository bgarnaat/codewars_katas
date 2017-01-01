import pytest
"""
TEST CASES:


test.assert_equals(greet(spoken, "Hello"), "Hello.")
test.assert_equals(greet(shouted, "Hello"), "HELLO!")
test.assert_equals(greet(whispered, "Hello"), "hello.")

test.assert_equals(greet(spoken, "Bye"), "Bye.")
test.assert_equals(greet(shouted, "Au revoir"), "AU REVOIR!")
test.assert_equals(greet(whispered, "Good day"), "good day.")
"""


from lambda_open_close import spoken, shouted, whispered

TEST_LIST = [
    [(spoken, "Hello"), "Hello."],
    [(shouted, "Hello"), "HELLO!"],
    [(whispered, "Hello"), "hello."],

    [(spoken, "Bye"), "Bye."],
    [(shouted, "Au revoir"), "AU REVOIR!"],
    [(whispered, "Good day"), "good day."],
]


@pytest.mark.parametrize('input, output', TEST_LIST)
def test_lambdas(input, output):
    from lambda_open_close import greet
    assert greet(input[0], input[1]) == output
