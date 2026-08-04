from collections import Counter


class Solution:
    def getLargestOutlier(self, nums: list[int]) -> int:
        counts = Counter(nums)
        total = sum(nums)
        answer = -(10**18)
        for value in nums:
            remainder = total - value
            if remainder % 2:
                continue
            special_sum = remainder // 2
            available = counts[special_sum] - (value == special_sum)
            if available > 0:
                answer = max(answer, value)
        return answer


if __name__ == "__main__":
    test_cases = [
        (([2, 3, 5, 10],), 10),
        (([-2, -1, -3, -6, 4],), 4),
        (([1, 1, 1, 1, 1, 5, 5],), 5),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().getLargestOutlier(nums) == expected
