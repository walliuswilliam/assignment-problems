import math

def function(x):
  return (math.exp((-x**2)/2))*(1/math.sqrt(2*math.pi))

def calc_standard_normal_probability(a,b):
  point = a
  riemann_sum = 0
  while point <= b:
    riemann_sum += 0.001*function(point)
    point += 0.001
  return riemann_sum

print(calc_standard_normal_probability(-1, 1))
print(calc_standard_normal_probability(-2, 2))
print(calc_standard_normal_probability(-3, 3))