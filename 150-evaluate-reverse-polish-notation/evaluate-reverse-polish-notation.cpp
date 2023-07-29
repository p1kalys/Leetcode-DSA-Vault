class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        int n=tokens.size();
        stack<int>s;
        for(int i=0; i<n; i++){
            if (tokens[i]=="+"){
                int ele1=s.top();s.pop();
                int ele2=s.top();s.pop();
                s.push(ele1+ele2);
            }
            else if (tokens[i]=="-"){
                int ele1=s.top();s.pop();
                int ele2=s.top();s.pop();
                s.push(ele2-ele1);
            }
            else if (tokens[i]=="*"){
                int ele1=s.top();s.pop();
                int ele2=s.top();s.pop();
                s.push(ele1*ele2);
            }
            else if (tokens[i]=="/"){
                int ele1=s.top();s.pop();
                int ele2=s.top();s.pop();
                s.push(ele2/ele1);
            }
            else{
                int k=stoi(tokens[i]);
                s.push(k);
            }
        }
        return s.top();
    }
};