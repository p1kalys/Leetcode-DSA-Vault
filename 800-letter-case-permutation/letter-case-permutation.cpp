class Solution {
    vector<string>ans;
     void solve(string s,string cur, int n ){
         if (cur.size()==s.size()){
             ans.push_back(cur);
             return;
         }
         if (s[n]>='0' && s[n]<='9'){
             solve(s,cur+s[n],n+1);
         }
         else{
             solve(s,cur+(char)(toupper(s[n])),n+1);
             solve(s,cur+(char)(tolower(s[n])),n+1);
         }
     }
public:
    vector<string> letterCasePermutation(string s) {
        string cur="";
        solve(s,cur,0);
        return ans;
    }
};