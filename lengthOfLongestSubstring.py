class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        max_count = 0
        i = 0
        while i < len(s) -1:
            val_list = []
            val_list = [s[i]]
            j=i+1
            while j < len(s):
                if s[j] in val_list:
                    break
                else:
                    val_list.append(s[j])
                    j+=1
            print(val_list)
            if len(val_list) > max_count:
                max_count = len(val_list)
            i+=1
        return max_count
