"""2035. 将数组分成两个数组并最小化数组和的差"""


class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        n = len(nums) // 2
        left, right = nums[:n], nums[n:]
        sums_left = [[] for _ in range(n + 1)]
        sums_right = [[] for _ in range(n + 1)]
        for mask in range(1 << n):
            count = mask.bit_count()
            sums_left[count].append(sum(left[i] for i in range(n) if mask >> i & 1))
            sums_right[count].append(sum(right[i] for i in range(n) if mask >> i & 1))
        for values in sums_right:
            values.sort()
        total = sum(nums)
        answer = float("inf")
        for count in range(n + 1):
            for value in sums_left[count]:
                target = total / 2 - value
                values = sums_right[n - count]
                lo, hi = 0, len(values)
                while lo < hi:
                    mid = (lo + hi) // 2
                    if values[mid] < target:
                        lo = mid + 1
                    else:
                        hi = mid
                for index in (lo - 1, lo):
                    if 0 <= index < len(values):
                        answer = min(answer, abs(total - 2 * (value + values[index])))
        return answer


if __name__ == "__main__":
    test_cases = [(([3, 9, 7, 3],), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumDifference(*args) == expected
