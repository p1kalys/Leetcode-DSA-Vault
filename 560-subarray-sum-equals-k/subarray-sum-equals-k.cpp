class Solution {
public:
    int subarraySum(vector<int>& arr, int K) {
        int n = arr.size();
        unordered_map<int, int> mpp;
        int count = 0, sum = 0;
        for (int i = 0; i < n; i++) {
            sum += arr[i];
            if (sum == K) {
                count++;
            }
            if (mpp.find(sum - K) != mpp.end()) {
                count += mpp[sum - K];
            }
            mpp[sum]++;
        }
        return count;
    }
};