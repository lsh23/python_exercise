#include<iostream>
#include<vector>
using namespace std;

vector<int> stu;
vector<int> visited;
vector<int> checked;
vector<int> ans;

void dfs(int n){
}

int main(void){

  int i,j,t,n;
  scanf("%d",&t);
  vector<int> a(t,0);

  for(i=0;i<t;i++){
      scanf("%d",%n);
      stu.clear(); stu.resize(n+1);
      for(j=1;j<=n;j++){
        cin >> stu[j];
      }
      stu.clear(); visited.resize(n+1);

      a[i] = dfs();
      //결과를 a[i]에 저장.
  }


  for(i=0;i<t;i++){
    printf("%d\n",a[i]);
  }
      //테스트 케이스 수 개수 만큼 결과 출력
  return 0;
}
