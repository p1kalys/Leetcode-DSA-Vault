class Solution {
public:
    vector<int> evenOddBit(int n) {
        int o=0,e=0;
        while(n){
            if(n&1)e++;
            n>>=1;
            if(n==0)break;
            if(n&1)o++;
            n>>=1;
        }
        return {e,o};
    }
};