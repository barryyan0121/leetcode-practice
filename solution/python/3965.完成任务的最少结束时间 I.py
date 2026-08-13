#
# @lc app=leetcode.cn id=3965 lang=python3
#
# [3965] 完成任务的最少结束时间 I
#


class Solution:
    # @lc code=start
    def finishTime(self, n: int, edges: list[list[int]], baseTime: list[int]) -> int:
        children = [[] for _ in range(n)]
        for parent, child in edges:
            children[parent].append(child)

        def dfs(node: int) -> int:
            if not children[node]:
                return baseTime[node]
            child_finish_times = [dfs(child) for child in children[node]]
            earliest = min(child_finish_times)
            latest = max(child_finish_times)
            return latest + (latest - earliest) + baseTime[node]

        return dfs(0)

    # @lc code=end


if __name__ == "__main__":
    test_cases = [
        ((3, [[0, 1], [1, 2]], [9, 5, 3]), 17),
        ((3, [[0, 1], [0, 2]], [4, 7, 6]), 12),
        ((4, [[0, 1], [0, 2], [2, 3]], [5, 8, 2, 1]), 18),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().finishTime(*args) == expected
