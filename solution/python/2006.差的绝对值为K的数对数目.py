"""2006. 差的绝对值为 K 的数对数目"""


class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        counts = {}
        answer = 0
        for value in nums:
            answer += counts.get(value - k, 0) + counts.get(value + k, 0)
            counts[value] = counts.get(value, 0) + 1
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 2, 2, 1], 1), 4), (([1, 3], 3), 0)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countKDifference(*args) == expected
