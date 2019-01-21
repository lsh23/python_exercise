#include <stdio.h>


int mid3(int a , int b , int c)
{
  if ( a >= b)
    if (b >= c)
      return b;
    else if (a <= c)
      return a;
    else
      return c;
  else if ( a > c )
    return a;
  else if ( b > c )
    return c;
  else
    return b;
}

int main(void)
{
  int a, b, c;
  int mid;
  printf("세 정수의 중앙값을 구합니다.\n");
  printf("a 의 값 : "); scanf("%d", &a);
  printf("b 의 값 : "); scanf("%d", &b);
  printf("c 의 값 : "); scanf("%d", &c);


  printf("중앙값은 %d 입니다. \n", mid3(a,b,c));

  return 0;
}
