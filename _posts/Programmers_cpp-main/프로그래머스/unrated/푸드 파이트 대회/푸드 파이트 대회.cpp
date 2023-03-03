#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<int> food) {
    string answer = "";
    for(int i = 1; i < food.size();i++)
    {
        int temp = food[i] / 2;
        for (int j = 0; j < temp; j++)
        {
            answer.append(to_string(i));
        }
    }
    std::string r_answer = answer;
    std::reverse(r_answer.begin(), r_answer.end());
    answer += "0";
    answer += r_answer;
    return answer;
}