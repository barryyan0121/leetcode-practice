"""2537. 统计好子数组的数目"""


class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        counts = {}
        pairs = left = answer = 0
        for right, value in enumerate(nums):
            pairs += counts.get(value, 0)
            counts[value] = counts.get(value, 0) + 1
            while pairs >= k:
                answer += len(nums) - right
                counts[nums[left]] -= 1
                pairs -= counts[nums[left]]
                left += 1
        return answer


if __name__ == "__main__":
    test_cases = [(([3, 1, 4, 3, 2, 2, 4], 2), 4)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countGood(*args) == expected
