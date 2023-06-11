class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        
        int n = arr.size();
        
        // left_max[i] will store the maximum till ith from left side
        
        vector<int> left_max(n, 0);
        
        // fill left_max
        
        left_max[0] = arr[0];
        
        for(int i = 1; i < n; i++)
        {
            left_max[i] = max(left_max[i - 1], arr[i]);
        }
        
        // right_min[i] will store the minimum till ith from right side
        
        vector<int> right_min(n, 0);
        
        // fill right_min array
        
        right_min[n - 1] = arr[n - 1];
        
        for(int i = n - 2; i >= 0; i--)
        {
            right_min[i] = min(right_min[i + 1], arr[i]);
        }
        
        // if at any index i we are having maximum till ith from left side is smaller than minimum till (i + 1)th from right side, then we found chunk
        
        int count = 0;
        
        for(int i = 0; i < n - 1; i++)
        {
            if(left_max[i] <= right_min[i + 1])
            {
                count++;
            }
        }
        
        // there will be always a partition at (n - 1)th index
        
        count++;
        
        return count;
    }
};