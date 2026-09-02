class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # sort 
        nums.sort()

        for i, num in enumerate(nums):
            if num == nums[i-1] and len(nums)!=1:
                return True

        return False


        