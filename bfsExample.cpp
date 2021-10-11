#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

#define MAX 201
#include <queue>

using namespace std;

int n, m = 0;
int map[MAX][MAX];
int v[MAX][MAX];

queue <pair<int, int>> q;

int dx[4] = { 0,-1,0,1 };
int dy[4] = { -1,0,1,0 };


void input() {
	scanf("%d %d", &n, &m);
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			scanf("%1d", &map[i][j]);
		}
	}
}

void bfs() {
	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx<1 || ny<1 || nx>n || ny>m)
				continue;
			
			if (map[nx][ny] == 1 && v[nx][ny] == 0) {
				q.push(make_pair(nx, ny));
				v[nx][ny] = v[x][y] + 1;
			}
		}
		
	}
}

int main() {
	input();
	q.push(make_pair(1, 1));
	v[1][1] = 1;
	bfs();
	printf("%d", v[n][m]);
	return 0;
}

/*
5 6
101010
111111
000001
111111
111111
*/