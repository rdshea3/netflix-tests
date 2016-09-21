#!/usr/bin/env python3


# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase
from Netflix import netflix_print, netflix_solve, netflix_rmse, netflix_get_cache, netflix_get_actual_ratings, netflix_eval
# -----------
# TestNetflix
# -----------


class TestNetflix (TestCase):

    # ----
    # eval
    # ----

    def test_eval_1(self):
        movie_id = 1130
        customer_id = [630317]
        customer_cache = netflix_get_cache('snm2235-jml4759-averageCustomerRating')
        movie_cache = netflix_get_cache('snm2235-jml4759-averageMovieRating')
        ratings = netflix_eval(movie_id, customer_id, movie_cache, customer_cache)
        self.assertEqual(ratings[0], round(3.7 - 0.312 + 0.133, 1))

    def test_eval_2(self):
        movie_id = 1130
        customer_id = [630317, 630317]
        customer_cache = netflix_get_cache('snm2235-jml4759-averageCustomerRating')
        movie_cache = netflix_get_cache('snm2235-jml4759-averageMovieRating')
        ratings = netflix_eval(movie_id, customer_id, movie_cache, customer_cache)
        self.assertEqual(len(ratings), 2)

    def test_eval_3(self):
        movie_id = 1130
        customer_id = []
        customer_cache = netflix_get_cache('snm2235-jml4759-averageCustomerRating')
        movie_cache = netflix_get_cache('snm2235-jml4759-averageMovieRating')
        ratings = netflix_eval(movie_id, customer_id, movie_cache, customer_cache)
        self.assertEqual(len(ratings), 0)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        netflix_print(w, 101, [1.0])
        self.assertEqual(w.getvalue(), "101:\n1.0\n")

    def test_print_2(self):
        w = StringIO()
        netflix_print(w, 1, [1.0, 2.0, 3.0])
        self.assertEqual(w.getvalue(), "1:\n1.0\n2.0\n3.0\n")

    def test_print_3(self):
        w = StringIO()
        netflix_print(w, 90, [])
        self.assertEqual(w.getvalue(), "90:\n")

    # ----
    # rmse
    # ----

    def test_rmse_1(self):
        a = [1.0, 2.0, 3.0]
        b = [1.0, 2.0, 3.0]
        self.assertEqual(netflix_rmse(a,b), 0.0)

    def test_rmse_2(self):
        a = [1.0, 2.0, 3.0]
        b = [2.0, 3.0, 4.0]
        self.assertEqual(netflix_rmse(a,b), 1.0)

    def test_rmse_3(self):
        a = [1.0, 2.0, 3.0]
        b = [5.0, 2.5, 1.1]
        self.assertEqual(netflix_rmse(a,b), 2.57)


    # ---------
    # get_cache
    # ---------

    def test_get_cache_1(self):
        name = 'snm2235-jml4759-actualCustomerRating'
        cache = netflix_get_cache(name)
        self.assertEqual(len(cache), 1408395)

    def test_get_cache_2(self):
        name = 'snm2235-jml4759-averageCustomerRating'
        cache = netflix_get_cache(name)
        self.assertEqual(len(cache), 480189)

    def test_get_cache_3(self):
        name = 'snm2235-jml4759-averageMovieRating'
        cache = netflix_get_cache(name)
        self.assertEqual(len(cache), 17770)

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1:\n30878\n")
        w = StringIO()
        rmse = netflix_solve(r, w)
        self.assertLess(rmse, 1)

    def test_solve_2(self):
        r = StringIO("10:\n1952305\n1531863\n1000:\n2326571\n977808\n1010534\n")
        w = StringIO()
        rmse = netflix_solve(r, w)
        self.assertLess(rmse, 1)

    def test_solve_3(self):
        r = StringIO("10:\n1952305")
        w = StringIO()
        rmse = netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "10:\n2.9\nRMSE: 0.1\n")

    # ------------------
    # get_actual_ratings
    # ------------------

    def test_get_actual_ratings_1(self):
        movie_id = 1130
        customer_id = [630317]
        name = 'snm2235-jml4759-actualCustomerRating'
        cache = netflix_get_cache(name)

        ratings = netflix_get_actual_ratings(movie_id, customer_id, cache)
        self.assertEqual(ratings[0],2)


    def test_get_actual_ratings_2(self):
        movie_id = 1130
        customer_id = [630317,630317,630317]
        name = 'snm2235-jml4759-actualCustomerRating'
        cache = netflix_get_cache(name)

        ratings = netflix_get_actual_ratings(movie_id, customer_id, cache)
        self.assertEqual(len(ratings),3)

    def test_get_actual_ratings_3(self):
        movie_id = 1130
        customer_id = []
        name = 'snm2235-jml4759-actualCustomerRating'
        cache = netflix_get_cache(name)

        ratings = netflix_get_actual_ratings(movie_id, customer_id, cache)
        self.assertEqual(len(ratings),0)





# ----
# main
# ----

if __name__ == "__main__":
    main()
