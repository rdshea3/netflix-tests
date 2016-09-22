#!/usr/bin/env python3

# -------
# imports
# -------

from io import StringIO
import json, urllib.request
import unittest

import Netflix
from Netflix import netflix_eval, netflix_print, netflix_solve, getRMSE

# -----------
# TestNetflix
# -----------

class TestNetflixEval (unittest.TestCase):
	def setUp(self):
		self.movies = dict()
		self.customerOffset = dict()
		self.actualsCache = dict()

		local_filename, headers = urllib.request.urlretrieve("http://www.cs.utexas.edu/users/fares/netflix-caches/amg5763-SuperMapMovieCache.json")
		with open(local_filename) as filename:
			data = json.load(filename)
			for movieID in data["movies"]:
				if self.movies.get(movieID) == None:
					self.movies[movieID] = []
				self.movies[movieID].append(float(data["movies"][movieID]["mean"]))
				self.movies[movieID].append(float(data["movies"][movieID]["standard_deviation"]))

		
		local_filename, headers = urllib.request.urlretrieve("http://www.cs.utexas.edu/users/fares/netflix-caches/amg5763-BehaviorCache.json")
		with open(local_filename) as filename:
			data = json.load(filename)
			for customerID in data:
				self.customerOffset[customerID] = data[customerID]

		with open("nb8384-ActualsCache.txt") as filename:
			for s in filename:
				if s[len(s) - 2] == ':':
					if len(s) > 2:
						movieID = int(s[0:len(s) - 2])
						if self.actualsCache.get(movieID) == None:
							self.actualsCache[movieID] = dict()
					else:
						raise ValueError("Input has ':' without a number before it")
				else:
					parts = s.split(" ")
					self.actualsCache[movieID][int(parts[0])] = int(parts[1])

	# ----
	# eval
	# ----

	def test_eval_1(self):
		Netflix.movies = self.movies;
		Netflix.customerOffset = self.customerOffset;
		Netflix.actualsCache = self.actualsCache;
		v = netflix_eval("1", "2097211")
		self.assertEqual(v, self.movies["1"][0] + self.customerOffset["2097211"])

	def test_eval_2(self):
		Netflix.movies = self.movies;
		Netflix.customerOffset = self.customerOffset;
		Netflix.actualsCache = self.actualsCache;
		v = netflix_eval("17770", "2097120")
		self.assertEqual(v, self.movies["17770"][0] + self.customerOffset["2097120"])

	def test_eval_3(self):
		Netflix.movies = self.movies;
		Netflix.customerOffset = self.customerOffset;
		Netflix.actualsCache = self.actualsCache;
		v = netflix_eval("17745", "1040743")
		self.assertEqual(v, self.movies["17745"][0] + self.customerOffset["1040743"])

	def test_eval_4(self):
		Netflix.movies = self.movies;
		Netflix.customerOffset = self.customerOffset;
		Netflix.actualsCache = self.actualsCache;
		v = netflix_eval("3886", "1040587")
		self.assertEqual(v, self.movies["3886"][0] + self.customerOffset["1040587"])

	def test_eval_5(self):
		Netflix.movies = self.movies;
		Netflix.customerOffset = self.customerOffset;
		Netflix.actualsCache = self.actualsCache;
		v = netflix_eval("3879", "1040462")
		self.assertEqual(v, self.movies["3879"][0] + self.customerOffset["1040462"])


class TestNetflix (unittest.TestCase):

	# ----
	# print
	# ----

	def test_print_1(self):			
		w = StringIO()
		writeBuffer = ['hi','bye','hello']
		netflix_print(w, writeBuffer)
		self.assertEqual(w.getvalue(), 'hi\nbye\nhello\n')

	def test_print_2(self):			
		w = StringIO()
		writeBuffer = ['test','movie','customer']
		netflix_print(w, writeBuffer)
		self.assertEqual(w.getvalue(), 'test\nmovie\ncustomer\n')

	def test_print_3(self):			
		w = StringIO()
		writeBuffer = ['one','two','three']
		netflix_print(w, writeBuffer)
		self.assertEqual(w.getvalue(), 'one\ntwo\nthree\n')

	def test_print_4(self):			
		w = StringIO()
		writeBuffer = ['movieOne','movieTwo','movieThree']
		netflix_print(w, writeBuffer)
		self.assertEqual(w.getvalue(), 'movieOne\nmovieTwo\nmovieThree\n')

	def test_print_5(self):			
		w = StringIO()
		writeBuffer = ['customerOne','customerTwo','customerThree']
		netflix_print(w, writeBuffer)
		self.assertEqual(w.getvalue(), 'customerOne\ncustomerTwo\ncustomerThree\n')
		



	# ----
	# getRMSE
	# ----

	def test_getRMSE_1(self):
		x = [1,2]
		y = [5,6]
		v = getRMSE(x, y)
		self.assertEqual(v, '4.00')

	def test_getRMSE_2(self):
		x = [20,6,14,4]
		y = [10,1,8,2]
		v = getRMSE(x, y)
		self.assertEqual(v, '6.42')

	def test_getRMSE_3(self):
		x = [32,6,10,235,26,6]
		y = [20,1,4,1,22,3]
		v = getRMSE(x, y)
		self.assertEqual(v, '95.73')

	def test_getRMSE_4(self):
		x = [2.0,5.0,17.0,12.8]
		y = [1.5,2.0,10.6,20.0]
		v = getRMSE(x, y)
		self.assertEqual(v, '5.05')

	def test_getRMSE_5(self):
		x = [7,7,10.0,2,7.0]
		y = [2,1,17.9,3,3.6]
		v = getRMSE(x, y)
		self.assertEqual(v, '5.21')

	# ----
	# solve
	# ----

	def test_solve_1(self):
		r = StringIO("1:\n30878\n")
		w = StringIO()
		netflix_solve(r,w)
		result = Netflix.movies["1"][0] + Netflix.customerOffset["30878"]
		resultstr = "{0:.1f}".format(result)
		RMSE = (((Netflix.actualsCache[1][30878] - result) ** 2)/1) ** 0.5
		RMSEstr = "{0:.2f}".format(RMSE)
		self.assertEqual(w.getvalue(), "1:\n" + resultstr + "\n" + "RMSE: " + RMSEstr + "\n")
		
# ----
# main
# ----

if __name__ == "__main__":
    unittest.main()