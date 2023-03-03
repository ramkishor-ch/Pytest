"""
Group Tests:

Pytest provides many inbuilt markers such as xfail, skip and parametrize. 

Apart from that, users can create their own marker names. Markers are applied on the tests using the syntax given below :

@pytest.mark.<markername>

To run the marked tests, we can use the following syntax :

pytest -m <markername> -v

-m <markername> represents the marker name of the tests to be executed.

"""


# test_compare.py

import pytest
@pytest.mark.great
def test_greater():
   num = 100
   assert num > 100

@pytest.mark.great
def test_greater_equal():
   num = 100
   assert num >= 100

@pytest.mark.others
def test_less():
   num = 100
   assert num < 200

   
# test_square.py
import pytest
import math

@pytest.mark.square
def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

@pytest.mark.square
def testsquare():
   num = 7
   assert 7*7 == 40

@pytest.mark.others
def test_equality():
   assert 10 == 11

# Now to run the tests marked as others, run the following command :
#    pytest -m others -v

# See the result below. It ran the 2 tests marked as others.

"""
Output:
test_compare.py::test_less PASSED
test_square.py::test_equality FAILED
============================================== FAILURES==============================================
___________________________________________ test_equality____________________________________________
   @pytest.mark.others
   def test_equality():
>  assert 10 == 11
E  assert 10 == 11
test_square.py:16: AssertionError
========================== 1 failed, 1 passed, 4 deselected in 0.08 seconds==========================
"""