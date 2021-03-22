# include <iostream>

void pointerCalc(int arr[], int arrLen){
  std::cout << "Array has address " << &arr << "\n";
  
  for (int count = 0; count < arrLen; count++){
    std::cout << "Index " << count << " has value " << arr[count] << " and address " << &arr[count] << "\n";
  }

}

int main(){
  int arr[4] = {11,12,13,14};
  int arrLen = sizeof(arr)/sizeof(arr[0]);
  pointerCalc(arr, arrLen);
  return 0;
}