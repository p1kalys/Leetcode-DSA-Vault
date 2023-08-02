class Solution {
public:
    int getSum(int a, int b) {
       if (b == 0)
        return a;
    else
        return getSum( a ^ b,(unsigned) (a & b) << 1);
    }
};