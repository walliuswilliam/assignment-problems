import sys
sys.path.append('1Assignment 21')
from merge_sort import merge

# def merge_sort(arr):
#   if len(arr) < 2:
#     return arr
#   halfway_index = len(arr)//2
#   left_half = arr[:halfway_index]
#   right_half = arr[halfway_index:]
#   sorted_left_half = merge_sort(left_half)
#   sorted_right_half = merge_sort(right_half)
#   return merge(sorted_left_half,sorted_right_half)

# print('testing merge sort 2')
# assert merge_sort([4,8,7,7,4,2,3,1]) == [1,2,3,4,4,7,7,8], merge_sort([4,8,7,7,4,2,3,1])
# print('passed')

# def merge(list1, list2):
#   output = []
#   i = 0 # index in list1
#   j = 0 # index in list2
#   while i < len(list1) and j < len(list2):
#     if list1[i] < list2[j]:
#       output.append(list1[i])
#       i += 1
#     else:    
#       output.append(list2[j])   
#       j += 1  
#   if i < len(list1):  
#     output += list1[i:]  
#   if j < len(list2):   
#     output += list2[j:]  
#   return output

# print('testing final merge sort...')
# assert merge([-2,1,4,4,4,5,7],[-1,6,6]) == [-2,-1,1,4,4,4,5,6,6,7], merge([-2,1,4,4,4,5,7],[-1,6,6])
# print('passed')

# def dot_product(arr1, arr2):
#   ans = 0
#   for i in range(len(arr1)):
#     ans += arr1[i]*arr2[i]
#   return ans
  
# print(dot_product([1,2,3], [2,4,3]))

# import sys
# sys.path.append('1Assignment 34')
# from cartesian_product import cartesian_product

# def grid_search(objective_function, grid_lines):
#   intersection_points = cartesian_product(grid_lines)
#   min_value = objective_function(intersection_points[0][0], intersection_points[0][1])
#   min_point = [intersection_points[0][0], intersection_points[0][1]]
#   for point in intersection_points:
#     temp_value = objective_function(point[0], point[1])
#     if temp_value < min_value:
#       min_value = temp_value
#       min_point = point
#   return min_value


# def two_variable_function(x, y):
#   return (x**2)*(y**2)+2*(y-1)**2

# x_lines = [0,1]
# y_lines = [0,1,2]
# grid_lines = [x_lines, y_lines]

# print(grid_search(two_variable_function, grid_lines))

# import math

# def f(x):
#   return x**2-1


# def gradient_descent(f,x0,alpha=0.1,delta=0.1,iterations=10000):
#   for iteration in range(iterations):
#     deriv = (f(x0+0.5*delta)-f(x0-0.5*delta))/delta
#     x0 = x0-alpha*deriv
#   return f(x0)

# print(gradient_descent(f, 2))


def f(x):
  # return x**3 + x - 1
  return x**2-1

def estimate_derivative(f, c, delta):
  return (f(c+0.5*delta)-f(c-0.5*delta))/delta

def zero_of_tangent_line(f, c, delta):
  slope = estimate_derivative(f, c, delta)
  y_at_x = f(c)
  b = y_at_x - slope*c
  x = (0-b)/slope
  return round(x,6)
# print('testing zero of tangent line...')
# answer = zero_of_tangent_line(f, 0.5, 0.001)
# assert round(answer,6) == 0.714286
# print('passed')

def estimate_solution(f, initial_guess, delta, precision):
  guess = initial_guess
  pre_guess = initial_guess+precision
  while abs(guess-pre_guess) >= precision:
    pre_guess = guess
    guess = zero_of_tangent_line(f, guess, delta)
  return guess


# print('testing estimate solution...')
# answer = estimate_solution(f, 0.5, 0.001, 0.01)
# assert round(answer, 6) == 0.682328
# print('passed')

print(zero_of_tangent_line(f, 2, 0.001))
print(estimate_solution(f, 2, 0.001, 0.00000001))
# 1.25