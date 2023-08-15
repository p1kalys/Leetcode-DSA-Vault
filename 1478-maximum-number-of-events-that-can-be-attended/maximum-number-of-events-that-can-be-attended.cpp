class Solution {
public:
    static bool cmp(vector<int> &a, vector<int> &b){
        if (a[0] == b[0])
            return a[1] < b[1];

        return a[0] < b[0];
    }

    int maxEvents(vector<vector<int>>& v) {
        sort(v.begin(), v.end(), cmp);
        int len = v.size();
        int j = 0;
        int ans = 0, loop = INT_MIN;
        priority_queue<int, vector<int>, greater<int>> pq;
        pq.push(INT_MAX);

        for(int i = 0; i < len; i++){
            loop = max(loop, v[i][1]);
        }

        for (int day = 0; day <= loop; day++) {
            while(pq.top() < day){
                pq.pop();
            }

            while(j < len && v[j][0] == day){
                pq.push(v[j][1]);
                j++;
            }

            if (pq.top() != INT_MAX && pq.top() >= day){
                ans = ans + 1;
                pq.pop();
            }
        }

        return ans;
    }
};