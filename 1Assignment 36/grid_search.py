import sys
sys.path.append('1Assignment 34')
from cartesian_product import cartesian_product

def grid_search(objective_function, grid_lines):
  intersection_points = cartesian_product(grid_lines)
  min_value = objective_function(intersection_points[0][0], intersection_points[0][1])
  min_point = [intersection_points[0][0], intersection_points[0][1]]
  for point in intersection_points:
    temp_value = objective_function(point[0], point[1])
    if temp_value < min_value:
      min_value = temp_value
      min_point = point
  return min_point


def two_variable_function(x, y):
  return (x-1)**2 + (y-1)**3

x_lines = [0, 0.25, 0.75]
y_lines = [0.9, 1, 1.1, 1.2]
grid_lines = [x_lines, y_lines]

print('testing grid_search...')
assert grid_search(two_variable_function, grid_lines) == [0.75, 0.9], grid_search(two_variable_function, grid_lines) 
print('passed')