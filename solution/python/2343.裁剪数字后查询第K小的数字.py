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

if __name__ == "__main__":
    assert Solution().smallestTrimmedNumbers(["102","473","251","814"], [[1,1],[2,3],[4,2],[1,2]]) == [2,2,1,0]
