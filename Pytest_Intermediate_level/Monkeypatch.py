# Monkey Patch :
# Modifying the behavior of a function or the property of a class for a test 
# e.g. there is an API call or database connection you will not make for a test but you know what the expected output should be. 

# Functions:
# monkeypatch.setattr : to patch the function or property with your desired testing behavior.

# In the context of testing, you do not want your test to depend on the running user.
# monkeypatch can be used to patch functions dependent on the user to always return a specific value.

# Example: monkeypatch.setattr is used to patch Path.home so that the known testing path Path("/abc") is always used the test is run. 
# This removes any dependency on the running user for testing purposes. 
# monkeypatch.setattr must be called before the function which will use the patched function is called. 
# After the test function finishes the Path.home modification will be undone.

# contents of test_module.py with source code and the test
from pathlib import Path

def getssh():
    """Simple function to return expanded homedir ssh path."""
    return Path.home() / ".ssh"

def test_getssh(monkeypatch):
    # mocked return function to replace Path.home
    # always return '/abc'
    def mockreturn():
        return Path("/abc")

    # Application of the monkeypatch to replace Path.home with the behavior of mockreturn defined above.
    monkeypatch.setattr(Path, "home", mockreturn)

    # Calling getssh() will use mockreturn in place of Path.home for this test with the monkeypatch.
    x = getssh()
    assert x == Path("/abc/.ssh")
