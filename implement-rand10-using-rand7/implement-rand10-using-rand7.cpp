// The rand7() API is already defined for you.
// int rand7();
// @return a random integer in the range 1 to 7

class Solution {
public:
    int rand10() {
        int index=INT_MAX;
        while (index>=40){
            index=rand7()-1+(rand7()-1)*7;
        }
        return 1+(index%10);
    }
};