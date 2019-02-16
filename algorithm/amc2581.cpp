#include<iostream>

using namespace std;

int prime[5000];

void makePrime(){
  int i,n;
  int ptr = 0;
  prime[ptr++] = 2;
  prime[ptr++] = 3;
  for(n=5 ; n<=10000; n+=2){
    int flag = 0;
    for(i = 1 ; prime[i]*prime[i] <= n ; i++){
      if(n%prime[i] == 0) {
        flag=1;
        break;
      }
    }
    if(!flag)
      prime[ptr++]= n;
  }
}

int main(){
  makePrime();
  int m,n;
  cin>>m>>n;
  int sum = 0;
  int min;
  int i;
  for(i=0 ; i<5000 ; i++){
    if(m<=prime[i] && prime[i]<=n){
      if(sum==0)
        min = prime[i];
      sum += prime[i];
    }
    if(prime[i]>n)
      break;
  }
  if(sum==0)
    cout << -1;
  else{
    cout << sum << "\n";
    cout << min;
  }

  return 0;
}
