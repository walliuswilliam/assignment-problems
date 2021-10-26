import sys
sys.path.append("1Assignment 82")
from sudoku_solver import is_valid

arr = [[1,None,4,None,6,None], [5,2,None,4,None,None], [None,1,3,None,5,4], [2,4,None,1,3,None], [None,6,1,None,2,None], [3,None,2,None,4,1]]

for x_0_1 in range(1,7):
	print(arr)
  arr[0][1] = x_0_1
  if is_valid(arr):
		for x_0_3 in range(1,7):
			arr[0][3] = x_0_3
			if is_valid(arr):
				for x_0_5 in range(1,7):
					arr[0][5] = x_0_5
					if is_valid(arr):
						for x_1_2 in range(1,7):
							arr[1][2] = x_1_2
							if is_valid(arr):
								for x_1_4 in range(1,7):
									arr[1][4] = x_1_4
									if is_valid(arr):
										for x_1_5 in range(1,7):
											arr[1][5] = x_1_5
											if is_valid(arr):
												for x_2_0 in range(1,7):
													arr[2][0] = x_2_0
													if is_valid(arr):
														for x_2_3 in range(1,7):
															arr[2][3] = x_2_3
															if is_valid(arr):
																for x_3_2 in range(1,7):
																	arr[3][2] = x_3_2
																	if is_valid(arr):
																		for x_3_5 in range(1,7):
																			arr[3][5] = x_3_5
																			if is_valid(arr):
																				for x_4_0 in range(1,7):
																					arr[4][0] = x_4_0
																					if is_valid(arr):
																						for x_4_3 in range(1,7):
																							arr[4][3] = x_4_3
																							if is_valid(arr):
																								for x_4_5 in range(1,7):
																									arr[4][5] = x_4_5
																									if is_valid(arr):
																										for x_5_1 in range(1,7):
																											arr[5][1] = x_5_1
																											if is_valid(arr):
																												for x_5_3 in range(1,7):
																													arr[5][3] = x_5_3
																													if is_valid(arr):
																														print(arr)