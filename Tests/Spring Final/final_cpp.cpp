#include <iostream>
#include <cassert>
#include<math.h>


int sumPerfectCube(int n) {
  int perfectSquares[n];
  int count = 0;

  for (int i = 1; i<(n+1); i++) {
    perfectSquares[count] = pow(i, 3);
    count++;
  }
  
  int len = sizeof(perfectSquares)/sizeof(perfectSquares[0]);
  int sum = 0;

  for(int i = 0; i<len; i++){
    sum += perfectSquares[i];
  }

  return sum;
}
  
  
int main() {
  std::cout << "Testing...\n";
  assert(sumPerfectCube(10)==3025);
  std::cout << "Success!";
}
 
 
 
 
 
 
 
 
