findSmallestPositive :: (Num a, Ord a) => [a] -> a  
findSmallestPositive [] = error "list is empty"  
findSmallestPositive [x] = x  
findSmallestPositive (x:xs)   
    | 0 < x && x < minTail = x
    | otherwise = minTail  
    where minTail = findSmallestPositive xs


main = print(findSmallestPositive [8, 3, -1, 2, -5, 7])