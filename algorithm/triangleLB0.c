#include <stdio.h>




void triangleLB( int n ){

    int i, j;

    for(i = 1 ; i <= n ; i++){
      for(j = 1 ; j <= i ; j ++){
        putchar('*');
      }
      putchar('\n');
    }
    printf("-------------------------------------\n");
}

void triangleLU(int n){

      int i, j;

      for(i = 1 ; i <= n ; i++){
        for(j = n ; j >= i ; j--){
          putchar('*');
        }
        putchar('\n');
      }
      printf("-------------------------------------\n");

}
void triangleRU(int n){

      int i, j;

      for(i = 1 ; i <= n ; i++){
        for(j = 1 ; j<= n ; j ++){
          if(j<i)
            putchar(' ');
          else
            putchar('*');
        }
        putchar('\n');
      }
      printf("-------------------------------------\n");

}
void triangleRB(int n){

  int i, j;

  for(i = 1 ; i <= n ; i++){
    for(j = 1 ; j<= n ; j ++){
      if(j>5-(i-1))
        putchar(' ');
      else
        putchar('*');
    }
    putchar('\n');
  }
  printf("-------------------------------------\n");

}


int main(void){
  triangleLB(5);
  triangleLU(5);
  triangleRU(5);
  triangleRB(5);
  return 0;
}
