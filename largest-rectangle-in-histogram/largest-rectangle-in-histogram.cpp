class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<int> s1; //initialise a stack
        int res = 0, n = heights.size();
        
        for(int i=0; i<=n; i++){
            // check for prev and next smaller indices
            while(!s1.empty() and (i==n || heights[s1.top()] >= heights[i])){
                int len = heights[s1.top()];
                s1.pop();
                
                int bre;
                if(s1.empty()) bre = i;
                else bre = i - s1.top() - 1;
                res = max(res, len*bre);
            }
            
            s1.push(i);
        }
        
        return res;
    }
};