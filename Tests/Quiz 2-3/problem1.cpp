# include <iostream>
# include <cassert>

int calcIndex(int n) {
  if (n<2){
    return n;
  }

    int terms[n+1]{};
    for (int count{ 0 }; n >= count; ++count) {
      if (count == 0 || count == 1){
        terms[count] = count;
      }
      else{
        terms[count] = terms[count-1] + terms[count-2];
      }
    }
    
    int count = 0;
    while (terms[count] <= n) {
      count += 1;
    }

    return count;
}

int main()
{
    std::cout << "Testing...\n";

    assert(calcIndex(8)==7);
    assert(calcIndex(100000)==26);

    std::cout << "Success!";

    return 0;
}