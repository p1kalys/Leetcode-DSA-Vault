class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        st=[]
        mini=nums[0]
        for n in nums[1:]:
            while st and n>st[-1][0]:
                st.pop()
            if st and n<st[-1][0] and n>st[-1][1]:
                return True
            st.append([n,mini])
            mini = min(n,mini)
        return  False