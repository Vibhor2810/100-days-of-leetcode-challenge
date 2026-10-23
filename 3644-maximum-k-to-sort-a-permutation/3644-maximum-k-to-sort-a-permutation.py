class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = None

        for i in range(len(nums)):
            if nums[i] != i:
                if ans is None:
                    ans = nums[i]
                else:
                    ans &= nums[i]

        return ans if ans is not None else 0