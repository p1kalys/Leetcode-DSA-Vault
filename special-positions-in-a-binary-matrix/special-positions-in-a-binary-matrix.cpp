class Solution {
public:
    int numSpecial(vector<vector<int>>& mat) {
        int m=mat.size();
        int n=mat[0].size();
        vector<int> rowmat(m),colmat(n);
        int res=0;
        for(int i=0; i < m; i++){
            for(int j=0; j < n; j++){
                rowmat[i]=rowmat[i]+mat[i][j];
                colmat[j]=colmat[j]+mat[i][j];
            }
        }
        for(int i=0; i < m; i++){
            for(int j=0; j < n; j++){
                if (rowmat[i]==1 and colmat[j]==1 and mat[i][j]){
                    res+=1;
                }
            }
        }
        return res;
    }
};