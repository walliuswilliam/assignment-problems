#include <iostream>
#include "constants.h"

double calculateDistanceFallen(int seconds)
{
    // approximate distance fallen after a particular number of seconds
    double distanceFallen = myConstants::gravity * seconds * seconds / 2;

    return distanceFallen;
}

void printStatus(int time, double height)
{
    std::cout << "At " << time
    << " seconds, the ball is at height "
    << height << " meters\n";
}

int main()
{
    using namespace std;
    cout << "Enter the initial height of the tower in meters: ";
    double initialHeight;
    cin >> initialHeight;
    
    int time = 0;
    double height;
    height = initialHeight - calculateDistanceFallen(time);

    while (height > 0) {
      printStatus(time, height);
      time += 1;
      height = initialHeight - calculateDistanceFallen(time);
    }
    printStatus(time, 0);

    return 0;
}