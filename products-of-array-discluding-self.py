class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        ind = 0
        while ind < len(nums):
            left = 0
            left_prod = 1
            while left < ind:
                left_prod *= nums[left]
                left+=1
            right = len(nums) -1
            right_prod = 1
            while right > ind:
                right_prod *= nums[right]
                right -=1
            ind +=1
            res.append(left_prod*right_prod)
        return res
