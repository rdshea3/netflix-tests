#!/usr/bin/env python3

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Netflix import netflix_read, netflix_eval, netflix_print, netflix_solve, read_caches, LineType

# -----------
# TestNetflix
# -----------


class TestNetflix (TestCase):
    # ----
    # read
    # ----

    def test_read_1(self):
        s = "111111:"
        line_type, name = netflix_read(s)
        self.assertEqual(line_type,  LineType.movie)
        self.assertEqual(name, 111111)

    def test_read_2(self):
        s = "111111"
        line_type, name = netflix_read(s)
        self.assertEqual(line_type, LineType.user)
        self.assertEqual(name,  111111)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        movie_map = {1: 3.7}
        user_map = {111: 3.7}
        rating = netflix_eval(1, 111, movie_map, user_map)
        self.assertEqual(round(rating, 1), 3.7)

    def test_eval_2(self):
        movie_map = {1: 5.0}
        user_map = {111: 5.0}
        rating = netflix_eval(1, 111, movie_map, user_map)
        self.assertEqual(round(rating, 1), 5.0)

    def test_eval_3(self):
        movie_map = {1: 1}
        user_map = {111: 1}
        rating = netflix_eval(1, 111, movie_map, user_map)
        self.assertEqual(round(rating, 1), 1.0)

    def test_eval_4(self):
        movie_map = {1: 4.0}
        user_map = {111: 4.0}
        rating = netflix_eval(1, 111, movie_map, user_map)
        self.assertEqual(round(rating, 1), 4.3)

    def test_eval_5(self):
        movie_map = {1: 3.0}
        user_map = {111: 3.0}
        rating = netflix_eval(1, 111, movie_map, user_map)
        self.assertEqual(round(rating, 1), 2.3)

    def test_eval_6(self):
        movie_map = {1: 4.0}
        user_map = {111: 3.4}
        rating = netflix_eval(1, 111, movie_map, user_map)
        self.assertEqual(round(rating, 1), 3.7)
    # ----
    # read_caches
    # ----

    def test_read_caches_1(self):
        movie_map, _, _ = read_caches()
        self.assertEqual(movie_map[16058], 2.487)

    def test_read_caches_2(self):
        _, user_map, _ = read_caches()
        self.assertEqual(user_map[2630799], 3.188)

    def test_read_caches_3(self):
        _, _, rmse_cache = read_caches()
        self.assertEqual(rmse_cache[(46846, 9939)], 3)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        netflix_print(w, LineType.movie, 111)
        self.assertEqual(w.getvalue(), "111:\n")

    def test_print_2(self):
        w = StringIO()
        netflix_print(w, LineType.user, 4.31)
        self.assertEqual(w.getvalue(), "4.3\n")

    def test_print_3(self):
        w = StringIO()
        netflix_print(w, LineType, 4.311111)
        self.assertEqual(w.getvalue(), "4.3\n")

    # -----
    # solve
    # -----
    def test_solve_1(self):
        r = StringIO("1:\n30878\n2647871")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1:\n3.7\n3.3\nRMSE: 0.54\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
