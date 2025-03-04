class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        i = 0
        s1_sorted = ''.join(sorted(s1))
        while i < len(s2) - length +1:
            target_str = s2[i:i+length]
            target_str = ''.join(sorted(target_str))
            if s1_sorted == target_str:
                return True
            
            i+=1
        return False
