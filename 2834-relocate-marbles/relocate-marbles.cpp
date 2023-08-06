class Solution {
public:
    vector<int> relocateMarbles(vector<int>& nums, vector<int>& moveFrom, vector<int>& moveTo) {
        set<int> st;
        for(int i=0;i<nums.size();i++)
        st.insert(nums[i]);

        for(int i=0;i<moveFrom.size();i++)
        {
            if(st.count(moveFrom[i]))
            {
                st.erase(moveFrom[i]);
                st.insert(moveTo[i]);
            }
        }
        vector<int> ans;
        for(auto i:st)
        {
            ans.push_back(i);
        }

        return ans;
    }
};