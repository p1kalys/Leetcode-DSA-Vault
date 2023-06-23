class Solution {
public:
    int hammingWeight(uint32_t n) {
        int res=0;
        long x=n;
        while(x){
            if (x%2==1) res++;
            x>>=1;
        }
        return res;
    }
};