class Solution:
    def romanToInt(self,s: str) -> int:
        def charToInt(c: str) -> int:
            if c == 'I': return 1
            if c == 'V': return 5
            if c == 'X': return 10
            if c == 'L': return 50
            if c == 'C': return 100
            if c == 'D': return 500
            if c == 'M': return 1000
        total = 0
        i = 0 
        length = len(s)

        while i <length:
            if i+1<length and charToInt(s[i])<charToInt(s[i+1]):
                total+=charToInt(s[i+1])-charToInt(s[i])
                i+=2
            else:
                total += charToInt(s[i])
                i+=1
        return total

    
        