from functools import reduce

prime_for_english_alphabet = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
ord_of_A = 65

def hashing(acc, y):
	return acc * prime_for_english_alphabet[y - ord_of_A]

def is_anagram(s_a, s_b):
	hash_of_s_a = reduce(hashing, map(ord, s_a), 1)
	hash_of_s_b = reduce(hashing, map(ord, s_b), 1)
	return hash_of_s_a == hash_of_s_b

def solution(string_a, string_b):
	count = 0
	for size in range(1, len(string_a) + 1):
		for index in range(len(string_a) - size + 1):
			substring_of_a = string_a[index:index + size]
			for index_of_b in range(len(string_b) - size + 1):
				substring_of_b = string_b[index_of_b:index_of_b + size]
				if is_anagram(substring_of_a, substring_of_b):
					count += 1
					break
	return count

def read_input():
	# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
	# This is all you need for most Kickstart problems.
	cases = int(input())  # read a line with a single integer
	for _ in range(cases):
		# string size but not needed in python
		int(input())
		string_a = input()
		string_b = input()
		yield string_a, string_b

def run():
	input_reader = read_input()
	case_number = 1
	for string_a, string_b in input_reader:
		print(f'Case #{case_number}:', solution(string_a, string_b))
		case_number = case_number + 1

if __name__ == "__main__":
	run()