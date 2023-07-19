class Solution {
public:
    int minimumMoves(string s) {
        int moves = 0 ; 
        int n = s.length() ; 
        int i = 0 ; 
        while (i < n)
        {
            if (s[i] == 'X')
            {
                moves ++ ;
                i += 3 ;
            }
            else
            {
                i ++ ;
            }
        }
        return moves ; 
    }
};