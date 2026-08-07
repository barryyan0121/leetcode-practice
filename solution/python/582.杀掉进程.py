#
# @lc app=leetcode.cn id=582 lang=python3
#
# [582] 杀掉进程
#

from typing import List


# @lc code=start
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        children = {}
        for child, parent in zip(pid, ppid):
            children.setdefault(parent, []).append(child)
        result, stack = [], [kill]
        while stack:
            process = stack.pop()
            result.append(process)
            stack.extend(children.get(process, []))
        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert sorted(solution.killProcess([1, 3, 10, 5], [3, 0, 5, 3], 5)) == [5, 10]
    assert solution.killProcess([1], [0], 1) == [1]
    print('第 582 题 "杀掉进程" 所有测试用例通过')
