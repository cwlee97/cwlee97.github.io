#include <string>
#include <vector>

using namespace std;

int solution(string t, string p) {
    int answer = 0;
    long long int_p = stoll(p);
    int len = p.size();
    for (int i = 0; i <= (t.size() - p.size()); i++)
    {
        if (stoll(t.substr(i, len)) <= int_p)
        answer += 1;
    }
    return answer;
}