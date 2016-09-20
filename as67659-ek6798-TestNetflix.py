#!/usr/bin/env python3

# -------------------------------
# cs373-netflix/TestNetflix.py
#
# Abderrahman Said-Alaoui
# Eric Kramer
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Netflix import netflix_read, netflix_eval, netflix_print, netflix_solve, rmse_calc

# -----------
# TestCollatz
# -----------


class TestNetflix(TestCase):
    # ----
    # read
    # ----

    def test_read_1(self):
        line = "42:\n"
        num = netflix_read(line)
        self.assertEqual(num, 42)

    def test_read_2(self):
        line = "427\n"
        num = netflix_read(line)
        self.assertEqual(num, 427)

    def test_read_3(self):
        line = "420000\n"
        num = netflix_read(line)
        self.assertEqual(num, 420000)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        value = netflix_eval(1, 548064, [])
        self.assertEqual(value, '3.49')

    def test_eval_2(self):
        value = netflix_eval(6946, 1261894, [])
        self.assertEqual(value, '3.19')

    def test_eval_3(self):
        value = netflix_eval(16326, 433517, [])
        self.assertEqual(value, '3.42')

    # ---------
    # rmse_calc
    # ---------

    def test_rmse_calc_1(self):
        value = rmse_calc([1.0, 1.5, 3.4, 3.6, 4.0, 5.0])
        self.assertEqual(value, '1.76')

    def test_rmse_calc_2(self):
        value = rmse_calc([0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
        self.assertEqual(value, '0.71')

    def test_rmse_calc_3(self):
        value = rmse_calc([42, 42, 42, 42, 1, 2, 0.5, 0.25])
        self.assertEqual(value, '4.63')

    # -----
    # print
    # -----

    def test_print_1(self):
        writer = StringIO()
        netflix_print(writer, "The best string ever")
        self.assertEqual(writer.getvalue(), "The best string ever\n")

    def test_print_2(self):
        writer = StringIO()
        netflix_print(writer, "The second best string ever")
        self.assertEqual(writer.getvalue(), "The second best string ever\n")

    def test_print_3(self):
        writer = StringIO()
        netflix_print(writer, "The third best string ever")
        self.assertEqual(writer.getvalue(), "The third best string ever\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        reader = StringIO("1:\n548064\n1095:\n453352\n1877477\n")
        writer = StringIO()
        netflix_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(),
            "1:\n3.49\n1095:\n3.16\n3.35\nRMSE: 1.12\n")

    def test_solve_2(self):
        reader = StringIO(
            "17236:\n477855\n1620428\n375352\n339109\n1465796\n1282081\n1199881\n")
        writer = StringIO()
        netflix_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(),
            "17236:\n2.75\n2.70\n2.70\n3.09\n3.22\n3.40\n2.65\nRMSE: 1.31\n")

    def test_solve_3(self):
        reader = StringIO("6905:\n246618\n1305872\n345476\n5427:\n129710\n")
        writer = StringIO()
        netflix_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(),
            "6905:\n4.14\n3.54\n3.07\n5427:\n3.19\nRMSE: 1.04\n")
# ----
# main
# ----

if __name__ == "__main__":
    main()
