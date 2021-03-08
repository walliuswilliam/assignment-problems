# include <iostream>
# include <cassert>

int dotProduct(int arr1[], int arr2[], int arrLen)
{
  int product = 0;
  for (int num{0}; arrLen > num; ++num){
    product += arr1[num]*arr2[num];
  }

  return product;

}

int main()
{

    int array1[] = {1, 2, 3, 4};
    int array2[] = {5, 6, 7, 8};
    int length = sizeof(array1) / sizeof(array1[0]);
    int ans = dotProduct(array1, array2, length);

    std::cout << "Testing...\n";
    assert(ans == 70);
    std::cout << "Success!";

    return 0;
}