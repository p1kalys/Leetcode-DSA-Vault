class Solution {
public:
    string reverseWords(string s) {
        int n = s.length();
        int left = 0;
        int right = 0;

        while (right < n) {
            while (right < n && s[right] != ' ') {
                right++;
            }

            //when copy = right, right is = ' '
            int copy = right; 
            //so we move back one place so it is the end of the substring.
            copy--;

            //swap characters from the left to right of the substring.
            while(left < copy){
                swap(s[left], s[copy]);
                left++;
                copy--;
            }

            //set left to be right+1 so to the right of the ' ' whitespace. 
            left = right+1;
            right = left; 
        }

        return s;
    }
};