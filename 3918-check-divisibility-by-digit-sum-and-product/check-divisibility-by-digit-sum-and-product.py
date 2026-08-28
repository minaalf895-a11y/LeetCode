class Solution:
    def checkDivisibility(self, n: int) -> bool:
        string = str(n)
        sumOfstr = 0
        prod = 1
        total = 0
        for i in string:
            sumOfstr = sumOfstr + int(i)
            prod = prod * int(i)
        total = sumOfstr + prod
        if total != 0 and n % total == 0:
            return True
        else:
            return False
        

        