class Solution {
public:
    bool help ( string s, int i , unordered_set<string>& words ,  vector<int>&dp ) 
    {
        if( i == s.size() ) return true ;
        if( dp[i]!=-1 ) return dp[i];
        string t = "";
        bool ans = false ; 
        for(int j = i ; j < s.size(); j ++ )
        {
            t += s[j];
            if(words.find(t)!=words.end())
            {
                ans |= help( s , j + 1 , words,dp ) ;
            }
            if( ans ) return  dp[i] = ans ;
        }
        return dp[i] =  ans ; 
    }
   
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<int>dp(s.size(),-1);
         unordered_set<string> dict(wordDict.begin(), wordDict.end());
        return help(s,0,dict,dp) ; 
    }
};