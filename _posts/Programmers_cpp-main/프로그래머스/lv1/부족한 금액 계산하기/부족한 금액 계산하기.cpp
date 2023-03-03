using namespace std;

long long solution(int price, int money, int count)
{
    long long answer = 0;
    for (int i = 1; i <= count; i++)
    {
        answer += price * i;
    }
    answer = answer - money;
    if (answer < 0)
    {
        return answer = 0;
    }
    return answer;
}