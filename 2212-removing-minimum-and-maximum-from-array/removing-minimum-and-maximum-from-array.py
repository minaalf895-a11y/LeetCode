class Solution(object):
    def minimumDeletions(self, nums):
        n = len(nums)
        if n <=2:
            return n 
        min_ind = nums.index(min(nums))
        max_ind = nums.index(max(nums))

        p1 = min(max_ind,min_ind)
        p2 = max(max_ind,min_ind)

        mid = n//2
        if p2 < mid:
            return p2+1
        elif p1>mid:
            return n-p1
        else:
            first_half = p2+1
            second_half = n - p1
            both = (p1+1)+(n-p2)
        return min(first_half,second_half,both)
       