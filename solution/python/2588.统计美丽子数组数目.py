"""2588. 统计美丽子数组数目"""


class Solution:
    def beautifulSubarrays(self, nums: list[int]) -> int:
        counts = {0: 1}
        prefix = answer = 0
        for value in nums:
            prefix ^= value
            answer += counts.get(prefix, 0)
            counts[prefix] = counts.get(prefix, 0) + 1
        return answer


if __name__ == "__main__":
    test_cases = [(([4, 3, 1, 2, 4],), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().beautifulSubarrays(*args) == expected
