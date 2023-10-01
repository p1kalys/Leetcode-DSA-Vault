class Solution {
public:
    string reverseWords(string s) {
        string ans;
        stack<char> st;
        s += " ";
        for(char ch : s){
            if( ch == ' ' ){
                while(!st.empty()){
                    ans.push_back(st.top());
                    st.pop();
                }
                ans += ' ';
            }
            else{
                st.push(ch);
            }
        }
        ans.pop_back();
        return ans;
    }
};