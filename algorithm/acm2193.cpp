#include<iostream>

using namespace std;

long long x[91][2];

void dp(int n){
  if(n==1) {x[1][0] = 0; x[1][1] = 1; return;}
  dp(n-1);
  x[n][0] = x[n-1][1] + x[n-1][0];
  x[n][1] = x[n-1][0];
}

int main(void){
  dp(90);
  int n;
  scanf("%d",&n);
  printf("%lld", x[n][0]+x[n][1]);

  return 0;
}
