 def matrix_multiply(self, matrix2):
    output_elements = [[0 for x in range(matrix2.num_cols)] for y in range(self.num_rows)]
    mat2_ele = matrix2.elements
    for i in range(len(output_elements)):
      for j in range(len(output_elements[i])):
        element_sum = 0  
        for k in range(self.num_cols):
          element_sum += self.elements[i][k]*mat2_ele[k][j]
        output_elements[i][j] = element_sum 
    return Matrix(output_elements)


def matrix_multiply(A, B):
..... product_elements = [[0 for x in range(B.num_cols)] for y in range(A.num_rows)]
..... for col_index in range(len(product_elements)):
..... ..... for row_index in range(len(product_elements[col_index])):
..... ..... ..... dot_product = 0
..... ..... ..... for i in range(A.num_cols):
..... ..... ..... ..... dot_product += A.elements[col_index][i]*B.elements[i][row_index]
..... ..... ..... product_elements[col_index][row_index] = dot_product
..... return Matrix(product_elements)