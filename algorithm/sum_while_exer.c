#include <stdio.h>

int sumof(int n , int k)
{
  int sum;
  sum = 0;
  while(n<=k)
  {
    sum = sum + n;
    n++;
  }
  printf("%d부터 %d 까지 의 합은 %d 입니다.\n" ,n ,k ,sum);

  return sum;
}

int main(void) {
  int n , k ;
  puts("n부터 k까지의 합을 구합니다.");
  printf("n의 값 : ");
  scanf("%d", &n);
  printf("k의 값 : ");
  scanf("%d", &k);
  sumof(n,k);
  return 0;
}
