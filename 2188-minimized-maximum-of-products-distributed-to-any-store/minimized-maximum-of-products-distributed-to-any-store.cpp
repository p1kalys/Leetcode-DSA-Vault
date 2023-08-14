class Solution {
public:
bool check(int mid, int n, vector<int> &quantities){
    int count = 0;
    for(int i=0;i<quantities.size();i++){
        if(quantities[i]%mid==0){
            count+=quantities[i]/mid;
        }
        else{
            count= count+(quantities[i]/mid)+1;
        }
    }
    if(count<=n) return true;
    return false;
}
    int minimizedMaximum(int n, vector<int>& quantities) {
        int low = 1;
        int high = *max_element(quantities.begin(), quantities.end());
        int res = -1;

        while(low<=high){
            int mid = low-(low-high)/2;
            if(check(mid, n, quantities)){
                res = mid;
                high = mid-1;
            }
            else{
                low = mid+1;
            }
        }
        return res;
    }
};