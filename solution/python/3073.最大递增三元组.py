from bisect import bisect_left


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        right = [0] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            right[i] = max(right[i + 1], nums[i + 1])
        vals = sorted(set(nums))
        bit = [0] * (len(vals) + 1)

        def update(i, value):
            while i < len(bit):
                bit[i] = max(bit[i], value)
                i += i & -i

        def query(i):
            result = 0
            while i:
                result = max(result, bit[i])
                i -= i & -i
            return result

        update(bisect_left(vals, nums[0]) + 1, nums[0])
        ans = 0
        for j in range(1, len(nums) - 1):
            rank = bisect_left(vals, nums[j]) + 1
            left = query(rank - 1)
            if left and nums[j] < right[j]:
                ans = max(ans, left - nums[j] + right[j])
            update(rank, nums[j])
        return ans
