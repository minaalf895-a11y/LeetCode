class Solution(object):
    def reverse(self, x):
        rev = str(abs(x))[::-1]
        
        forw = -int(rev) if x < 0 else int(rev)

        if -2147483648 <= forw <= 2147483647:
            return forw
        else: 
            return 0
        