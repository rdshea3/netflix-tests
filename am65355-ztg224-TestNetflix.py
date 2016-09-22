#!/usr/bin/env python3.5

# ---------------------------
# Copyright (C) 2016
# Alan Ma
# Zachary Gilkerson
# ---------------------------

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase
from Netflix import netflix_eval, netflix_solve
import requests
import pickle

# -----------
# TestNetflix
# -----------

user_movie_rating = pickle.loads(requests.get('http://www.cs.utexas.edu/users/fares/netflix-caches/snm2235-jml4759-actualCustomerRating.pickle').content)
avg_movie_rating = pickle.loads(requests.get('http://www.cs.utexas.edu/users/fares/netflix-caches/snm2235-jml4759-averageMovieRating.pickle').content)
avg_user_rating = pickle.loads(requests.get('http://www.cs.utexas.edu/users/fares/netflix-caches/snm2235-jml4759-averageCustomerRating.pickle').content)

class TestNetflix (TestCase):
    # ----
    # eval
    # ----

    def test_eval_1(self):
        u = 716091
        m = 2043
        v = netflix_eval(u, m)
        self.assertEqual(v, "3.5")

    def test_eval_2(self):
        u = 40391
        m = 6470
        v = netflix_eval(u, m)
        self.assertEqual(v, "2.1")

    def test_eval_3(self):
        u = 116
        m = 6470
        v = netflix_eval(u, m)
        self.assertEqual(v, "3.6")

    def test_eval_4(self):
        u = 73821
        m = 1823
        v = netflix_eval(u, m)
        self.assertEqual(v, "3.2")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("10:\n1952305")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10:\n2.9\nRMSE: 0.10")

    def test_solve_2(self):
        r = StringIO("10:\n1952305\n1531863\n1000:\n2326571\n977808\n1010534")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10:\n2.9\n2.6\n1000:\n3.2\n2.9\n2.6\nRMSE: 0.34")


    def test_solve_3(self):
        r = StringIO("10037:\n253214\n612895\n769764\n396150\n2555464\n1988133\n560277\n1839686\n2569369\n1845071\n1627613\n948108\n1316833\n911710\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10037:\n3.9\n3.0\n3.2\n3.7\n3.6\n3.6\n3.2\n2.7\n3.1\n3.6\n3.0\n3.1\n3.2\n3.2\nRMSE: 0.82")

    def test_solve_4(self):
        r = StringIO("6905:\n246618\n1305872\n345476\n5427:\n129710")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(
            w.getvalue(), "6905:\n3.8\n3.2\n2.4\n5427:\n2.7\nRMSE: 1.18")


# ----
# main
# ----

if __name__ == "__main__":
    main()
