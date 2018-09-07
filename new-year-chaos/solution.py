from typing import List, Union
import unittest

def find_median_of_three(A: int, B: int, C: int):
	first_choice = max(A,B)
	second_choice = max(B,C)
	return min(first_choice, second_choice)

def solution(A: List[int]) -> Union[int, str]:
	"""Solution to the new year chaos problem

	Given a list of integers satisfying the conditions laid out in
	`<https://www.hackerrank.com/challenges/new-year-chaos/problem>`_ then find the
	number of minimum movement change to reach the state of the List or the string
	"Too chaotic"

	:param A: A list of integers
	:type A: List[int]
	:return: Number of movement change or "Too chaotic"
	:rtype: Union[int, str]
	"""
	number_of_movements = 0
	for idx, value in enumerate(A):
		if value > (idx + 3):
			# indices starts from 0 so plus 3
			return "Too chaotic"
		for check_index in range(max(0, value - 2), idx):
			# -2 because -1 from deduction of value to be 0-indexed
			# then another -1 so that you compare from the previous one
			if A[check_index] > value:
				number_of_movements = number_of_movements + 1

	return number_of_movements

class TestNewYearChaos(unittest.TestCase):
	def test_sample_input(self):
		self.assertEqual(3, solution([2,1,5,3,4]))

	def test_simple_input_no_chaos(self):
		self.assertEqual(0, solution([1,2,3,4,5,6,7]))

	def test_too_chaotic(self):
		self.assertEqual("Too chaotic", solution([4,1,2,3,5,6]))
		self.assertEqual("Too chaotic", solution([1,5,2,3,4,6]))

	def test_one_difference(self):
		self.assertEqual(1, solution([1,2,4,3,5]))

	def test_harder_shuffle(self):
		self.assertEqual(7, solution([1,2,5,3,7,8,6,4]))

	def test_number_beyond_index_shuffled(self):
		self.assertEqual(9, solution([1,3,2,6,5,4,9,10,8,7,11]))

	def test_number_beyond_index_shuffled_discreetly(self):
		self.assertEqual(13, solution([2,1,5,6,3,4,9,8,11,7,10,14,13,12]))

unittest.main()
