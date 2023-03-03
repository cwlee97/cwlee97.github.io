#include <string>
#include <vector>

using namespace std;

int solution(int left, int right) {
    int answer = 0;
    for (int i = left; i <= right; i++)
    {
        int  temp = 0;
        for (int j = 1; j * j <= i; j++)
        {
            if (j * j == i) temp += 1;
            else if (i % j == 0) temp += 2;
        }
        if (temp % 2 == 0) answer += i;
        else answer -= i;
    }
    return answer;
}