import matplotlib.pyplot as plt

def collatz_iterations(n):
  iterations = 0
  while n != 1:
    if n % 2 == 0:
      n = n/2
      iterations += 1
    else:
      n = 3*n+1
      iterations += 1
  return iterations

print('testing collatz iterations...')
assert collatz_iterations(13) == 9, 'failed'
print('passed')


highest_iterations = 0
for n in range(1, 1001):
  iterations = collatz_iterations(n)
  if highest_iterations < iterations:
    highest_iterations = iterations
    highest_index = n
print(highest_index)


plt.style.use('bmh')
x_coords = [x for x in range(1,1001)]
y_coords = [collatz_iterations(x) for x in range(1,1001)]
plt.plot(x_coords, y_coords)
plt.xlabel('Numbers')
plt.ylabel('Number of Iterations')
plt.title('Collatz Iterations')
plt.savefig('plot.png')