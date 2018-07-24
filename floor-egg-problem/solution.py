# Solution:
# - Type: Dynamic programming
# - Runtime: O(floor^2 * egg)
# - Space: O(egg * floor)
# Uses dynamic programming to calculate based on previous known minimized maximum regret
# Optimal substructure: Notice that a floor F' with remaining eggs E' with known optimum solution to the problem
# can be used to build the solution for floor F and eggs E by simply adding the optimum solution for floors (F - F') and eggs
# (E - E')

def egg_and_floor_best_worse_case(egg, floor):
  table = [[0 for _ in range(floor + 1)]]
  table.append([y for y in range(floor + 1)])
  table.extend([[0 for _ in range(floor + 1)] for _ in range(egg - 1)])

  i = 2
  while i <= egg:
    j = 1
    while j <= floor:
      drop = 1
      minimized_maximum_regret = None
      while drop <= j:
        broken_drop = 1 + table[i - 1][drop - 1]
        continue_with_same_egg_drop = 1 + table[i][j - drop]

        ## we choose the maximum number of drops (which is the worst case)
        ## then we minimize the current one we have with the maximum we found (getting the minimized worst case)
        if broken_drop > continue_with_same_egg_drop:
          minimized_maximum_regret = broken_drop if minimized_maximum_regret is None \
            else min(minimized_maximum_regret, broken_drop)
        else:
          minimized_maximum_regret = continue_with_same_egg_drop if minimized_maximum_regret is None \
            else min(minimized_maximum_regret, continue_with_same_egg_drop)

        drop += 1

      table[i][j] = minimized_maximum_regret
      j += 1
    i += 1
  return table[egg][floor]

print(egg_and_floor_best_worse_case(1, 2) == 2)
print(egg_and_floor_best_worse_case(1, 0) == 0)
print(egg_and_floor_best_worse_case(0, 1) == 0)
print(egg_and_floor_best_worse_case(2, 3) == 2)
print(egg_and_floor_best_worse_case(2, 8) == 4) # dropping first at 5
print(egg_and_floor_best_worse_case(2, 100) == 14) # the two eggs 100 floors problem
print(egg_and_floor_best_worse_case(3, 1000) == 19)
print(egg_and_floor_best_worse_case(7, 20) == 5)
