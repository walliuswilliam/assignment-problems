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



puzzle = [[1,None,4,None,6,None], [5,2,None,4,None,None], [None,1,3,None,5,4], [2,4,None,1,3,None], [None,6,1,None,2,None], [3,None,2,None,4,1]]


def count(nested_list):
  count = 0
  for list_nest in nested_list:
    count += len(list_nest)
  return count






# def solve_puzzle(puzzle):

#   current_col = 0
#   current_row = 0
#   while any(None in i for i in puzzle) or not is_valid(puzzle):
#     if puzzle[current_row][current_col] == None:
#       puzzle[current_row][current_col] = 0
#     puzzle[current_row][current_col] += 1

#     if any(puzzle[current_row][current_col] in i for i in puzzle):
#       continue

#     if puzzle[current_row][current_col] >= count(square)+1:
#       puzzle[current_row][current_col] = None
#       try:
#         current_col -= 1
#       except:

#       continue

#     if is_valid(square):
#       current_index += 1
            
#   return square

  



# print(solve_puzzle(puzzle))






# def solve_puzzle(arr):
#   for x1 in range(1,7):
#     arr[0][0] = x1
#     for x2 in range(1,7):
#       arr[0][1] = x2
#       if is_valid(arr):
#         for x3 in range(1,7):
#           arr[0][3] = x2
#           if is_valid(arr):
#             for x4 in range(1,7):
#               arr[1][4]
#               if is_valid(arr):



def clear_log():
  with open('1Assignment 82/for_loops.py', 'w') as file:
    file.writelines([''])

def write(string):
  with open('1Assignment 82/for_loops.py', 'a') as file:
    file.writelines([string])


clear_log()

write('import sys\nsys.path.append("1Assignment 82")\nfrom sudoku_solver import is_valid\n\narr = [[1,None,4,None,6,None], [5,2,None,4,None,None], [None,1,3,None,5,4], [2,4,None,1,3,None], [None,6,1,None,2,None], [3,None,2,None,4,1]]\n\n')
indent = ''

for row_index in range(len(puzzle)):
  for col_index in range(len(puzzle[0])):
    value = puzzle[row_index][col_index]
    if value is None:
      iterator = 'x_{}_{}'.format(str(row_index), str(col_index))
      write('{}for {} in range(1,7):\n'.format(indent, iterator))
      indent += '\t'
      write('{}arr[{}][{}] = {}\n'.format(indent, row_index, col_index, iterator))
      write('{}if is_valid(arr):\n'.format(indent))
      indent += '\t'
write(indent+'print(arr)')
      









