nthFibonacciNumber n = nthFibonacciNumber (n-1) + nthFibonacciNumber (n-2)
nthFibonacciNumber 0 = 0
nthFibonacciNumber 1 = 1
main = print (nthFibonacciNumber 20)