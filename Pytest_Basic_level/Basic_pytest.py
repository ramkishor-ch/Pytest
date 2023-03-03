# Pytest:
# Pytest is a python based testing framework, which is used to write and execute test codes. 
# In the present days of REST services, pytest is mainly used for API testing even though we can use pytest to write simple to complex tests, 
# i.e., we can write codes to test API, database, UI, etc.

# Advantages of Pytest:
# a. Pytest is free and open source.
# b. Because of its simple syntax, pytest is very easy to start with.
# c. Pytest can run multiple tests in parallel, which reduces the execution time of the test suite.
# d. Pytest allows us to run a subset of the entire test suite.
# e. Pytest has its own way to detect the test file and test functions automatically, if not mentioned explicitly.
# f. Pytest allows us to skip a subset of the tests during execution.

# https://docs.pytest.org/en/7.2.x/getting-started.html#get-started

# Basics of Pytest:
# Install pytest: pytest requires: Python 3.7+ or PyPy3.

# Run the following command in your command line: pip install -U pytest

# Check that you installed the correct version: $ pytest --version
# pytest 7.2.1

# display help section of pytest : pytest -h




# 1. Create your first test:
    # Create a new file called test_sample.py, containing a function, and a test:

# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

# Run:
# pytest
#   or
# pytest <filename.py> -v #verbose

# Finished:
    #After it finishes, pytest then shows a failure report because func(3) does not return 5.

# Assert:
    #The assert keyword is used when debugging code.
    #The assert keyword lets you test if a condition in your code returns True, 
    #if not, the program will raise an AssertionError.
    #You can write a message to be written if the code returns False, check the example below.

#Write a message if the condition is False:
x = "hello"

#if condition returns True, then nothing happens:
assert x == "hello"

#if condition returns False, AssertionError is raised:
assert x == "goodbye", "x should be 'hello'"






# 2. Run multiple tests
    #pytest will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories.

# Assert that a certain exception is raised:
# Use the raises helper to assert that some code raises an exception:

# content of test_sysexit.py
import pytest

def f():
    raise SystemExit(1)		#raise allows you to throw an exception at any time.

def test_mytest():
    with pytest.raises(SystemExit):		#https://docs.pytest.org/en/7.2.x/reference/reference.html#pytest.raises
        f()

# Execute the test function with “quiet” reporting mode:
# $ pytest -q test_sysexit.py






# 3. Group multiple tests in a class :
# Once you develop multiple tests, you may want to group them into a class. 
# pytest makes it easy to create a class containing more than one test:

# content of test_class.py
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x	#passed

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")	#failed


# pytest -q test_class.py

# Where:   -q/--quiet flag keeps the output brief

# Python hasattr() function is an inbuilt utility function, 
# which is used to check if an object has the given named attribute and return true if present, else false.


# Poor Practice of test cases:
# Something to be aware of when grouping tests inside classes is that each test has a unique instance of the class. 
# Having each test share the same class instance would be very detrimental to test isolation and would promote poor 
# test practices. This is outlined below:

# content of test_class_demo.py
class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 1


# $ pytest -k TestClassDemoInstance -q

# Where:
# -k <substring> represents the substring to search for in the test names.
# -q  -q/--quiet flag keeps the output brief




# 4. Request a unique temporary directory for functional tests:
# content of test_tmp_path.py
def test_needsfiles(tmp_path):
    print(tmp_path)
    assert 0

# $ pytest -q test_tmp_path.py

# Where:
# assert 0 means assert(0) or assert(false) is usually used to mark unreachable code, 
# so that in debug mode a diagnostic message is emitted and the program is aborted when the supposedly unreachable is actually reached, 
# which is a clear signal that the program isn't doing what we think it is.


# List the name tmp_path in the test function signature and pytest will lookup and call a fixture factory 
# to create the resource before performing the test function call. Before the test runs, 
# pytest creates a unique-per-test-invocation temporary directory:



# Pytest-Fixtures:
# Fixtures are functions, which will run before each test function to which it is applied. 
# Fixtures are used to feed some data to the tests such as database connections, 

import pytest
@pytest.fixture
def tmp_path():
   input = PosixPath('PYTEST_TMPDIR/test_needsfiles0')
   return input

def test_needsfiles(tmp_path):
    print(tmp_path)
    assert 0