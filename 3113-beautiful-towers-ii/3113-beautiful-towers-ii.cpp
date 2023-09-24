class Solution {
public:
    long long solve(vector<int> &arr , int idx){
        long long ans = arr[idx] ;
        int prev = arr[idx] , next = arr[idx] ;
        for(int i=idx+1 ; i<arr.size() ; i++){
            prev = min(prev , arr[i]) ;
            ans += prev ;
        }
        for(int i = idx-1 ; i>= 0 ; i--){
            next = min(next , arr[i]) ;
            ans += next ;
        }
        return ans ;
    }
    long long maximumSumOfHeights(vector<int>& arr) {
        long long ans = 0 ;
        for(int i = 0 ; i < arr.size() ; i++){
            if(i>0){
                if(arr[i]<arr[i-1]){
                    continue;
                }
                if(i!=arr.size()-1 && arr[i]>=arr[i-1] && arr[i]<=arr[i+1]){
                    continue;
                }
            }
            ans = max(ans , solve(arr , i)) ;
        }
        return ans ;
    }
};