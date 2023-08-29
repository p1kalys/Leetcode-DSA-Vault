class Solution {
public:
    int bestClosingTime(string customers) {
        int n = customers.size();
        vector<int> pre_n(n + 1, 0), post_y(n + 1, 0);

        for (int i = 1; i < n + 1; i++) {
            pre_n[i] = pre_n[i - 1];
            if (customers[i - 1] == 'N') {
                pre_n[i]+=1;
            }
        }

        for (int i = n - 1; i >= 0; i--) {
            post_y[i] = post_y[i + 1];
            if (customers[i] == 'Y') {
                post_y[i] +=1;
            }
        }

        int index = 0;
        int mini = INT_MAX;

        for (int i = 0; i < n + 1; i++) {
            int penalty = pre_n[i] + post_y[i];
            if (penalty < mini) {
                mini = penalty;
                index = i;
            }
        }
        return index;
    }
};