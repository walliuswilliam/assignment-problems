reverseList :: [a] -> [a]
reverseList [] = []
reverseList (x:xs) = reverseList xs ++ [x]


take' :: (Num i, Ord i) => i -> [a] -> [a]  
take' n _  
    | n <= 0   = []  
take' _ []     = []  
take' n (x:xs) = x : take' (n-1) xs


tail' n input_list = (reverseList (take' n (reverseList input_list)))

main = print(tail' 4 [8, 3, -1, 2, -5, 7])