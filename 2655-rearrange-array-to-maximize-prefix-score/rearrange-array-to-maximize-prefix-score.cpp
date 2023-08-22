class Solution {
public:
    int maxScore(vector<int>& a) {
        sort(a.begin(),a.end(),greater<int> ());
        long long int s=0,c=0;
        for(int i=0;i<a.size();i++)
        {
            s+=a[i];
            if(s>0) c++;
        }
       return c;
    }
};