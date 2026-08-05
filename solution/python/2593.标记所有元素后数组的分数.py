"""2593. 标记所有元素后数组的分数"""


class Solution:
    def findScore(self, nums: list[int]) -> int:
        marked = [False] * len(nums)
        answer = 0
        for value, index in sorted((value, index) for index, value in enumerate(nums)):
            if not marked[index]:
                answer += value
                marked[index] = True
                if index:
                    marked[index - 1] = True
                if index + 1 < len(nums):
                    marked[index + 1] = True
        return answer


if __name__ == "__main__":
    test_cases = [(([2, 1, 3, 4, 5, 2],), 7)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().findScore(*args) == expected
