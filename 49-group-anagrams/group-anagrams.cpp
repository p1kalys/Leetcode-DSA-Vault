class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>>ans;
        unordered_map<string, vector<string>>map;

        for (auto x : strs) {
            string temp = x;
            sort(x.begin(), x.end());
            map[x].push_back(temp);
        }

        for ( auto x : map) {
            ans.push_back(x.second);
        }

        return ans;

    }
};