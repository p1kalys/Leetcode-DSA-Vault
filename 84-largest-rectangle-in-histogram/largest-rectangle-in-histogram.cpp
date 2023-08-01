class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<int> s1; //initialise a stack
        int res = 0, n = heights.size();
        int left[n],right[n];
        for(int i=0; i<n; i++){
            while(!s1.empty() and (heights[s1.top()] >= heights[i])){
                s1.pop();
            }
            if(s1.empty())left[i]=0;
            else left[i]=s1.top()+1;
            s1.push(i);
        }
        while (!s1.empty()) s1.pop();
        for(int i=n-1; i>=0; i--){
            while(!s1.empty() and (heights[s1.top()] >= heights[i])){
                s1.pop();
            }
            if(s1.empty())right[i]=n-1;
            else right[i]=s1.top()-1;
            s1.push(i);
        }
        for(int i=0; i<n;i++){
            res=max(res,heights[i]*(right[i]-left[i]+1));
        }
        return res;
    }
};