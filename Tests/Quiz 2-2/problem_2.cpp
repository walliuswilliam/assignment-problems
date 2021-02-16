# include <iostream>
# include <cassert>

int seqSum(int x)
{
  int sumArr [x+1]{};
  
  for(int count = 0; x >= count ; ++count){
    if (count == 0 || count == 1){
        sumArr[count] = count;
      }
    else{
        sumArr[count] = sumArr[count-1] + 2*sumArr[count-2];
      }
  }

  int sumArrLen = sizeof(sumArr)/sizeof(sumArr[0]);
  int sum = 0;

  for(int count = 0; sumArrLen > count; count++){
    sum = sum + sumArr[count];
  }

  return sum;
}

int extendedSeqSum(int x)
{
  int sumArr [x]{};
  
  for(int count = 0; x >= count ; ++count){
    if (count == 0 || count == 1){
        sumArr[count] = count;
      }
    else{
        sumArr[count] = sumArr[count-1] + 2*sumArr[count-2];
      }
  }

  int sumArrLen = sizeof(sumArr)/sizeof(sumArr[0]);
  int sum = 0;

  for(int count = 0; sumArrLen > count; count++){
    sum = sum + sumArr[count];
  }

  int extendedSum;
  extendedSum = seqSum(sum);

  return extendedSum;
}



int main()
{
    std::cout << "Testing...\n";

    assert(seqSum(0)==0);
    assert(seqSum(3)==5);
    assert(seqSum(8)==170);

    assert(extendedSeqSum(2)==1);
    assert(extendedSeqSum(4)==21);

    std::cout << "Success!";

    return 0;
}