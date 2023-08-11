class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) {
            return 0; // No jumps needed for a single element array
        }
        
        int jumps = 0; // To count the number of jumps
        int currentEnd = 0; // The current farthest reachable index
        int nextEnd = 0; // The next farthest reachable index
        
        for (int i = 0; i < n - 1; ++i) { // Stop at n - 1 since the last element doesn't require a jump
            nextEnd = max(nextEnd, i + nums[i]); // Update the next farthest reachable index
            
            if (i == currentEnd) { // Need to jump to a new position
                currentEnd = nextEnd;
                jumps++;
                
                if (currentEnd >= n - 1) {
                    break; // If we can reach the last index, no need for further jumps
                }
            }
        }
        
        return jumps;
    }
};