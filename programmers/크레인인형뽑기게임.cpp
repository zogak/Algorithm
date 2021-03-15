#include <string>
#include <vector>
#include <stack>
using namespace std;
stack <int> s;
int cnt;
int basket(int x) {
    if (s.empty() || s.top() != x) {
        s.push(x);
    }
    else if (s.top() == x) {
        s.pop();
        cnt += 2;
    }
    return cnt;
}
int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    for (int i = 0; i < moves.size(); i++) {
        int position = moves[i] - 1;
        for (int j = 0; j < board.size(); j++) {
            if (board[j][position] == 0) continue;
            else {
                answer = basket(board[j][position]);
                board[j][position] = 0;
                break;
            }
        }
    }
    return answer;
}