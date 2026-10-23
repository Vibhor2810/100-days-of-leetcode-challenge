
class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # Already sorted
        if all(nums[i] == i for i in range(n)):
            return 0

        zero = nums.index(0)

        # Check ascending circular order
        ascending = all(
            nums[(zero + i) % n] == i
            for i in range(n)
        )

        if ascending:
            return min(zero, n - zero + 2)

        # Check descending circular order
        descending = all(
            nums[(zero + i) % n] == (n - i) % n
            for i in range(n)
        )

        if descending:
            k = (n - 1 - zero) % n
            return 1 + min(k, n - k)

        # Cannot be sorted using the allowed operations
        return -1
