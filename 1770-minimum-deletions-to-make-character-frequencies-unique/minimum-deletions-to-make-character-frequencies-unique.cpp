class Solution {
public:
    int minDeletions(string s) {
        vector<int> freq(26,0);
        for(auto i: s){
            freq[i -'a']++;
        }

        priority_queue<int> pq;
        for (int i=0; i<26; i++){
            if (freq[i]>0){
                pq.push(freq[i]);
            }
        }
        int deleteCount = 0;
        while (pq.size() > 1) {
            int ele = pq.top();
            pq.pop();

            if (ele == pq.top()){
                if (ele - 1 > 0){
                    pq.push(ele-1);
                }
                deleteCount++;
            }
        }
        return deleteCount;
    }
};