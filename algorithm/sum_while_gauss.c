#include <stdio.h>

int main(void)
{
  int i , n;
  int sum;
  puts("1부터 n까지의 합을 구합니다.");
  printf("n의 값 : ");
  scanf("%d", &n);
  sum = 0;
  i = 1;

  sum = (i+n)*(n-i+1)/2 ;

  printf("1부터 %d 까지 의 합은 %d 입니다.\n" , n , sum );

  return 0;
}
