class Solution {
public:
    int maximalNetworkRank(int n, vector<vector<int>>& roads) {
        vector<int> adj[n];
        set<pair<int,int>> s;
        for(auto x:roads){
            adj[x[0]].push_back(x[1]);
            adj[x[1]].push_back(x[0]);
            s.insert({x[0],x[1]});
            s.insert({x[1],x[0]});
        }
        int rank=0;
        for(int i=0;i<n-1;i++){
            for(int j=i+1;j<n;j++){
                int cnt=adj[i].size()+adj[j].size();
                if(s.find({i,j})!=s.end()){
                    cnt--;
                }
                rank=max(rank,cnt);
            }
        }
        return rank;
    }
};