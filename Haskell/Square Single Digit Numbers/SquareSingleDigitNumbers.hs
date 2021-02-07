squareSingleDigitNumbers n = map (**2) (filter (<10) n)  

main = print(squareSingleDigitNumbers [2, 7, 15, 11, 5])