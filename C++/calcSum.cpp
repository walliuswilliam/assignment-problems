#include <iostream>
#include <cassert>

int calcSum(int m, int n) {
  int ascending[m][n]{};
  int descending[n][m]{};
  int outputArray[m][m]{};

  int ascendingCount = 1;
  int descendingCount = m*n;

  for (int row{ 0 }; m > row; ++row) {
    for (int column{ 0 }; n > column; ++column) {
      ascending[row][column] = ascendingCount;
      ascendingCount += 1;
    }
  }
  
  for (int row{ 0 }; n > row; ++row) {
    for (int column{ 0 }; m > column; ++column) {
      descending[row][column] = descendingCount;
      descendingCount -= 1;
    }
  }


  for (int row{ 0 }; m > row; ++row) {
    for (int column{ 0 }; m > column; ++column) {
      int element_sum = 0;
      for (int nCol{ 0 }; n > nCol; ++nCol) {
        element_sum += ascending[row][nCol]*descending[nCol][column];
      }
      outputArray[row][column] = element_sum;
    }
  }

  int sum = 0;
  for (int row{ 0 }; m > row; ++row) {
    for (int column{ 0 }; m > column; ++column) {
      sum += outputArray[row][column];
    }
  }

  return sum;
}

int main() {
  std::cout << "Testing...\n";
  assert(calcSum(2,3)==131);
  std::cout << "Success!";
}
 
 
 
 
 
 
 
 
