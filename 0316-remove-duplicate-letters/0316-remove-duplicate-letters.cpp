class Solution {
public:
    string removeDuplicateLetters(string s) {
        vector<int>f(26,0);
        for(auto i: s){
            f[i-'a']++;
        }
        stack<char>st;
        vector<bool>seen(26,false);
        for (int i=0; i<s.size(); i++){
            if (seen[s[i]-'a']){
                f[s[i]-'a']--;
                continue;
            }
            while(!st.empty() and f[st.top()-'a']>0 and st.top()>s[i]){
                seen[st.top()-'a']=false;
                st.pop();
            }
            st.push(s[i]);
            f[s[i]-'a']--;
            seen[s[i]-'a']=true;
        }

        string res="";
        while(!st.empty()){
            res = st.top()+res;
            st.pop();
        }
        return res;

    }
};