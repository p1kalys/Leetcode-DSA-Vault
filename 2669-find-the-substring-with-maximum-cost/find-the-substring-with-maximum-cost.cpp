class Solution {
public:
    int maximumCostSubstring(string s, string chars, vector<int>& vals) {
        vector<int>sc(26,2000);
        
        for(int i=0;i<chars.size();i++)
            sc[chars[i]-'a']=vals[i];
        
        for(int i=0;i<26;i++)
        {
            if(sc[i]==2000)
                sc[i]=i+1;
        }
        
        int ans=0;
        int sum=0;
        
        for(int i=0;i<s.size();i++)
        {
            sum+=sc[s[i]-'a'];
            ans=max(ans,sum);
            
            if(sum<0)
                sum=0;
        }
        return ans;
    }
};