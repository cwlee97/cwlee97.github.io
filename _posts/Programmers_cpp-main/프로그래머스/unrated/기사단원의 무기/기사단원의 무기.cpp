#include <string>
#include <vector>

using namespace std;

int solution(int number, int limit, int power) {
    int answer = 0;
    vector<int> list;
    for(int i = 1; i <= number; i++)
    {
        if (i == 1) list.push_back(1);
        else
        {
            int temp = 0;
            for (int j = 1; j * j <= i; j++)
            {
                if (j * j == i) temp += 1;
                else if (i % j == 0) temp += 2;
            }
            list.push_back(temp);
        }
    }
    for (int k = 0; k < list.size(); k++)
    {
        if (list[k] > limit) answer += power;
        else answer += list[k];
    }
    return answer;
}