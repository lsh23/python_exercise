#include <stdio.h>

int main(void)
{
  int a, b, c;
  int max;
  printf("세 정수의 최댓값을 구합니다.\n");
  printf("a 의 값 : "); scanf("%d", &a);
  printf("b 의 값 : "); scanf("%d", &b);
  printf("c 의 값 : "); scanf("%d", &c);

  max = a;
  if( b > max ) max = b;
  if( c > max ) max = c;

  printf("최대값은 %d 입니다. \n", max );

  return 0;
}
