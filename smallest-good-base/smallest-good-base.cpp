class Solution {
    unsigned long long mysolve(unsigned long long n, int d) {
        double tn = (double)n;
        unsigned long long right = (unsigned long long)(pow(tn, 1.0 / d) + 1);
        unsigned long long left = 1;
        while (left <= right)
        {
            unsigned long long mid = left + (right - left) / 2;
            unsigned long long sum = 1, cur = 1;
            for (int i = 1; i <= d; i++)
            {
                cur *= mid;
                sum += cur;
            }
            if (sum == n)
                return mid;
            if (sum > n)
                right = mid - 1;
            else
                left = mid + 1;
        }
        return 0;
    }

public:
    string smallestGoodBase(string n) {
        unsigned long long tn = (unsigned long long)stoll(n);
        unsigned long long x = 1;
        for (int i = 62; i >= 1; i--)
        {
            if ((x << i) < tn)
            {
                unsigned long long cur = mysolve(tn, i);
                if (cur != 0)
                    return to_string(cur);
            }
        }
        return to_string(tn - 1);
    }
};