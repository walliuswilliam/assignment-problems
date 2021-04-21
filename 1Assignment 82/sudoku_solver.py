def is_valid(arr):
  #row checker
  for row in arr:
    if None not in row:
      if set(row) != {1,2,3,4,5,6}:
        return False
    else:
      row = [i for i in row if i != None]
      if len(set(row)) != len(row):
        return False

  #column checker
  columns = []
  for column_index in range(len(arr)):
    column = []
    for row in arr:
      column.append(row[column_index])
    columns.append(column)

  for column in columns:
    if None not in column:
      if set(column) != {1,2,3,4,5,6}:
        return False
    else:
      column = [i for i in column if i != None]
      if len(set(column)) != len(column):
        return False
  
  #box checker
  box_starters = [(0,0), (0,3), (2,0), (2,3), (4,0), (4,3)] #(row, column)
  for box_starter in box_starters:
    box = set()
    for row in range(0, 2):
      for col in range(0, 3):
        num = arr[row + box_starter[0]][col + box_starter[1]]
        if num in box:
          return False
        if num != None:
          box.add(num)

  return True


# print(is_valid([[1,3,4,5,6,2],
#                 [5,2,6,4,1,3],
#                 [6,1,3,2,5,4],
#                 [2,4,5,1,3,6],
#                 [4,6,1,3,2,5],
#                 [3,5,2,6,4,1]]))


def solve_puzzle(arr)
  for x1 in range(1,7):
    if arr[0][0] is None:
      arr[0][0] = x1
    for x2 in range(1,7):
      if x2 not in [x1] and arr[0][1] is None:
        arr[0][1] = x2
        is_valid(arr)
            for x3 in range(1,7):
                if x3 in [x1, x2]:
                    continue
                for x4 in range(1,7):
                    if x4 in [x1, x2, x3]:
                        continue
                    for x5 in range(1,7):
                        if x5 in [x1, x2, x3, x4]:
                            continue
                        for x6 in range(1,7):
                            if x6 in [x1, x2, x3, x4, x5]:
                                continue
                            for x7 in range(1,7):
                                if x7 in [x1, x2, x3, x4, x5, x6]:
                                    continue
                                for x8 in range(1,7):
                                    if x8 in [x1, x2, x3, x4, x5, x6, x7]:
                                        continue
                                    for x9 in range(1,7):
                                        if x9 in [x1, x2, x3, x4, x5, x6, x7, x8]:
                                            continue
                                        square = [[x1, x2, x3],
                                                  [x4, x5, x6],
                                                  [x7, x8, x9]]
                                        if is_valid(square, 15):
                                            return square





puzzle = [[None, None,   4,  None, None, None],
          [None, None, None,   2,    3,  None],
          [3,    None, None, None,   6,  None],
          [None,   6,  None, None, None,    2],
          [None,   2,    1,  None, None, None],
          [None, None, None,   5,  None, None]]


