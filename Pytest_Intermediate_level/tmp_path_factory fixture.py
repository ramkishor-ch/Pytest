# The tmp_path_factory is a session-scoped fixture which can be used to create arbitrary temporary directories 
# from any other fixture or test.

# Example: suppose your test suite needs a large image on disk, which is generated procedurally. 
# Instead of computing the same image for each test that uses it into its own tmp_path, 
# you can generate it once per-session to save time:

# contents of conftest.py
import pytest


@pytest.fixture(scope="session")
def image_file(tmp_path_factory):
    img = compute_expensive_image()
    fn = tmp_path_factory.mktemp("data") / "img.png"
    img.save(fn)
    return fn


# contents of test_image.py
def test_histogram(image_file):
    img = load_image(image_file)
    # compute and test histogram

# tmpdir()
# Return a temporary directory path object which is unique to each test function invocation, 
# created as a sub directory of the base temporary directory.
# By default, a new base temporary directory is created each test session, and old bases are removed after 3 sessions