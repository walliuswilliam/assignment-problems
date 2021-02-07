recommendClothing :: (RealFloat a) => a -> String  
recommendClothing degreesCelsius  
    | degreesFahrenheit >= 80 = "You should wear a shortsleeve shirt"
    | degreesFahrenheit > 65 = "You should wear a longsleeve shirt"
    | degreesFahrenheit > 50 = "You should wear a sweater"
    | otherwise = "You should wear a jacket"
    where degreesFahrenheit = (degreesCelsius*(9/5))+32

main = print(recommendClothing 5)