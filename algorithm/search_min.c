#include <stdio.h>

int main(void)
{
  int a, b, c;
  int min;
  printf("세 정수의 최소값을 구합니다.\n");
  printf("a 의 값 : "); scanf("%d", &a);
  printf("b 의 값 : "); scanf("%d", &b);
  printf("c 의 값 : "); scanf("%d", &c);

  min = a;
  if( b < min ) min = b;
  if( c < min ) min = c;

  printf("최소값은 %d 입니다. \n", min);

  return 0;
}
