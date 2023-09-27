class Solution {
public:
    bool Can_split(vector<int>&nums,int k,int mid){
        int sum=0,c=1;
        for(int i=0;i<nums.size();i++){
            sum+=nums[i];
            if(sum>mid){
                c++;
                sum=nums[i];
            }
        }
        if(c<=k) return true;
        return false;
    }

    int splitArray(vector<int>& nums, int k) {
        int l=INT_MIN,h=0,ans=0;
        for(auto i:nums){
            l=max(l,i);
            h+=i;
        }
        while(l<=h){
            int mid=l+(h-l)/2;
            int temp=Can_split(nums,k,mid);
            if(temp==true){
                ans=mid;
                h=mid-1;
            }else{
                l=mid+1;
            }
        }
        return ans;
    }
};