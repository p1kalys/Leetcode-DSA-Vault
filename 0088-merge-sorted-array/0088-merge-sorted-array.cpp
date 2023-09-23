class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i=m-1;
        int j=n-1;
        int merge = m+n-1;
        while (i>=0 && j>=0) {
            if (nums1[i]>=nums2[j]){
                nums1[merge]=nums1[i];
                i--;
            }
            else {
                nums1[merge]=nums2[j];
                j--;
            }
            merge--;
        }
        while(j>=0) {
            nums1[merge]=nums2[j];
            j--;
            merge--;
        }
    
    }
};