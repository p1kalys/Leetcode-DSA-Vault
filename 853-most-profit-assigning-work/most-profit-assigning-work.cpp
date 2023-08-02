class Solution {
public:
    int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
        vector<pair<int, int>> dif;
        for(int i=0;i<difficulty.size();i++){
            dif.push_back({profit[i], difficulty[i]});
        }
        sort(dif.rbegin(), dif.rend());
        sort(worker.rbegin(), worker.rend());
        int i=0, j=0,ans=0;
        while(i<worker.size() && j<dif.size()){
            if(worker[i]>=dif[j].second){
                ans+=dif[j].first;
                i++;
            }
            else j++;
        }
        return ans;
    }
};