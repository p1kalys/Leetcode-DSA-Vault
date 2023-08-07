class Solution {
public:
    int count = 0;
    void solve(int i,vector<bool>&visited,vector<vector<int>>&rooms)
    {
        visited[i]=true;
        count++;

        if(count==visited.size())
         return;

        for(auto x:rooms[i]) 
        {
            if(visited[x]==false)
             solve(x,visited,rooms);
        }
    }
    bool canVisitAllRooms(vector<vector<int>>& rooms) 
    {
        // initially we are at room 0
        int n = rooms.size();
        vector<bool>visited(n,false);
        count=0;

        solve(0,visited,rooms);
            
       
        return (count==visited.size())?true:false;
        
    }
};