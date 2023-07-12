class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        vector<pair<int,int>>pairs;
        vector<string>ans;
        for(int i=0;i<names.size(); i++){
            pairs.push_back({heights[i],i});
        }
        sort(pairs.begin(),pairs.end(),greater<pair<int,int>>());
        for(auto i: pairs){
            ans.push_back(names[i.second]);
        }
        return ans;
    }
};