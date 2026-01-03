class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_strs = sorted(strs,key=len)
        print(sorted_strs)
        key = sorted_strs[0]
        min_count = len(key)
        for i in sorted_strs[1:]:
            temp_count = 0
            for j, k in zip(i, key):
                if j == k:
                    temp_count+=1
                else:
                    break
            if temp_count < min_count:
                min_count = temp_count
        return key[:min_count]
