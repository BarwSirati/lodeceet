class Solution:
    def romanToInt(self, s: str) -> int:
        num = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        su = 0
        i = 0
        while i < len(s):
            if i != len(s)-1 and num[s[i]] < num[s[i+1]]:
                su += int(num[s[i+1]]-num[s[i]])
                i+=2
                continue
            else:
                su += int(num[s[i]])
            i+=1

        return su
        