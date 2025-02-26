class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes, res = [], ""
        for i in strs:
            res += str(len(i))
            res +=","
        res+="#"
        for i in strs:
            res+=i
        print(res)
        return res
        

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i] != "#":
            digit = ""
            while s[i] != ",":
                digit +=s[i]
                i+=1
            sizes.append(int(digit))
            i+=1
        s = s[i+1:]
        j = 0
        for i in sizes:
            res.append(s[j:j+i])
            j = j+i
        return res
