classifyNumber x = if x >= 0 then "Non-negative" else "Negative"
main = putStrLn (classifyNumber 5)