class Solution {
public:
    static int f(int a){
        int counta=0;
        while(a){
            if(a&1) counta++;
            a=a>>1;
        }
        return counta;
    }
    static bool cmp(int a, int b){
        int counta=f(a);
        int countb=f(b);
        
        if (counta == countb) return a<b;
        return counta<countb;
    }

    vector<int> sortByBits(vector<int>& arr) {
        sort(arr.begin(),arr.end(), cmp);
        return arr;
    }
};