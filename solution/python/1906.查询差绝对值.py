"""1906. 查询差绝对值"""


class Solution:
    def minDifference(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        prefix = [[0] * 101 for _ in range(len(nums) + 1)]
        for index, value in enumerate(nums, 1):
            prefix[index] = prefix[index - 1].copy()
            prefix[index][value] += 1
        answers = []
        for left, right in queries:
            previous = -1
            best = 101
            for value in range(1, 101):
                if prefix[right + 1][value] - prefix[left][value]:
                    if previous != -1:
                        best = min(best, value - previous)
                    previous = value
            answers.append(best)
        return answers


if __name__ == "__main__":
    assert Solution().minDifference([1, 3, 4, 8], [[0, 1], [1, 2], [2, 3], [0, 3]]) == [
        2,
        1,
        4,
        1,
    ]
