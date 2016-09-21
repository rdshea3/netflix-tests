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

from io import StringIO
from unittest import main, TestCase
import sys
import Netflix
from Netflix import *

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    "class to test collatz functionality"
    # ----
    # read
    # ----

    def test_loadCache1(self):
        "testing the read functionality"
        load_caches()
        self.assertEqual(Netflix.meanCache["movies"][1]["mean"],3.56)
    def test_loadCache2(self):
        "testing the read functionality"
        load_caches()
        self.assertEqual(Netflix.differenceCache["6"],-.26)
    def test_loadCache3(self):
        "testing the read functionality"
        load_caches()
        self.assertEqual(Netflix.actualCache[(30878,1)],4)

    def test_parse1(self):
        w = StringIO()
        self.assertIsInstance(netflix_parse([30878],1,w),float)
    def test_parse2(self):
        w = StringIO()
        self.assertIsInstance(netflix_parse([1952305,1531863],10,w),float)
    def test_parse3(self):
        w = StringIO()
        self.assertIsInstance(netflix_parse([2326571,977808],1000,w),float )

    def test_eval1(self):
        load_caches()
        result = netflix_eval(30878,1)
        self.assertIsInstance(result,float)
        self.assertLessEqual(result,5)
        self.assertGreaterEqual(result,1)
    def test_eval2(self):
        load_caches()
        result = netflix_eval(1531863,10)
        self.assertIsInstance(result,float)
        self.assertLessEqual(result,5)
        self.assertGreaterEqual(result,1)
    def test_eval3(self):
        load_caches()
        result = netflix_eval(977808,1000)
        self.assertIsInstance(result,float )
        self.assertLessEqual(result,5)
        self.assertGreaterEqual(result,1)
    def test_eval4(self):
        load_caches()
        result = netflix_eval(14756,1)
        self.assertIsInstance(result,float)
        self.assertLessEqual(result,5)
        self.assertGreaterEqual(result,1)
    def test_eval5(self):
        load_caches()
        result = netflix_eval(1772839,1)
        self.assertIsInstance(result,float)
        self.assertLessEqual(result,5)
        self.assertGreaterEqual(result,1)
    def test_eval6(self):
        load_caches()
        result = netflix_eval(2380848,1)
        self.assertIsInstance(result,float)
        self.assertLessEqual(result,5)
        self.assertGreaterEqual(result,1)

    def test_write1(self):
        w = StringIO()
        netflix_write(w,"")
        self.assertEqual(w.getvalue(),"\n")

    def test_write2(self):
        w = StringIO()
        netflix_write(w,""+str(4))
        self.assertEqual(w.getvalue(),"4\n")

    def test_write3(self):
        w = StringIO()
        netflix_write(w,"4.3")
        self.assertEqual(w.getvalue(),"4.3\n")

    def test_solve(self):
        r = StringIO("1:\n30878\n10:\n1952305\n")
        w = StringIO()
        netflix_solve(r,w)
        lines = w.getvalue().split("\n")
        self.assertGreater(1.0,float(lines[len(lines)-2]))
    # -----
    # solve
    # -----

    # def test_solve1(self):
    #     r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
    #     w = StringIO()
    #     collatz_solve(r, w)
    #     self.assertEqual(
    #         w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
    # def test_solve2(self):
    #     r = StringIO("10 1\n200 100\n210 201\n1000 900\n")
    #     w = StringIO()
    #     collatz_solve(r, w)
    #     self.assertEqual(
    #         w.getvalue(), "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



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