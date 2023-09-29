class Solution {
    bool isPossible(int mid, vector<int>& position, int m){
        int balls=1;
        int Lastplacedball=position[0];
        for(int i=1; i<position.size(); i++){
            if (position[i]-Lastplacedball >=mid){
                balls++;
                Lastplacedball=position[i];
            }
        }
        if (balls>=m){
                return true;
            }
        return false;
    }
public:
    int maxDistance(vector<int>& position, int m) {
        int n=position.size();
        sort(position.begin(),position.end());
        int l=1;
        int hi=position[n-1]-position[0];
        while (l<=hi){
            int mid=l+(hi-l)/2;
            if (isPossible(mid,position,m)){
                l=mid+1;
            }
            else{
                hi=mid-1;
            }
        }
        return hi;
    }

};