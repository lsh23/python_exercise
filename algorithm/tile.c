#include <stdio.h>

int d[1001];

int dp(int x) {
    if(x==1) return 0;
    if(x==2) return 3;
    if(x==4) return 11;
    if(x%2!=0) return d[x] = 0;
    if(d[x] != 0) return d[x];
    return d[x] = (dp(x-2)*3 + dp(x-4)*2);
}

int main(void){
    int x;
    scanf("%d", &x);
    printf("%d", dp(x));
}
