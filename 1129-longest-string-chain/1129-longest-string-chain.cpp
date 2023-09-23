class Solution {
public:
    bool check(string s1, string s2) {
        if (s1.size() != s2.size()+1) {
            return false;
        }
        int i = 0, j = 0;
        while (i<s1.size()) {
            if (j<s2.size() && s1[i]==s2[j]){
                i++;
                j++;
            }
            else {
                i++;
            }
        }
        if (i==s1.size() && j==s2.size()) {
            return true;
        }
        else {
            return false;
        }

    }

    static bool cmp(string s1, string s2){
        return s1.size()<s2.size();
    }
    int longestStrChain(vector<string>& words) {
        sort(words.begin(),words.end(),cmp);
        int n=words.size();
        vector<int>dp(n,1);
        int maxi = 0;
        for(int i=0; i<n; i++) {
            for(int prev=0; prev<i;prev++){
                if (check(words[i],words[prev]) && dp[i]<dp[prev]+1) {
                    dp[i] = dp[prev]+1;
                }
            }
            maxi = max(maxi, dp[i]);
        }
        return maxi;
    }
};