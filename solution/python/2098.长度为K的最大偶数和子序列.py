"""2098. 长度为 K 的最大偶数和子序列"""


class Solution:
    def largestEvenSum(self, nums: list[int], k: int) -> int:
        nums.sort(reverse=True)
        chosen = nums[:k]
        if sum(chosen) % 2 == 0:
            return sum(chosen)
        odd_low = min((x for x in chosen if x % 2), default=None)
        even_low = min((x for x in chosen if x % 2 == 0), default=None)
        odd_high = max((x for x in nums[k:] if x % 2), default=None)
        even_high = max((x for x in nums[k:] if x % 2 == 0), default=None)
        candidates = []
        if odd_low is not None and even_high is not None:
            candidates.append(sum(chosen) - odd_low + even_high)
        if even_low is not None and odd_high is not None:
            candidates.append(sum(chosen) - even_low + odd_high)
        return max(candidates, default=-1)


if __name__ == "__main__":
    test_cases = [(([4, 1, 5, 3, 1], 3), 12)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().largestEvenSum(*args) == expected
