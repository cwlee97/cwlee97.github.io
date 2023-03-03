#include <string>
#include <vector>
#include <set>

using namespace std;

int solution(int x, int y, int n) {
    int answer = 0;
    set<int> list = {x};
    while (true)
    {
        set<int> temp = {};
        for (auto ele : list)
        {
            if (ele == y) return answer;
            if ((ele * 2) <= y) temp.insert(ele * 2);
            if ((ele * 3) <= y) temp.insert(ele * 3);
            if ((ele + n) <= y) temp.insert(ele + n);
        }
        if (temp.size() == 0) return answer = -1;
        list = temp;
        answer += 1;
    }
}