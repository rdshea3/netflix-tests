#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestNetflix.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

import Netflix

# -----------
# TestCollatz
# -----------


class TestNetflix(TestCase):

    def setUp(self):
        Netflix.mean_user_ratings = {0: 3.0, 1: 4.0}
        Netflix.mean_movie_ratings = {0: 2.0}

    # ----
    # eval
    # ----

    def test_eval_1(self):
        Netflix.current_movie = 0
        v = Netflix.netflix_eval(0)
        self.assertEqual(round(v, 2), 1.3)

    def test_eval_2(self):
        Netflix.current_movie = 0
        v = Netflix.netflix_eval(1)
        self.assertEqual(v, 2.3)

    def test_eval_3(self):
        Netflix.current_movie = 0
        v = Netflix.netflix_eval(2)
        self.assertEqual(v, 2)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        Netflix.netflix_print(w, '')
        self.assertEqual(w.getvalue(), "\n")

    def test_print_2(self):
        w = StringIO()
        Netflix.netflix_print(w, 'abcdefg')
        self.assertEqual(w.getvalue(), "abcdefg\n")

    def test_print_3(self):
        w = StringIO()
        Netflix.netflix_print(w, '\n')
        self.assertEqual(w.getvalue(), "\n\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("0:\n0\n")
        w = StringIO()
        Netflix.netflix_solve(r, w, False)
        self.assertEqual(
            w.getvalue(), "0:\n1.2999999999999998\n")

    def test_solve_2(self):
        r = StringIO("0:\n1\n")
        w = StringIO()
        Netflix.netflix_solve(r, w, False)
        self.assertEqual(
            w.getvalue(), "0:\n2.3\n")

    def test_solve_3(self):
        r = StringIO("0:\n2\n")
        w = StringIO()
        Netflix.netflix_solve(r, w, False)
        self.assertEqual(
            w.getvalue(), "0:\n2.0\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage3 run --branch TestNetflix.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""
