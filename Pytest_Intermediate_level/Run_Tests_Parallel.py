"""
Run tests in parallel

a. install package: pip install pytest-xdist
b. speed up test runs by sending tests to multiple CPU's:
pytest -n NUMCPUS
c. run command: pip install webdriver_manager
d. run the test file: python filename.py -n 3

"""


import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = None


@pytest.fixture
def setup():
   print("Start Browser")
   global driver
   driver = webdriver.Chrome(ChromeDriverManager().install())
   driver.maximize_window()
   yield
   driver.quit()
   print("close browser")


def test_1(setup):
   driver.get("https://www.google.com")
   print("Test 1 executed")


def test_2(setup):
   driver.get("https://www.google.com")
   print("Test 2 executed")


def test_3(setup):
   driver.get("https://www.google.com")
   print("Test 3 executed")