# How to run doctests
# By default, all files matching the test*.txt pattern will be run through the python standard doctest module. 

# You can change the pattern by issuing:
# pytest --doctest-glob="*.rst"

# If you then have a text file like this:

# content of test_example.txt
    # hello this is a doctest
    # >>> x = 3
    # >>> x
    # 3

#then you can just invoke pytest directly:

# Output:
    # $ pytest
    # =========================== test session starts ============================
    # platform linux -- Python 3.x.y, pytest-7.x.y, pluggy-1.x.y
    # rootdir: /home/sweet/project
    # collected 1 item

    # test_example.txt .                                                   [100%]
    # ============================ 1 passed in 0.12s =============================

# By default, pytest will collect test*.txt files looking for doctest directives, 
# but you can pass additional globs using the --doctest-glob option (multi-allowed).
