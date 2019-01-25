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
  while(i<=n)
  {
    sum = sum + i ;
    printf("현재 i 값 : %d , sum 값 : %d \n" , i , sum);
    i++;

  }
  printf("1부터 %d 까지 의 합은 %d 입니다.\n" , n , sum );

  return 0;
}
