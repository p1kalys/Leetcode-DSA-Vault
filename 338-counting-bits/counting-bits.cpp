class Solution {
public:
    vector<int> countBits(int n) {
        vector<int>ans(n+1,0);
        int x=0;
        int b=1;
        while (b<=n){
            while(x<b && x+b <=n){
                ans[x+b] = ans[x] + 1;
                x+=1;
            }
            x=0;
            b<<=1;
        }
        return ans;
    }
};