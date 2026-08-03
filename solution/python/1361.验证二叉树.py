# @lc app=leetcode.cn id=1361 lang=python3

from typing import List


class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        indegree = [0] * n
        for child in leftChild + rightChild:
            if child != -1:
                indegree[child] += 1
                if indegree[child] > 1:
                    return False
        roots = [node for node in range(n) if indegree[node] == 0]
        if len(roots) != 1:
            return False
        seen = set()
        stack = [roots[0]]
        while stack:
            node = stack.pop()
            if node in seen:
                return False
            seen.add(node)
            if leftChild[node] != -1:
                stack.append(leftChild[node])
            if rightChild[node] != -1:
                stack.append(rightChild[node])
        return len(seen) == n


if __name__ == "__main__":
    test_cases = [
        (
            Solution().validateBinaryTreeNodes,
            (4, [1, -1, 3, -1], [2, -1, -1, -1]),
            True,
        ),
        (
            Solution().validateBinaryTreeNodes,
            (4, [1, -1, 3, -1], [2, 3, -1, -1]),
            False,
        ),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1361 题 "验证二叉树" 所有测试用例通过')
