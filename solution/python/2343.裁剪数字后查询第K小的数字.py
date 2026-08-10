"""2343. 裁剪数字后查询第 K 小的数字"""


class Solution:
    def smallestTrimmedNumbers(
        self, nums: list[str], queries: list[list[int]]
    ) -> list[int]:
        answer = []
        for k, trim in queries:
            order = sorted(range(len(nums)), key=lambda i: (nums[i][-trim:], i))
            answer.append(order[k - 1])
        return answer
