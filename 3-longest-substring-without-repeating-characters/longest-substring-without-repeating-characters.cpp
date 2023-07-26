class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int>mpp(256,-1);
        int l=0,r=0;
        int res=0;
        while (r < s.size()){
            if (mpp[s[r]]!=-1) l=max(mpp[s[r]]+1,l);
            mpp[s[r]]=r;
            res=max(res,r-l+1);
            r++;
        }
        return res;
    }
};