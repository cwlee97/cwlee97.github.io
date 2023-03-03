#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    int temp1[sizes.size()], temp2[sizes.size()];
    for (int i = 0; i < sizes.size(); i++)
    {
        if (sizes[i][0] > sizes[i][1])
        {
            temp1[i] = sizes[i][0];
            temp2[i] = sizes[i][1];
        }
        else
        {
            temp1[i] = sizes[i][1];
            temp2[i] = sizes[i][0];
        }
    }
    int x = temp1[0];
    int y = temp2[0];
    for (int i = 1; i < sizes.size(); i++)
    {
        if (x < temp1[i])
            x = temp1[i];
        if (y < temp2[i])
            y = temp2[i];
    }
    answer = x * y;
    return answer;
}