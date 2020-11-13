def f(x):
  # return x**3 + x - 1
  return 1-x**2

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

print('quiz', zero_of_tangent_line(f, 1, 0.001))