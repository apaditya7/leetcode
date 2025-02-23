class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result_dict = {}
        for i in nums:
            if i in result_dict.keys():
                result_dict[i] += 1
            else:
                result_dict[i] = 1
        arr = []
        for num,cnt in result_dict.items():
            arr.append([cnt,num])
        arr.sort()
        arr = arr[::-1]
        result = []
        i = 0
        while i < k:
            result.append(arr[i][1])
            i+=1
        return result
        
