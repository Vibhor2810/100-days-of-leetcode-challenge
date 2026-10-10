class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        k = k1 + k2
        n = len(nums1)
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]

        if sum(diffs) <= k:
            return 0

        max_d = max(diffs)
        cnt = [0] * (max_d + 2)
        for d in diffs:
            cnt[d] += 1
        for d in range(max_d, 0, -1):
            if cnt[d] == 0:
                continue
            if k >= cnt[d]:
                k -= cnt[d]
                cnt[d - 1] += cnt[d]
                cnt[d] = 0
            else:
                cnt[d] -= k
                cnt[d - 1] += k
                k = 0
                break

        return sum(d * d * c for d, c in enumerate(cnt))