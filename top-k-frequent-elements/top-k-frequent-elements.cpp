class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int>a;
        priority_queue<pair<int,int>>elements;
        vector<int>ans;
        for(int i=0; i<nums.size(); i++){
            a[nums[i]]++;
        }
        while (!a.empty()){
            elements.push({a.begin()->second,a.begin()->first});
            a.erase(a.begin());
        }
        for(int i=0; i<k; i++){
            ans.push_back(elements.top().second);
            elements.pop();
        }
        return ans;
    }
};