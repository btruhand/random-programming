from typing import List
import unittest

def solution(A: List[int]) -> int:
	"""Solution to problem

	Given a list of integers give the FIRST unique integer in the array

	:param A: The list
	:type A: List[int]
	:return: The first unique integer or -1 if there's none
	:rtype: int
	"""
	uniqueness_set = dict(map(lambda x: (x, 0), A))
	for el in A:
		uniqueness_set[el] = uniqueness_set[el] + 1

	for el in A:
		if uniqueness_set[el] == 1:
			return el

	return -1

class TestFirstNonRepeatInteger(unittest.TestCase):
	def test_single_value_array(self):
		self.assertEqual(1, solution([1]))

	def test_all_unique_array(self):
		self.assertEqual(1, solution([1,5,7,9]))

	def test_first_one_is_unique(self):
		self.assertEqual(4, solution([4,7,5,6,7,6,5]))

	def test_unique_is_somewhere_in_the_middle(self):
		self.assertEqual(10, solution([4,8,4,5,10,5,12,8]))

	def test_unique_is_at_the_end(self):
		self.assertEqual(15, solution([1,5,5,6,7,1,6,7,15]))

unittest.main()