class Solution(object):
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        B1 = [0] * (n + 2)
        B2 = [0] * (n + 2)

        def upd(B, i, v):
            while i <= n + 1:
                B[i] += v
                i += i & -i

        def qry(B, i):
            s = 0
            while i > 0:
                s += B[i]
                i -= i & -i
            return s

        def range_add(l, r, v):
            upd(B1, l, v)
            upd(B1, r + 1, -v)
            upd(B2, l, v * (l - 1))
            upd(B2, r + 1, -v * r)

        def prefix(i):
            return qry(B1, i) * i - qry(B2, i)

        last = {}
        S2 = 0
        ans = 0
        for j, x in enumerate(nums):
            p = last.get(x, -1)
            l, r = p + 2, j + 1
            s = prefix(r) - prefix(l - 1)
            S2 += 2 * s + (r - l + 1)
            range_add(l, r, 1)
            last[x] = j
            ans += S2
        return ans % MOD