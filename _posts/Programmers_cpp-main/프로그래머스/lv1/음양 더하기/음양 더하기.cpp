#include <string>
#include <vector>

using namespace std;

int solution(vector<int> absolutes, vector<bool> signs) {
    int answer = 0;
    for(int i; i < absolutes.size(); i++)
    {
        int temp = 0;
        if (signs[i] == true) temp = absolutes[i];
        else  temp = absolutes[i] * -1;
        answer += temp;
    }
    return answer;
}