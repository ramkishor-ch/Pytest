"""
Usage:

The plugin provides two command line options to rerun failures from the last pytest invocation:

--lf, --last-failed - to only re-run the failures.

--ff, --failed-first - to run the failures first and then the rest of the tests.

For cleanup (usually not needed), a --cache-clear option allows to remove all cross-session cache contents ahead of a test run.

"""

import pytest

@pytest.mark.parametrize("i", range(50))
def test_num(i):
    if i in (17, 25):
        pytest.fail("bad luck")

"""
run command: pytest -q
test will fail for 17 and 25

run command: pytest -lf
run-last-failure: rerun previous 2 failures

run command: pytest -ff
run-last-failure: rerun previous 2 failures

run command: pytest --nf
New --nf, --new-first options: 
run new tests first followed by the rest of the tests, in both cases tests are also sorted by the file modified time, 
with more recent files coming first.

run command: pytest --cache-show
You can always peek at the content of the cache using the --cache-show 

run command: pytest --cache-clear
clear all cache files and values by adding the --cache-clear option like this

"""