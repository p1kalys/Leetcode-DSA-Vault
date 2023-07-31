class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> res;
        vector<string>graystring = generate(n);
    
        for( auto i:graystring){
            res.push_back(stoi(i,0,2));
        }
        return res;    
    }
    vector<string> generate(int n){
        if (n==1){
            return {"0","1"};
        }
        vector<string>ans;
        vector<string>temp = generate(n-1);
        for(int i=0; i<temp.size(); i++){
            ans.push_back("0"+temp[i]);
        }
        for(int i=temp.size()-1; i>=0; i--){
            ans.push_back("1"+temp[i]);
        }
        return ans;
    }
};