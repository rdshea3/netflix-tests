#!/usr/bin/env python3

# -------------------------------
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Netflix import netflix_read, netflix_read_cache, netflix_predict, netflix_eval, netflix_print, netflix_solve

# -----------
# TestCollatz
# -----------


class TestNetflix (TestCase):
    # ----
    # read
    # ----

    def test_read_1(self):
        s = StringIO("10005:\n254775\n1892654\n469365\n793736\n926698\n10:\n1952305\n1531863\n")
        i = netflix_read(s)
        j = i.items()
        self.assertEqual(i, {10: [1952305, 1531863], 10005: [254775, 1892654, 469365, 793736, 926698]})

    def test_read_2(self):
        s = StringIO("10010:\n1462925\n52050\n650466\n1813166\n2224061\n815731\n154626\n531384\n696688\n1088633\n639327\n59938\n1856669\n2034703\n1060588\n2475682\n1075860\n1633365\n681503\n186927\n2374977\n2113696\n1677862\n")
        i = netflix_read(s)
        j = i.items()
        self.assertEqual(i, {10010: [1462925, 52050, 650466, 1813166, 2224061, 815731, 154626, 531384, 696688, 1088633, 639327, 59938, 1856669, 2034703, 1060588, 2475682, 1075860, 1633365, 681503, 186927, 2374977, 2113696, 1677862]})

    def test_read_3(self):
        s = StringIO("10037:\n253214\n612895\n769764\n396150\n2555464\n1988133\n560277\n1839686\n2569369\n1845071\n1627613\n948108\n1316833\n911710\n")
        i = netflix_read(s)
        j = i.items()
        self.assertEqual(i, {10037: [253214, 612895, 769764, 396150, 2555464, 1988133, 560277, 1839686, 2569369, 1845071, 1627613, 948108, 1316833, 911710]})

    # ----------
    # read_cache 
    # ----------

    def test_read_cache_1(self):
        t = netflix_read_cache('snm2235-jml4759-actualCustomerRating.pickle')
        self.assertIsInstance(t, dict)

    def test_read_cache_2(self):
        t = netflix_read_cache('snm2235-jml4759-averageCustomerRating.pickle')
        self.assertIsInstance(t, dict)
    
    def test_read_cache_3(self):
        t = netflix_read_cache('snm2235-jml4759-averageMovieRating.pickle')
        self.assertIsInstance(t, dict)

    # -------
    # predict 
    # -------

    def test_predict_1(self):
        dict1 = {1: [1, 2, 3]}
        dict2 = {1: 2}
        dict3 = {1: 4, 2: 3, 3: 5}
        r = netflix_predict(dict1, dict2, dict3)
        self.assertEqual(r, {(3, 1): 3, (1, 1): 2, (2, 1): 1})

    def test_predict_2(self):
        dict1 = {1: [1, 2], 2: [1, 2]}
        dict2 = {1: 2, 2: 4}
        dict3 = {1: 5, 2: 3}
        r = netflix_predict(dict1, dict2, dict3)
        self.assertEqual(r, {(1, 2): 5, (1, 1): 3, (2, 1): 1, (2, 2): 3})

    def test_predict_3(self):
        dict1 = {1: [1], 2: [1], 3: [1]}
        dict2 = {1: 1, 2: 1, 3: 1}
        dict3 = {1: 5}
        r = netflix_predict(dict1, dict2, dict3)
        self.assertEqual(r, {(1, 2): 1, (1, 3): 1, (1, 1): 1})

    # ----
    # eval
    # ----

    def test_eval_1(self):
        a = {(3, 1): 3, (1, 1): 2, (2, 1): 1}
        p = {(3, 1): 3, (1, 1): 2, (2, 1): 1}
        v = netflix_eval(a, p)
        self.assertLessEqual(v, 1)

    def test_eval_2(self):
        a = {(1, 2): 5, (1, 1): 3, (2, 1): 1, (2, 2): 3}
        p = {(1, 2): 4.1, (1, 1): 3, (2, 1): 1.89, (2, 2): 3}
        v = netflix_eval(a, p)
        self.assertLessEqual(v, 1)

    def test_eval_3(self):
        a = {(1, 2): 1, (1, 3): 1, (1, 1): 1}
        p = {(1, 2): 2, (1, 3): 2.25, (1, 1): 0.76}
        v = netflix_eval(a, p)
        self.assertLessEqual(v, 1)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        i = {1: [1, 2, 3]}
        p = {(3, 1): 3, (1, 1): 2, (2, 1): 1}
        r = 0
        netflix_print(i, p, r, w)
        self.assertEqual(w.getvalue(), "1:\n2.0\n1.0\n3.0\nRMSE: 0.00\n")

    def test_print_2(self):
        w = StringIO()
        i = {1: [1, 2], 2: [1, 2]}
        p = {(1, 2): 4.1, (1, 1): 3, (2, 1): 1.89, (2, 2): 3}
        r = 0.63
        netflix_print(i, p, r, w)
        self.assertEqual(w.getvalue(), "1:\n3.0\n1.9\n2:\n4.1\n3.0\nRMSE: 0.63\n")

    def test_print_3(self):
        w = StringIO()
        i = {1: [1], 2: [1], 3: [1]}
        p = {(1, 2): 2, (1, 3): 2.25, (1, 1): 0.76}
        r = 0.93
        netflix_print(i, p, r, w)
        self.assertEqual(w.getvalue(), "1:\n0.8\n2:\n2.0\n3:\n2.2\nRMSE: 0.93\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("10005:\n254775\n1892654\n469365\n793736\n926698\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10005:\n3.5\n4.0\n3.2\n2.9\n3.0\nRMSE: 1.47\n")

    def test_solve_2(self):
        r = StringIO("10010:\n1462925\n52050\n650466\n1813166\n2224061\n815731\n154626\n531384\n696688\n1088633\n639327\n59938\n1856669\n2034703\n1060588\n2475682\n1075860\n1633365\n681503\n186927\n2374977\n2113696\n1677862\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10010:\n2.2\n2.0\n2.1\n2.9\n2.6\n2.2\n2.3\n2.1\n1.7\n2.5\n1.8\n1.8\n2.0\n1.7\n2.8\n2.1\n1.8\n2.6\n1.2\n2.2\n1.6\n1.8\n1.9\nRMSE: 1.19\n")

    def test_solve_3(self):
        r = StringIO("10037:\n253214\n612895\n769764\n396150\n2555464\n1988133\n560277\n1839686\n2569369\n1845071\n1627613\n948108\n1316833\n911710\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10037:\n3.9\n3.0\n3.2\n3.7\n3.6\n3.6\n3.2\n2.7\n3.1\n3.6\n3.0\n3.1\n3.2\n3.3\nRMSE: 0.82\n")

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
