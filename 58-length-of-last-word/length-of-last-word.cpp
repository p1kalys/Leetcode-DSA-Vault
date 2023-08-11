class Solution {
public:
    int lengthOfLastWord(string s) {
        int l=0;
        int flag=0;
        for(int i=s.size()-1;i>=0;i--){
            if(s[i]!=' '){
                flag=1;
                l+=1;
            }
            else{
                if (flag) {
                    break;
                }
            }
        }
        return l;
    }
};