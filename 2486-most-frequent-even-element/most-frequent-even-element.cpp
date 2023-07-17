class Solution {
public:
    int mostFrequentEven(vector<int>& nums) {
	    int ans = -1;
		
		//vector to find the maximum frequency of the elements
        vector<int> findMax;
		
		//vector to store the frequency of even numbers only
        vector<int> even;
		
		//hashing
        unordered_map<int,int> mp;
        for(int i=0;i<nums.size();++i){
            if(nums[i]%2==0){
            mp[nums[i]]++;
            }
        }
		
		//finding maximum frequency
        int max=0;
        for(auto i: mp){
           findMax.push_back(i.second); 
        }
		
		//if there is no even number in the array then its frequency will also be null hence return -1
        if(findMax.size()==0) return ans;
		
        sort(findMax.begin(),findMax.end());
        max=findMax[findMax.size()-1];
		
		
		//as we need to return the even number with max frequency , hence store only those numbers 
		// whose frequency is equal to max
        for(auto i:mp){
            if(i.second==max){
                even.push_back(i.first);
            }
        }
		
		//sorting the even numbers because if the frequency of any number of elements is same 
		// then we need to return the smallest among those 
        sort(even.begin(),even.end());
       
        if(even.size()>=1) return even[0];
        else  return ans;
    }
};