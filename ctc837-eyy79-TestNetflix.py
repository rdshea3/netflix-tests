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

from Netflix import netflix_eval, netflix_solve

# -----------
# TestNetflix
# -----------


class TestNetflix (TestCase):

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1:\n30878\n2647871\n1283744\n2488120\n317050\n1904905\n1989766\n14756\n1027056\n1149588\n1394012\n1406595\n2529547\n1682104\n2625019\n2603381\n1774623\n470861\n712610\n1772839\n1059319\n2380848\n548064\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1:\n3.8\n3.4\n3.9\n4.8\n3.7\n4.1\n3.4\n3.8\n4.2\n3.5\n3.2\n3.6\n4.1\n3.8\n2.6\n3.9\n3.7\n4.7\n4.2\n4.1\n3.1\n4.7\n3.7\nRMSE: 0.77\n")

    def test_solve_2(self):
        r = StringIO("10011:\n1624701\n2646826\n10012:\n2445069\n1483604\n418164\n2491070\n1485175\n1043648\n1913770\n2560523\n2416960\n161063\n56741\n2301550\n1275794\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10011:\n4.6\n4.2\n10012:\n3.2\n4.1\n3.0\n3.1\n3.8\n3.8\n2.4\n3.2\n3.0\n3.3\n3.8\n3.1\n3.1\nRMSE: 0.74\n")

    def test_solve_3(self):
        r = StringIO("10007:\n1204847\n2160216\n248206\n835054\n1064667\n2419805\n2084848\n671106\n2087887\n1340891\n1917538\n2018945\n2520477\n10008:\n1813636\n2048630\n930946\n1492860\n1687570\n1122917\n1885441\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10007:\n2.6\n3.3\n2.4\n2.3\n2.2\n2.9\n2.8\n2.9\n2.6\n3.1\n2.6\n2.6\n2.4\n10008:\n4.7\n3.3\n3.7\n2.6\n4.2\n4.3\n4.1\nRMSE: 0.94\n")

    def test_solve_4(self):
        r = StringIO("10015:\n975179\n829739\n1732761\n2162539\n933118\n467156\n164480\n613439\n1312973\n1769664\n2477285\n484575\n2602717\n1320821\n1236649\n705793\n1395812\n2056853\n770517\n1514136\n988835\n1172474\n1213571\n1801332\n1623337\n588400\n2378764\n2405069\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10015:\n3.8\n3.2\n3.2\n3.5\n3.8\n3.9\n4.2\n3.9\n4.1\n3.6\n3.8\n3.7\n3.6\n4.2\n4.2\n3.5\n3.7\n4.1\n3.9\n4.1\n5.3\n4.2\n4.4\n2.9\n3.1\n3.3\n4.2\n3.7\nRMSE: 0.85\n")

    def test_solve_5(self):
        r = StringIO("1002:\n2174660\n1685301\n2030264\n1419286\n2520929\n2035568\n1288929\n1680156\n1858104\n988266\n2633719\n156594\n1384253\n1417842\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1002:\n3.2\n3.0\n3.5\n3.4\n3.2\n3.7\n3.8\n2.4\n3.4\n3.4\n4.1\n3.6\n3.4\n2.9\nRMSE: 0.99\n")

    def test_solve_6(self):
        r = StringIO("10021:\n2366406\n1033592\n249998\n1205724\n10022:\n510391\n268014\n2511719\n661571\n1824779\n2178013\n2104013\n1829777\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10021:\n2.2\n2.5\n2.5\n2.1\n10022:\n2.3\n3.3\n3.0\n2.7\n3.5\n3.5\n2.5\n2.8\nRMSE: 0.79\n")







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
