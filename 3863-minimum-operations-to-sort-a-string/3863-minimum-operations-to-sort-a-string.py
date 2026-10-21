class Solution(object):
    def minOperations(self, s):
        n = len(s)

        # Step 1: Check if already sorted
        sorted_string = True
        for i in range(1, n):
            if s[i] < s[i - 1]:
                sorted_string = False
                break

        if sorted_string:
            return 0

        # Step 2: An unsorted string of length 2 cannot be sorted
        if n == 2:
            return -1

        # Step 3: Find minimum and maximum characters
        mn = min(s)
        mx = max(s)

        # Step 4: Can be sorted in one operation
        if s[0] == mn or s[-1] == mx:
            return 1

        # Step 5: Check whether min or max appears in the middle
        for i in range(1, n - 1):
            if s[i] == mn or s[i] == mx:
                return 2

        # Step 6: Remaining cases need three operations
        return 3