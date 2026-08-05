"""2023. 连接后等于目标字符串的字符串对"""

from collections import Counter


class Solution:
    def numOfPairs(self, nums: list[str], target: str) -> int:
        counts = Counter(nums)
        answer = 0
        for value, count in counts.items():
            if target.startswith(value) and target[len(value) :] in counts:
                answer += count * counts[target[len(value) :]]
                if value == target[len(value) :]:
                    answer -= count
        return answer


if __name__ == "__main__":
    test_cases = [((["777", "7", "77", "77"], "7777"), 4)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().numOfPairs(*args) == expected
