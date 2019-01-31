#include <stdio.h>

void spira(int n){

  int i, j;

  for(i = 1 ; i <= n ; i++){
    for(j = 1 ; j <= 2*n -1 ; j ++){
      if(n-i<j && j<n+i)
        putchar('*');
      else
        putchar(' ');
    }
    putchar('\n');
  }
}


void nspira(int n){

  int i, j;

  for(i = 1; i <= n ; i++){
    for(j = 1 ; j <= 2*n -1 ; j ++){
      if(n-(n-(i-1))<j && j<n+(n-(i-1)))
        printf("%d", i%10);
      else
        putchar(' ');
    }
    putchar('\n');
  }
}

int main(void){
  spira(5);
  nspira(5);


  return 0;
}
