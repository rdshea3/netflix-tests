#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Netflix import rmse_numpy, netflix_process, netflix_eval 

# -----------
# TestCollatz
# -----------

class TestNetflix (TestCase) :
    # ----------
    # rmse_numpy
    # ----------

    def test_rmse_numpy1(self) :
        self.assertEqual(rmse_numpy((2, 3, 4), (3, 2, 5)), 1)

    def test_rmse_numpy2(self) :
        self.assertEqual(rmse_numpy((2, 3, 4), (4, 1, 6)), 2)

    def test_rmse_numpy3(self) :
        self.assertEqual(rmse_numpy((2, 3, 4), (4, 3, 2)), 1.632993161855452)
  
    # ---------------
    # netflix_process
    # ---------------

    def test_netflix_process1(self):
        s = StringIO("1:\n30878\n")
        w = StringIO()
        for line in s:
            netflix_process(line, w)
        self.assertEqual(w.getvalue(), "1:\n3.8\n")


    def test_netflix_process2(self):
        s = StringIO("1:\n30878\n10:\n1952305\n")
        w = StringIO()
        for line in s:
            netflix_process(line, w)
        self.assertEqual(w.getvalue(), "1:\n3.8\n10:\n2.9\n")


    def test_netflix_process3(self):
        s = StringIO("1:\n30878\n10:\n1952305\n1531863\n")
        w = StringIO()
        for line in s:
            netflix_process(line, w)
        self.assertEqual(w.getvalue(), "1:\n3.8\n10:\n2.9\n2.8\n")

    def test_netflix_eval1(self):
        s = StringIO("10:\n1952305\n");
        w = StringIO();
        netflix_eval(s,w)
        self.assertEqual(w.getvalue(), "10:\n2.9\nRMSE: 0.10\n")

    def test_netflix_eval2(self):
        s = StringIO("1000:\n2326571\n977808\n1010534\n");
        w = StringIO();
        netflix_eval(s,w)
        self.assertEqual(w.getvalue(), "1000:\n3.4\n2.9\n2.8\nRMSE: 0.45\n")

    def test_netflix_eval3(self):
        s = StringIO("10:\n1952305\n1531863\n1000:\n2326571\n977808\n");
        w = StringIO();
        netflix_eval(s,w)
        self.assertEqual(w.getvalue(), "10:\n2.9\n2.8\n1000:\n3.4\n2.9\nRMSE: 0.36\n")
# ----
# main
# ----

if __name__ == "__main__" :
    main()

