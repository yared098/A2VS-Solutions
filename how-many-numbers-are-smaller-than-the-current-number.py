class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ls=[]
        for i in range(len(nums)):
            n=0
            for j in range(len(nums)):
                if(nums[i]>nums[j]):
                    n=n+1
            ls.append(n)
        return ls