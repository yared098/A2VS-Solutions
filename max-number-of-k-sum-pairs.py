class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(nums[i]==-1 or nums[j]==-1):
                    continue
                if(i==j and j==i):
                    continue
                if(nums[i]+nums[j]==k):
                    nums[i]=-1
                    nums[j]=-1
        m=nums.count(-1)
        return int(m/2)
        