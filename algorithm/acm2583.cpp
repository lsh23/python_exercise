#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
int m,n,k;
int plane[100][100] = {0};
int visited[100][100] = {0};
int _nx[4] = {0,1,-1,0};
int _ny[4] = {1,0,0,-1};

int dfs(int x, int y){

  int cnt = 1;

  for(int i = 0 ; i < 4 ;i ++){
    int nx = x + _nx[i];
    int ny = y + _ny[i];

    if(nx < 0 || ny < 0 || nx >= m || ny >=k)
      continue;
    //다음 좌표가 범위를 벗어나면 아무것도 하지않음
    if(plane[nx][ny] || visited[nx][ny])
      continue;
    // 범위를 벗어나지 않지만 조사대상이아니거나 조사 된 곳이면 패스
    visited[nx][ny]++;
    cnt += dfs(nx,ny);
  }

  return cnt;
}


int main(void){
  int i,j;
  scanf("%d %d %d",&m ,&n ,&k);

  int x1,y1,x2,y2;
  int l;

  for(l = 0 ; l < k ; l++){
    scanf("%d %d %d %d", &y1,&x1,&y2,&x2);
    for(i = x1;i<x2;i++)
      for(j = y1;j<y2; j++)
          plane[i][j] = 1;
  }

  vector<int> v;

  for(i = 0 ; i < m ; i++){
    for(j = 0 ; j < n ; j ++ )
      if(!plane[i][j]&&!visited[i][j]){
        visited[i][j]++;
        v.push_back(dfs(i,j));

      }
  }

  sort(v.begin(),v.end());

  for(i = 0 ; i < m ; i++){
    for(j = 0 ; j < n ; j ++ )
      printf("%d ", plane[i][j] );
    printf("\n");
  }

  printf("-------------\n");
  for(i = 0 ; i < m ; i++){
    for(j = 0 ; j < n ; j ++ )
      printf("%d ", visited[i][j] );
    printf("\n");
  }

  printf("-------------\n");
  for(i = 0 ; i < k ; i++){
    cout << v[i] << " ";
  }


  return 0;
}
