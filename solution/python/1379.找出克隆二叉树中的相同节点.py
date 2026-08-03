# @lc app=leetcode.cn id=1379 lang=python3
from typing import Optional
from common.node import TreeNode


class Solution:
    def getTargetCopy(
        self, original: Optional[TreeNode], cloned: Optional[TreeNode], target: TreeNode
    ) -> Optional[TreeNode]:
        if not original:
            return None
        if original is target:
            return cloned
        return self.getTargetCopy(
            original.left, cloned.left, target
        ) or self.getTargetCopy(original.right, cloned.right, target)


if __name__ == "__main__":
    test_cases = ["clone"]
    for _, _case in enumerate(test_cases):
        pass
    original = TreeNode.create_root([7, 4, 3, None, None, 6, 19])
    cloned = TreeNode.create_root([7, 4, 3, None, None, 6, 19])
    assert Solution().getTargetCopy(original, cloned, original.right.left).val == 6
    print('第 1379 题 "找出克隆二叉树中的相同节点" 所有测试用例通过')
