#include <iostream>
using namespace std;

int main(){
    int sum = 0;
    for (int i = 0;i<1000;i++){
        if (i%5 == 0){
            sum = sum+i;
        }
        else if (i%3 == 0) {
            sum = sum+i;
        }
    }
    std::cout << sum << "\n";
    return 0;
}