#include <iostream>
#include <algorithm>

using namespace std;

bool compare(int a, int b){
  return a > b;
}

int main(void){
  int a[10] = {10 , 3, 5 , 2 , 14, 20 ,7 , 9 ,13, 17};
  sort(a, a+10 , compare);
  for(int i = 0; i < 10; i ++){
    cout << a[i] << ' ';
  }
}
