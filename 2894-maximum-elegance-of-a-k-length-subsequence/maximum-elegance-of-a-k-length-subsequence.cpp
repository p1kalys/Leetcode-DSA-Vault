#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:

    static bool cmp(vector<int>& a, vector<int>& b){
        return a[0] > b[0];
    }

    long long findMaximumElegance(vector<vector<int>>& items, int k) {
        int n = items.size();
        sort(items.begin(), items.end(), cmp);

        unordered_map<int,int> freq; //frequency of category
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;

        long long totProfit = 0;
        for(int i=0; i<k; i++){
            totProfit += items[i][0];
            freq[items[i][1]]++;
            pq.push({items[i][0], i});
        }

        long long res = totProfit + freq.size() * freq.size();

        for(int i=k; i<n && !pq.empty(); i++){
            if(freq.count(items[i][1]))
                continue; //because we now want to add new categories
            int idx = pq.top().second;
            pq.pop();
            if(freq[items[idx][1]] == 1){
                i--; //we have skipped this element since it has a unique category.
                continue;
            }
            //now we know that pq.top() element has duplicate category, 
            //let's replace it with new item of new category
            totProfit += items[i][0] - items[idx][0];
            freq[items[idx][1]]--;
            freq[items[i][1]]++;
            long long unique = freq.size() * freq.size();
            res = max(res, totProfit + unique);
        }
        return res;
    }
};