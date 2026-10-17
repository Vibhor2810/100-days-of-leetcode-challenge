class Solution(object):
    def minSwaps(self, nums):
        def ds(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        n = len(nums)
        order = sorted(range(n), key=lambda i: (ds(nums[i]), nums[i]))
        # order[k] = index in original array of the element that belongs at position k

        visited = [False] * n
        cycles = 0
        for i in range(n):
            if not visited[i]:
                cycles += 1
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = order[j]
        return n - cycles