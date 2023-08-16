class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        int n = words.size();
        vector<string> ans;
        int i = 0;
        while( i < n){
            int len = words[i].size();
            int j = i + 1;
            while( j < n && len + words[j].size() + (j-i) <= maxWidth){
                len += words[j].size();
                j++;
            }

            int numWords = j-i;
            int numSpaces = maxWidth - len;
            string line;

            if(numWords == 1 || j == n){
                line = words[i];
                for(int k = i + 1 ;k < j;k++){
                    line += ' ' + words[k];
                }
                line += string(maxWidth - line.size(),' ');
            }else{
                int spacesBtwnWords = numSpaces / (numWords - 1);
                int extraSpaces = numSpaces % (numWords - 1);
                line = words[i];
                for(int k = i + 1;k<j;k++){
                    line += string(spacesBtwnWords,' ');
                    if(extraSpaces){
                        line += ' ';
                        extraSpaces--;
                    }
                    line += words[k];
                }
            }
            ans.push_back(line);
            i= j;
        }
        return ans;
    }
};