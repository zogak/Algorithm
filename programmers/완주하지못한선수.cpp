#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    unordered_map <string, int> p;
    for (string name : participant) {
        p[name]++;
    }
    for (string com : completion) {
        p[com]--;
    }
    for (auto a : p) {
        if (a.second > 0) {
            answer = a.first;
            break;
        }
    }
    return answer;
}