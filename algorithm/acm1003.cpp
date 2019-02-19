#include<iostream>
using namespace std;

int ans[41][2];

void make(int n){
  if(n==0)
    {ans[n][0] = 1; ans[n][1] = 0;
      // printf("ans[%d][0] %d ans[%d][1] %d \n", n, ans[n][0] , n ,ans[n][1]);
      return;}
  if(n==1)
    {ans[n][0] = 0; ans[n][1] = 1;
      make(0);
      // printf("ans[%d][0] %d ans[%d][1] %d \n", n, ans[n][0] , n,ans[n][1]);
return;}
  make(n-1);
  ans[n][0] = ans[n-1][0]+ans[n-2][0];
  ans[n][1] = ans[n-1][1]+ans[n-2][1];

  // printf("ans[%d][0] %d ans[%d][1] %d \n", n, ans[n][0] , n ,ans[n][1]);
}

int main(void){
  int t ,i;
  scanf("%d",&t);
  int test[t];
  for(i = 0 ; i < t ; i++){
    scanf("%d",&test[i]);
  }


  make(40);

  for(i = 0 ; i < t ; i++){
    printf("%d %d\n", ans[test[i]][0],ans[test[i]][1] );
    // printf("ans[%d][0] ans[%d][1] = %d %d\n",test[i],test[i],ans[test[i]][0], ans[test[i]][1]);
  }

  return 0;
}
