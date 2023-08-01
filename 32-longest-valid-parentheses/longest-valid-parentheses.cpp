class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int>st;
        int n=s.size();
        for(int i=0;i<n;i++){
            if (s[i]=='('){
                st.push(i);
            }
            else{
                if(!st.empty()){
                s[st.top()]='1';
                s[i]='1';
                st.pop();
                }
            }
        }
        int res=0,count=0;
        for(int j=0;j<n;j++){
            if (s[j]=='1'){
                count++;
            }
            else{
                res=max(res,count);
                count=0;
            }
        }
        res=max(res,count);
        return res;
    }
};