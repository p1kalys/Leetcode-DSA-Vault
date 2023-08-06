class Solution {
public:
    long long continuousSubarrays(vector<int>& a) {
        int n = (int)a.size();
        long long ans = 0;
        int l = 0;
        multiset<int>s;
        for(int i = 0 ; i < n ; i++) {
            s.insert(a[i]);
            while(abs(*s.rbegin() - *s.begin()) > 2) {
                s.erase(s.find(a[l]));
                l++;
            }
            ans += (i-l+1);
        }
        return ans;
    }
};