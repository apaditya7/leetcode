class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_index = 0
        right_index = 1
        while left_index < len(numbers)-1:
            right_index = left_index+1
            while right_index < len(numbers):
                if numbers[right_index] + numbers[left_index] == target:
                    return [left_index+1,right_index+1]
                right_index+=1
            left_index+=1
