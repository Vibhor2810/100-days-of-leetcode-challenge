class Solution(object):
    def maxAlternatingSum(self, nums):
        sq = sorted((x * x for x in nums), reverse=True)
        k = (len(sq) + 1) // 2 
        return sum(sq[:k]) - sum(sq[k:])        