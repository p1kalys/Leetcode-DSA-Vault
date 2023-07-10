class Solution {
    vector<string>ans;
public:
    vector<string> generateParenthesis(int n) {
        generate(0, 0, n, "");
        return ans;
    }

    void generate(int open, int close, int n, string s)
    {
    if (s.size() == 2 * n)
        ans.push_back(s);
    if (open < n)
        generate(open + 1, close, n, s + "(");
    if (close < open)
        generate(open, close + 1, n, s + ")");
    }
};