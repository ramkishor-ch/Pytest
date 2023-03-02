"""
Stop Test Suite after N Test Failures:
  
In a real scenario, once a new version of the code is ready to deploy, it is first deployed into pre-prod/ staging environment. 
Then a test suite runs on it.

The code is qualified for deploying to production only if the test suite passes. 
If there is test failure, whether it is one or many, the code is not production ready.

Therefore, what if we want to stop the execution of test suite soon after n number of test fails. 
This can be done in pytest using maxfail.

"""

# The syntax to stop the execution of test suite soon after n number of test fails is as follows
# pytest --maxfail = <num>

import pytest
import math

def test_sqrt_failure():
   num = 25
   assert math.sqrt(num) == 6

def test_square_failure():
   num = 7
   assert 7*7 == 40

def test_equality_failure():
   assert 10 == 11

"""
pytest test_failure.py -v --maxfail 1

we can see the execution is stopped on one failure.

Output:

test_failure.py::test_sqrt_failure FAILED
=================================== FAILURES=================================== 
_______________________________________test_sqrt_failure __________________________________________
   def test_sqrt_failure():
   num = 25
>  assert math.sqrt(num) == 6
E  assert 5.0 == 6
E  + where 5.0 = <built-in function sqrt>(25)
E  + where <built-in function sqrt>= math.sqrt
test_failure.py:6: AssertionError
=============================== 1 failed in 0.04 seconds===============================
"""