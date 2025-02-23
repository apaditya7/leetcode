class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}
        for i in strs:
            temp_i = ''.join(sorted(i))
            if temp_i in result_dict.keys():
                result_dict[temp_i].append(i)
            else:
                result_dict[temp_i] = [i]
        result_list = []
        for i in result_dict.values():
            result_list.append(i)
        return result_list
