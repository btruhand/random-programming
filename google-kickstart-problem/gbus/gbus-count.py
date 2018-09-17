def cmp_range(range_one, range_two):
	if range_one[0] < range_two[0]:
		return -1
	elif range_one[0] == range_two[0]:
		return 0
	else:
		return 1

def solution(bus_ranges, cities):
	num_bus_per_city = []
	for city in cities:
		num_per_city = 0
		for bus_range in bus_ranges:
			if bus_range[0] <= city <= bus_range[1]:
				num_per_city = num_per_city + 1
		num_bus_per_city.append(num_per_city)
	return num_bus_per_city

def read_input():
	# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
	# This is all you need for most Kickstart problems.
	t = int(input())  # read a line with a single integer
	for _ in range(1, t + 1):
		int(input())
		bus_ranges = [int(x) for x in input().split(' ')[:-1]]
		bus_ranges = [tuple(iter_pair) for iter_pair in zip(*[iter(bus_ranges)] * 2)]
		num_cities = int(input())
		cities = []
		for _ in range(num_cities):
			cities.append(int(input()))
		yield bus_ranges, cities
		input() # waste an empty line
		#print("Case #{}: {} {}".format(i, n + m, n * m))
		# check out .format's specification for more formatting options

def run():
	input_reader = read_input()
	case_number = 1
	for bus_ranges, cities in input_reader:
		print(f'Case #{case_number}:', ' '.join(map(str, solution(bus_ranges, cities))))
		case_number = case_number + 1

if __name__ == "__main__":
	run()