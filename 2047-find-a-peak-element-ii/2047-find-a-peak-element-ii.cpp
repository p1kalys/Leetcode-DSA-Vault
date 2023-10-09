class Solution {
public:
    int max_index(vector<int>& matMid){
        int maxxi = INT_MIN;
        int res=0;
        for(int i=0;i<matMid.size();i++){
            if(matMid[i]>maxxi){
                maxxi = matMid[i];
                res = i;
            }
        }
        return res;
    }
    vector<int> findPeakGrid(vector<vector<int>>& mat) {
        vector<int> res;
        int low=0;
        int high=mat.size()-1;
        while(low<=high){
            int mid = low + (high-low)/2;
            int maxxi = max_index(mat[mid]);
            if( ((mid-1>=0)?mat[mid][maxxi]>mat[mid-1][maxxi]:1) && ((mid+1<mat.size())?mat[mid][maxxi]>mat[mid+1][maxxi]:1) ){
                res.push_back(mid);
                res.push_back(maxxi);
                return res;
            }
            else if((mid-1>=0)?mat[mid][maxxi]<=mat[mid-1][maxxi]:0){
                high=mid-1;
            }
            else{
                low=mid+1;
            }
        }
        return res;
    }
};