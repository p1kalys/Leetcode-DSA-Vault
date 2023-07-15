class Solution {
public:
    void solve(string &digits, vector<string> &choice, vector<string> &result, string &ans, int index){

        if(ans.length() == digits.size()){
            result.push_back(ans);
            return;
        }

        int idx = digits[index] - '0';
        string temp = choice[idx-2];

        for(int i=0;i<temp.length();i++){
            
            ans.push_back(temp[i]);
            solve(digits, choice, result, ans, index+1);
            ans.pop_back();
        }

    }

    vector<string> letterCombinations(string digits) {

        if(digits.size() == 0)
            return {};

        vector<string> choice = {"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
        vector<string> result;
        string ans = "";

        solve(digits, choice, result, ans, 0);

        return result;
    }
};