class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        ind1 = 0
        while ind1 < len(nums) - 2:
            ind2 = ind1 + 1
            while ind2 < len(nums) -1:
                ind3 = ind2 + 1
                while ind3 < len(nums):
                    if nums[ind1]+nums[ind2]+nums[ind3] == 0:
                        sorted_list = [nums[ind1],nums[ind2],nums[ind3]]
                        sorted_list.sort()
                        if sorted_list in res:
                            ind3+=1
                            continue
                        else:
                            res.append(sorted_list)
                    ind3+=1
                ind2+=1
            ind1+=1
        return res
