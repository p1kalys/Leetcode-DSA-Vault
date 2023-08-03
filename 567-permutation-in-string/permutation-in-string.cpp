class Solution {
public:
    bool equal(vector<int>a, vector<int>b){
        for(int i=0;i<26;i++){
            if (a[i]!=b[i]) return false;
        }
        return true;
    }
    bool checkInclusion(string s1, string s2) {
        //sliding window
        if (s1.size()>s2.size()) return false;
        vector<int>f1(26,0),f2(26,0);
        for(auto c:s1) f1[c-'a']++;
        int i=0,j=0;
        while(j<s2.size()){
            f2[s2[j]-'a']++;
            if (j-i+1 == s1.size()){
                if (equal(f1,f2)) return true;
            }
            if(j-i+1 <s1.size()) j++;
            else{
                f2[s2[i]-'a']--;
                i++;
                j++;
            }
        }
        return false;
    }
};