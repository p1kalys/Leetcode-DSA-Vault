class Solution {
public:
    int maximumScore(int a, int b, int c) {
        int maxi = max(a,max(b,c));
        int mini = min(a,min(b,c));
        int mid = a+b+c-maxi-mini;
        if(mini+mid<=maxi) return mini+mid;

        return (a+b+c)/2;
    }
};