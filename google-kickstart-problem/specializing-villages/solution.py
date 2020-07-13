def solution(num_villages, adjacency_graph):
	village_veggies = list(range(1, num_villages + 1))
	number_of_villages_as_fruits = range(1, num_villages)
	for to_make_fruits in number_of_villages_as_fruits:
		fruit_villages = []
		fruit_veggie_village_combination = make_possible_combo(fruit_villages, village_veggies, to_make_fruits)
		print(fruit_veggie_village_combination)

def read_input():
	# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
	# This is all you need for most Kickstart problems.
	cases = int(input())  # read a line with a single integer
	for _ in range(cases):
		# string size but not needed in python
		num_villages, num_edges = (int(x) for x in input().split(' '))
		adjacency_graph = [[None] * num_villages for _ in range(num_villages)]
		for _edges in range(num_edges):
			village_a, village_b, cost = (int(y) for y in input().split(' '))
			adjacency_graph[village_a - 1][village_b - 1] = cost
			adjacency_graph[village_b - 1][village_a - 1] = cost

		yield num_villages, adjacency_graph

def run():
	input_reader = read_input()
	case_number = 1
	for num_villages, adjacency_graph in input_reader:
		print(f'Case #{case_number}:', solution(num_villages, adjacency_graph))
		case_number = case_number + 1

def make_possible_combo(list_a, list_b, to_be_added):
	combos = []
	for index in range(len(list_b) - to_be_added + 1):
		copy_of_list_a = list_a.copy()
		copy_of_list_a.append(list_b[index])
		if to_be_added == 1:
			# the case when 1
			copy_of_list_b = list_b.copy()
			del copy_of_list_b[index]
			combos.append((copy_of_list_a, copy_of_list_b))
		else:
			for start_to_add in range(index, len(list_b) - to_be_added + 1):
				copy_of_copied_list_a = copy_of_list_a.copy()
				copy_of_copied_list_a.extend(list_b[start_to_add + 1:start_to_add + to_be_added])
				set_list_b = set(list_b)
				set_copied_list_a = set(copy_of_copied_list_a)
				combos.append((copy_of_copied_list_a, list(set_list_b - set_copied_list_a)))
	return combos

if __name__ == "__main__":
	run()