degreesCelsius c = 9/5*c+32
recommendClothing n = degreesCelsius n >= 80 = "shortsleeve" 
main = print (recommendClothing 11)