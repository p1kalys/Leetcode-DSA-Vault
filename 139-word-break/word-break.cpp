class Solution {
public:

    bool check( vector<string>& words , string t )
    {
        auto it = find( words.begin() , words.end(),t )  ; 

        if( it == words.end() ) return false ; 

        else return true ;
    }
    
    bool help ( string s, int i , vector<string>& words ,  vector<int>&dp ) 
    {
         if( i == s.size() ) return true ;

         if( dp[i]!=-1 ) return dp[i];

         string t = "";

        bool ans = false ; 

         for(int j = i ; j < s.size(); j ++ )
         {
             t += s[j];

             if( check(words,t) )
             {
                 ans |= help( s , j + 1 , words,dp ) ;
             }

             if( ans ) return  dp[i] = ans ;

         }

        return dp[i] =  ans ; 

    }
   
    bool wordBreak(string s, vector<string>& wordDict) {

        vector<int>dp(s.size(),-1);
        
        return help(s,0,wordDict,dp) ; 

    }
};