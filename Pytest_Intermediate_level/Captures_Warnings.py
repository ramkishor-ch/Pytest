# How to capture warnings :
# Starting from version 3.1, pytest now automatically catches warnings during test execution and 
# displays them at the end of the session:

# content of test_show_warnings.py
import warnings

def api_v1():
    warnings.warn(UserWarning("api v1, should use functions from v2"))
    return 1

def test_one():
    assert api_v1() == 1

# Running pytest now produces this output:

# $ pytest test_show_warnings.py

    # =========================== test session starts ============================
    # platform linux -- Python 3.x.y, pytest-7.x.y, pluggy-1.x.y
    # rootdir: /home/sweet/project
    # collected 1 item

    # test_show_warnings.py .                                              [100%]

    # ============================= warnings summary =============================
    # test_show_warnings.py::test_one
    # /home/sweet/project/test_show_warnings.py:5: UserWarning: api v1, should use functions from v2
    #     warnings.warn(UserWarning("api v1, should use functions from v2"))

    # -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
    # ======================= 1 passed, 1 warning in 0.12s =======================