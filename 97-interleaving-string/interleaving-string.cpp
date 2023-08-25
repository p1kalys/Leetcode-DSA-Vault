class Solution {
public:
    int solve(int index1 , int index2 , int index3 , int n , int m ,  string& s1 , string &s2 , string &s3 , vector<vector<int>> &dp)
    {
        if(index1==n && index2==m)
        {
            return 1;
        }
        if(index1>=n && index2 >=m) return 0;
        
        if(dp[index1][index2]!=-1) return dp[index1][index2];

        //when both values are equal and match
        if(index1<n && index2<m && s1[index1]==s3[index3] && s2[index2]==s3[index3])
        {
            return dp[index1][index2]=solve(index1+1 , index2 , index3 +1, n , m , s1 , s2 , s3 , dp) || solve(index1, index2 + 1 , index3 + 1, n , m, s1 , s2 , s3 , dp); 
        }

        else if( index1<n && s1[index1]==s3[index3])
        {
            return dp[index1][index2] = solve(index1+1 , index2 , index3+1 ,n , m , s1 , s2, s3 , dp);
        }

        else if(index2<m && s2[index2]==s3[index3])
        {
            return dp[index1][index2]=solve(index1 , index2+1 , index3+1 , n , m , s1 , s2, s3 , dp);
        }
        else
        {
            return dp[index1][index2]=0;
        }
    }
    bool isInterleave(string s1, string s2, string s3) {
        int n = s1.size();
        int m = s2.size();
        int o = s3.size();
        if(n+m!=o) return false;
        vector<vector<int>> dp(n+1 , vector<int> (m+1 , -1));
        return solve(0 , 0 , 0 , n , m , s1 , s2 , s3 , dp);
    }
};