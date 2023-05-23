#include <iostream>

double function(int n){
    if (n == 0){
        return 1;
    }
    else{
        return (((double) n / (double)(n + 2)) - 10) * function(n - 1);
    }
}
double function1() {
    std::cout << "Enter the number: " << std::endl;
    int number;
    std::cin >> number;
    double sum = 1;
    while(number!=0){
        sum = sum * (((double) number / (double)(number + 2)) - 10);
        number--;
    }
    std::cout<< "The result: " << sum <<std::endl;
}
int main() {
    std::cout<<"Enter the number: "<< std::endl;
    int number;
    std::cin>>number;
    std::cout << "The result: " << function(number) << std::endl;
    function1();
    return 0;
}