class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        
        nums.sort() 
        max_count = 1
        count = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                count += 1
            elif nums[i] != nums[i - 1]: 
                count = 1
            max_count = max(max_count, count) 
        
        return max_count
