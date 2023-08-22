class Solution {
public:
    string convertToTitle(int n) {
        string s="";
        while(n>0)
        {     
              int temp = n%26 ;
              char t;
              if(temp == 0)t = 'Z';
              else t = temp-1+'A';
    
              n=(n-1)/26;
              s=t+s;

        }
        return s;
    }
};