sumFactors a = sum([b|b <- [1..a], a `mod` b == 0])

main = print (sumFactors 10)