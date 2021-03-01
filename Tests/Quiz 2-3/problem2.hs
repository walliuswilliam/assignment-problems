gradeCredits ['A'] = 4
gradeCredits ['B'] = 3
gradeCredits ['C'] = 2
gradeCredits ['D'] = 1
gradeCredits ['F'] = 0

calcGPA grades = sum(map(gradeCredits) grades)/length(grades)

main = print(calcGPA(["A", "B", "B", "C", "C", "C", "D", "F"]))
