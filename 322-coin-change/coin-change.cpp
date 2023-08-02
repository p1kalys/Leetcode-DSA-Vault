class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> v(amount+1, amount+1);
        v[0]=0;
        for (int i = 1; i <= amount; ++i)
            for(int c : coins)
                if (i - c >= 0)
                    v[i] = min(v[i], v[i-c] + 1);
        return v[amount] > amount ? -1 : v[amount];
    }
};