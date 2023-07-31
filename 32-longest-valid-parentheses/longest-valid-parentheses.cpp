class Solution {
public:
    int longestValidParentheses(string s) 
    {
        stack<int>st;
        for(int i = 0; i < s.size(); i++)
        {
            if(s[i] == '(') st.push(i);
            else
            {
                if(!st.empty() && s[st.top()] == '(') st.pop();
                else st.push(i);
            }
        }
        int res = 0;
        if(!st.empty()) res = s.size() - st.top() - 1;
        else if(st.empty()) return s.size();
        while(!st.empty())
        {
            int top = st.top() - 1;
            st.pop();
            if(!st.empty()) top -= st.top();
            else top += 1;
            res = max(res , top);
        }
        return res;
    }
};