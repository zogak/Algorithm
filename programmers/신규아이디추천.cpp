#include <iostream>
#include <string>
#include <vector>

using namespace std;
bool isAlpha(char c) {
    if (c >= 'a' && c <= 'z') {
        return true;
    }
    return false;
}
bool isNum(char c) {
    if (c >= '0' && c <= '9') {
        return true;
    }
    return false;
}
string solution(string new_id) {
    string answer = "";
    //step1
    for (int i = 0; i < new_id.size(); i++) {
        new_id[i] = tolower(new_id[i]);
    }
    cout << "1 : " << new_id << endl;

    //step2
    for (int i = 0; i < new_id.size(); i++) {
        if (isAlpha(new_id[i]) || isNum(new_id[i]) || new_id[i] == '-' || new_id[i] == '_' || new_id[i] == '.') {
            continue;
        }
        new_id.erase(i, 1);
        i--;
    }
    cout << "2 : " << new_id << endl;
    //step3
    for (int i = 0; i < new_id.size() - 1; i++) {
        if (new_id[i] == '.' && new_id[i + 1] == '.') {
            new_id.erase(i, 1);
            i--;
        }
    }
    cout << "3 : " << new_id << endl;

    //step4
    if (!new_id.empty() && new_id[0] == '.') {
        new_id.erase(0, 1);
    }
    if (!new_id.empty() && new_id.back() == '.') {
        new_id.erase(new_id.size() - 1);
    }
    cout << "4 : " << new_id << endl;

    //step5
    if (new_id.size() == 0) {
        new_id = "a";
    }
    cout << "5 : " << new_id << endl;

    //step6
    if (new_id.size() >= 16) {
        new_id.erase(15);
        if (new_id[14] == '.') {
            new_id.erase(14);
        }
    }
    cout << "6 : " << new_id << endl;

    //step7
    if (new_id.size() <= 2) {
        while (new_id.size() < 3) {
            new_id += new_id.back();
        }
    }
    cout << "7 : " << new_id << endl;
    answer = new_id;
    return answer;
}

int main() {
    string one = "...!@BaT#*..y.abcdefghijklm";
    string two = "z-+.^.";
    string three = "=.=";
    string four = "123_.def";
    string five = "abcdefghijklmn.p";
    cout << solution(one);
}