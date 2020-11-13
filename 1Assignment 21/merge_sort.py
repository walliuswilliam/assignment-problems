def merge(x,y):
  output_list = []
  x_index = 0
  y_index = 0  
  while x_index < len(x) and y_index < len(y):
    if x[x_index] > y[y_index]:
      output_list.append(y[y_index])
      y_index += 1
    else:
      output_list.append(x[x_index])
      x_index += 1
  
  if x_index < len(x):
    while x_index < len(x):
      output_list.append(x[x_index])
      x_index += 1
  else:
    while y_index < len(y):
      output_list.append(y[y_index])
      y_index += 1
  return output_list

if __name__ == "__main__":
  print('testing merge sort...')
  assert merge([-2,1,4,4,4,5,7],[-1,6,6]) == [-2,-1,1,4,4,4,5,6,6,7], merge([-2,1,4,4,4,5,7],[-1,6,6])
  print('passed')
