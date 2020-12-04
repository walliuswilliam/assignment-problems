#assignment 35

# #part b
# def summation(iterations):
#   total = 0
#   for k in range(1, iterations+1):
#     if k < 25:
#       total += 0
#     else:
#       calc = 1/(k**5)
#       total += calc
#   return 1/total

# print(summation(10000))

# #part f
# def sum_finder():
#   total = 0
#   final_num = None
#   for num in range(25, 1000):
#     print(total)
#     if total >= 0.95:
#       final_num = num
#       break
#     else:
#       total += 1443199.78322/(num**5)
#   return final_num

# print(sum_finder())



#assignment 36
def summation(iterations):
  total = 0
  for k in range(1, iterations+1):
    if k < 68:
      total += 0
    else:
      calc = 1/(k**4)
      total += calc
  return 1/total

print(summation(10000))

def sum_finder():
  total = 0
  final_num = None
  for num in range(68, 1000):
    print(total)
    if total >= 0.95:
      final_num = num
      break
    else:
      total += 922742.15044495/num**4
  return final_num

print(sum_finder())