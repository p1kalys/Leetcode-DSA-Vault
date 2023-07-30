class Solution {
public:
    bool asteroidsDestroyed(int m, vector<int>& a) {
        sort(a.begin(),a.end());
        long long sum = m;
        for(int i = 0;i<a.size();i++)
        {
            if(a[i]>sum) return false;
            sum+=a[i];
        }
        return true; 
    }
};