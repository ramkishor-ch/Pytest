"""

@pytest.mark.parametrize allows one to define multiple sets of arguments and fixtures at the test function or class.


"""


import pytest

@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


"""
    ================================= FAILURES =================================
    ____________________________ test_eval[6*9-42] _____________________________

    test_input = '6*9', expected = 42

        @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
        def test_eval(test_input, expected):
    >       assert eval(test_input) == expected
    E       AssertionError: assert 54 == 42
    E        +  where 54 = eval('6*9')

    test_expectation.py:6: AssertionError

"""