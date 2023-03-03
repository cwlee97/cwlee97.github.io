#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string X, string Y) {
    string answer = "";
    for (int i = 9; i >= 0; i--)
    {
        int X_count = count(X.begin(), X.end(), char(i+48));
        int Y_count = count(Y.begin(), Y.end(), char(i+48));
        if (X_count > Y_count) 
        {
            for (int j = 0; j < Y_count; j++) answer += to_string(i);
        }
        else
        {
            for (int j = 0; j < X_count; j++) answer += to_string(i);
        }
    }
    if (answer[0] == '0') 
    {
        answer = "0";
        return answer;
    }
    if (answer == "") answer = "-1";
    return answer;
}