class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> res;
        res.push_back( 0 );
        for( int k = 0; k<n; k++ ) {
            int i = res.size(), t = (1<<k) ;
            while( i ) {
                int temp = res[--i] | t;
                res.push_back( temp );
            }
        }
        return res;    
    }
};