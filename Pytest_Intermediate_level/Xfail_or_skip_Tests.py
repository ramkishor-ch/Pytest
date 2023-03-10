"""
Skip and Xfail tests in Pytest:

Situations :
    a. A test is not relevant for some time due to some reasons.
    b. A new feature is being implemented and we already added a test for that feature.

In these situations, we have the option to xfail the test or skip the tests.

Pytest will execute the xfailed test, but it will not be considered as part failed or passed tests. 
Details of these tests will not be printed even if the test fails (remember pytest usually prints the failed test details). 

We can xfail tests using the following marker − @pytest.mark.xfail

Skipping a test means that the test will not be executed. We can skip tests using the following marker − @pytest.mark.skip

"""

import pytest
@pytest.mark.xfail
@pytest.mark.great
def test_greater():
   num = 100
   assert num > 100

@pytest.mark.xfail
@pytest.mark.great
def test_greater_equal():
   num = 100
   assert num >= 100

@pytest.mark.skip
@pytest.mark.others
def test_less():
   num = 100
   assert num < 200

"""
Output:
    test_compare.py::test_greater xfail
    test_compare.py::test_greater_equal XPASS
    test_compare.py::test_less SKIPPED
    ============================ 1 skipped, 1 xfailed, 1 xpassed in 0.06 seconds============================
"""