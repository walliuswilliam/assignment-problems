# include <iostream>
# include <cassert>

int metaFibonacciSum(int n)
{
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
    int termLen = sizeof(terms)/sizeof(terms[0]);
    int extendedTerms[terms[termLen-1]]{};
    int extTermLen = sizeof(extendedTerms)/sizeof(extendedTerms[0]);

    for (int count{ 0 }; extTermLen >= count; ++count) {
      if (count == 0 || count == 1){
        extendedTerms[count] = count;
      }
      else{
        extendedTerms[count] = extendedTerms[count-1] + extendedTerms[count-2];
      }
    }

    int partialSums[extTermLen+1]{};
    int sum = 0;
    for (int count{ 0 }; extTermLen >= count; ++count) {
      sum = 0;
      for (int countTwo{ 0 }; count >= countTwo; ++countTwo){
        sum += extendedTerms[countTwo];
      }
      partialSums[count] = sum;
    }

    int metaSum = 0;

    for (int count{ 0 }; termLen-1 >= count; ++count) {
      metaSum += partialSums[terms[count]];
    }

    return metaSum;
}

int main()
{
    std::cout << "Testing...\n";

    assert(metaFibonacciSum(6)==74);

    std::cout << "Success!";

    return 0;
}