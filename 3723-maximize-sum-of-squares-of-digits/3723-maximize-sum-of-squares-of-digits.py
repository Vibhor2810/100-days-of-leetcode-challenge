class Solution(object):
    def maxSumOfSquares(self, num, sum):
        if sum > 9 * num or sum < 1:
            return ""

        result = ""

        while sum > 0:
            digit = min(9, sum)
            result += str(digit)
            sum -= digit

        result += "0" * (num - len(result))

        return result