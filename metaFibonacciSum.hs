fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)

partialSumEntries k = [fib(i)|i <- [0..k]]
partialSum k = sum(partialSumEntries k)
metaSumEntries n = [partialSum(fib(k))|k <- [0..n]]
metaSum n = sum(metaSumEntries n)

main = print (metaSum 6) -- should come out to 74