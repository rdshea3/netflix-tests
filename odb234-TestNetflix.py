# -------
# imports
# -------
from io import StringIO
from unittest import main, TestCase

from Netflix import netflix_solve, find_pred, probe_reduce, get_rmse

#------------
# TestNetFlix
#------------

class TestNetflix(TestCase):
	"""Class for Netflix unit tests"""
	#------
	# solve
	#------
	def test_solve_1(self):
		"""solve test 1"""
		read = StringIO('1:\n30878\n2647871\n1283744\n2488120\n317050\n1904905\n1989766\n')
		write = StringIO()
		netflix_solve(read, write)
		self.assertEqual(write.getvalue(), '1:\n4.52\n4.27\n4.46\n5.17\n4.53\n4.66\n4.33\nRMSE:0.81\n')

	def test_solve_2(self):
		"""solve test 2"""
		read = StringIO('1:\n30878\n2647871\n1283744\n2488120\n317050\n1904905\n1989766\n14756\n1027056\n1149588\n1394012\n1406595\n2529547\n1682104\n2625019\n2603381\n1774623\n470861\n712610\n1772839\n1059319\n2380848\n548064\n')
		write = StringIO()
		netflix_solve(read, write)
		self.assertEqual(write.getvalue(), '1:\n4.52\n4.27\n4.46\n5.17\n4.53\n4.66\n4.33\n4.53\n4.74\n4.41\n4.07\n4.46\n4.7\n4.72\n3.96\n4.68\n4.46\n5.04\n4.8\n4.83\n4.14\n5.38\n4.42\nRMSE:0.83\n')


	def test_solve_3(self):
		"""solve test 3"""
		read = StringIO('1:\n30878\n2647871\n1283744\n2488120\n317050\n1904905\n1989766\n14756\n1027056\n1149588\n1394012\n1406595\n2529547\n1682104\n2625019\n2603381\n1774623\n470861\n712610\n1772839\n1059319\n2380848\n548064\n123456\n')
		write = StringIO()
		netflix_solve(read, write)
		self.assertEqual(write.getvalue(), '1:\n4.52\n4.27\n4.46\n5.17\n4.53\n4.66\n4.33\n4.53\n4.74\n4.41\n4.07\n4.46\n4.7\n4.72\n3.96\n4.68\n4.46\n5.04\n4.8\n4.83\n4.14\n5.38\n4.42\n1.0\nRMSE:0.68\n')

	def test_solve_4(self):
		"""solve test 4"""
		read = StringIO('1:\n30878\n2647871\n1283744\n2488120\n317050\n1904905\n1989766\n14756\n1027056\n1149588\n1394012\n1406595\n2529547\n1682104\n2625019\n2603381\n1774623\n470861\n712610\n1772839\n1059319\n2380848\n548064\n123456\n')
		write = StringIO()
		netflix_solve(read, write)
		self.assertNotEqual(write.getvalue(), '')

	def test_solve_5(self):
		"""solve test 5"""
		read = StringIO('1:\n30878\n2647871\n1283744\n2488120\n317050\n1904905\n1989766\n14756\n1027056\n1149588\n1394012\n1406595\n2529547\n1682104\n2625019\n2603381\n1774623\n470861\n712610\n1772839\n1059319\n2380848\n548064\n123456\n123456\n')
		write = StringIO()
		netflix_solve(read, write)
		self.assertNotEqual(write.getvalue(), '1:\n4.52\n4.27\n4.46\n5.17\n4.53\n4.66\n4.33\n4.53\n4.74\n4.41\n4.07\n4.46\n4.7\n4.72\n3.96\n4.68\n4.46\n5.04\n4.8\n4.83\n4.14\n5.38\n4.42\n1.0\nRMSE:0.68\n')

	def test_solve_6(self):
		"""solve test 6"""
		read = StringIO('1:\n30878\n2647871\n1283744\n2488120\n317050\n1904905\n1989766\n14756\n1027056\n1149588\n1394012\n1406595\n2529547\n1682104\n2625019\n2603381\n1774623\n470861\n712610\n1772839\n1059319\n2380848\n548064\n123456\n123456\n')
		write = StringIO()
		netflix_solve(read, write)
		self.assertNotEqual(write.getvalue(), '1:\n4.52\n4.27\n4.46\n5.17\n4.53\n4.66\n4.33\n4.53\n4.74\n4.41\n4.07\n4.46\n4.7\n4.72\n3.96\n4.68\n4.46\n5.04\n4.8\n4.83\n4.14\n5.38\n4.42\n1.0\nRMSE:0.68\n')

	#---------
	# get_rmse
	#---------

	def test_rmse_1(self):
		"""RSME test 1"""
		probe_avg = {1:1, 2:2, 3:3, 4:4}
		rmse = get_rmse(probe_avg)
		self.assertEqual(1.73, rmse)

	def test_rmse_2(self):
		"""RSME test 2"""
		probe_avg = {1:1}
		rmse = get_rmse(probe_avg)
		self.assertNotEqual(0.0, rmse)

	def test_rmse_3(self):
		"""RSME test 3"""
		probe_avg = {1:4.52, 2: 4.27, 3:4.46, 4:5.17, 5:4.53, 6:4.66, 7:4.33, 8:4.53, 9:4.74, 10:4.41, 11:4.07, 12:4.46, 13:4.7, 14:4.72, 15:3.96, 16:4.68, 17:4.46, 18:5.04, 19:4.8, 20:4.83, 21:4.14, 22:5.38, 23:4.42}
		rmse = get_rmse(probe_avg)
		self.assertEqual(1.49, rmse)

	def test_rmse_4(self):
		"""RSME test 4"""
		probe_avg = {}
		rmse = get_rmse(probe_avg)
		self.assertEqual(0.0, rmse)

	def test_rmse_5(self):
		"""RSME test 5"""
		probe_avg = {1:1.125, 2:1.365, 3:4.43, 4:3.52, 5:2.65, 6:3.95}
		rmse = get_rmse(probe_avg)
		self.assertNotEqual(0.0, rmse)

	def test_rmse_6(self):
		"""RSME test 6"""
		probe_avg = {1:1.251, 2:2.25, 3:3.25, 4:4.25, 5:0.25, 6:1.5}
		rmse = get_rmse(probe_avg)
		self.assertEqual(2.1, rmse)

#-----
# main
#-----

if __name__ == "__main__":
	main()
