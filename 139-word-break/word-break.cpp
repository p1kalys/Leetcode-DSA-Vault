class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<bool> dp(s.size()+1, false);
        dp[0] = true;

        for(int i = 0; i < s.size(); i++){
            if(!dp[i]) continue;
            for(auto word: wordDict){
                if(s.substr(i, word.length()) == word && i + word.length() <= s.size()){
                    dp[i + word.length()] = true;
                }
            }
        }

        return dp[s.size()];
    }
};