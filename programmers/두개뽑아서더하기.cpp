#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer;
    int n = numbers.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            answer.push_back(numbers[i] + numbers[j]);
        }
    }
    sort(answer.begin(), answer.end());
    answer.erase(unique(answer.begin(), answer.end()), answer.end());

    for (int i = 0; i < answer.size(); i++) {
        printf("%d", answer[i]);
    }
    return answer;
}