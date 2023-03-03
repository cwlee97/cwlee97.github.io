#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<string> keymap, vector<string> targets) {
    vector<int> answer;
    for(int i = 0; i < targets.size(); i++)
    {
        int min = 0;
        for (int k = 0; k < targets[i].size(); k++)
        {
            int temp = 0;
            for(int j = 0; j < keymap.size(); j++)
            {
                if (j == 0) temp = keymap[j].find(targets[i][k]);
                else if (temp > (keymap[j].find(targets[i][k]))) 
                {
                    temp = keymap[j].find(targets[i][k]);
                }
            } 
            if (temp == string::npos)
            {
                answer.push_back(-1);
                break;
            }
            else min += (temp + 1);
        }
        if ((i+1) != answer.size()) answer.push_back(min);
    }
    return answer;
}