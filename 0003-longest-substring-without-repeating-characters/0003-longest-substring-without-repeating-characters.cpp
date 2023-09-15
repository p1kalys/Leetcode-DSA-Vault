class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char>c;
        int l=0,res=0;
        for(int r=0; r<s.size();r++){
            while (c.find(s[r])!=c.end()){
                c.erase(s[l]);
                l+=1;
            }
            c.insert(s[r]);
            res = max(res, r-l+1);
        }
        return res;
    }
};

