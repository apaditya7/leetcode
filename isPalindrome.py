class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        clean_text = ''.join(char for char in s if char.isalnum())
        if clean_text == clean_text[::-1]:
            return True
        else:
            return False
