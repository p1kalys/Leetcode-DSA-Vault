class Solution {
public:
    vector<int> findArray(vector<int>& pref) {
        int n=pref.size();
        int prefix = 0;
        for (int i=1; i<n; i++) {
            prefix ^= pref[i-1];
            pref[i] = prefix ^ pref[i];
        }
        return pref;
    }
};