# include <iostream>
# include <cassert>

int main()
{
    int array[5]{ 30, 50, 20, 10, 40 };
    int arrayLen = sizeof(array)/sizeof(array[0]);
    int smallestNum;
    int tempItem;

    for (int index{ 0 }; arrayLen > index; ++index) {
      smallestNum = index;
      for (int count{ index }; arrayLen > count; ++count) {
        if (array[count] < array[smallestNum]) {
          smallestNum = count;
        }
      }

      if (smallestNum != index) {
        tempItem = array[index];
        array[index] = array[smallestNum];
        array[smallestNum] = tempItem;
      }
    }

    std::cout << "Testing...\n";

    assert(array[0]==10);
    assert(array[1]==20);
    assert(array[2]==30);
    assert(array[3]==40);
    assert(array[4]==50);

    std::cout << "Succeeded";

    return 0;
}