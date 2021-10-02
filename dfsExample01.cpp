#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#define MAX 1000

using namespace std;

int n, m = 0;
int map[MAX][MAX];

int dx[4] = { 0,-1,0,1};
int dy[4] = { -1,0,1,0};

void input() {
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%1d", &map[i][j]);
		}
	}
}

void dfs(int x, int y) {
	map[x][y] = 2;

	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];

		if (nx < 0 || ny < 0 || nx >= n || ny >= m) {
			continue;
		}

		if (map[nx][ny] == 0) {
			dfs(nx, ny);
		}
	}
}

int main() {
	int res = 0;
	input();

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (map[i][j] == 0) {
				dfs(i, j);
				res++;
				
			}
			
		}
	}
	printf("%d", res);

	return 0;
}

/*
4 5
00110
00011
11111
00000
*/