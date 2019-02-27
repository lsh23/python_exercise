#include<iostream>
#include<vector>
#include<queue>

using namespace std;

int n, m, v;
int graph[1001][1001] = { 0 };
int visited[1001] = { 0 };
vector<int> vec;
queue<int> que;

void reset_visited(int n) {
	for (int i = 1; i<=n; i++)
		visited[i] = 0;
}

void bfs(int _v) {
	//방문했다하고 오름차순으로 증가하면서 인접하면 그곳으로
	visited[_v]++;
	vec.push_back(_v);
	for (int i = 1; i <= n; i++) {
		if (graph[_v][i] && !visited[i]) {
			visited[i]++;
			que.push(i);
		}
		else
			continue;
	}

	if (!que.empty()) {
		int front = que.front();
		que.pop();
		bfs(front);
	}
	else
		return;
		//조금 이상하게 작성하긴함 그냥 재귀말고 while문으로 작서하는것이 일반적이였음
}

void dfs(int _v) {
	//방문했다하고 오름차순으로 증가하면서 인접하면 그곳으로
	visited[_v]++;
	vec.push_back(_v);
	for (int i = 1; i <= n; i++) {
		if (graph[_v][i] && !visited[i]) {
			dfs(i);
		}
		else
			continue;
	}
}

int main(void) {
	int i;
	int v1, v2;
	scanf("%d %d %d", &n, &m, &v);
	for (i = 0; i<m; i++) {
		scanf("%d %d", &v1, &v2);
		graph[v1][v2]++;
		graph[v2][v1]++;
	}// 그래프 구성

	dfs(v);
	reset_visited(n);
	for (i = 0; i<n; i++) {
		cout << vec[i] << " ";
	}
	cout << "\n";
	bfs(v);

	for (; i < vec.size(); i++) {
		cout << vec[i] << " ";
	}




	return 0;
}
