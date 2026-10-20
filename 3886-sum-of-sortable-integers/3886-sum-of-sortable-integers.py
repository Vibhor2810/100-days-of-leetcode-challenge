
class Solution(object):
    def sortableIntegers(self, nums):
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True
            prev_max = float('-inf')

            for start in range(0, n, k):
                block = nums[start:start + k]

                # Blocks must be in sorted order globally
                if min(block) < prev_max:
                    valid = False
                    break

                # Check whether this block can be sorted by rotation
                descents = 0
                for i in range(k):
                    if block[i] > block[(i + 1) % k]:
                        descents += 1

                if descents > 1:
                    valid = False
                    break

                prev_max = max(block)

            if valid:
                ans += k

        return ans

