class Solution { 
public:
    vector<vector<int>> findPrimePairs(int n) {
        vector<bool>sieve(n+1,true);
        vector<vector<int>>ans;
        sieve[0]=sieve[1]=false;
        for(int i=2; i*i<=n; i++){
            if (sieve[i]){
                for(int j=i*i; j<=n; j+=i){
                    sieve[j]=false;
                }
            }
        }

        for(int i=2;i<=n/2;i++){
            if (sieve[i] && sieve[n-i]){
                ans.push_back({i,n-i});
            }
        }
        return ans;
    }
};