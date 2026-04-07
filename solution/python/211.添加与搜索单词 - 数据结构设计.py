#
# @lc app=leetcode.cn id=211 lang=python3
# @lcpr version=30203
#
# [211] 添加与搜索单词 - 数据结构设计
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class WordDictionary:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def addWord(self, word: str) -> None:
        node = self
        for ch in word:
            node = node.children.setdefault(ch, WordDictionary())
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node: "WordDictionary", idx: int) -> bool:
            if idx == len(word):
                return node.is_end
            ch = word[idx]
            if ch == ".":
                return any(dfs(child, idx + 1) for child in node.children.values())
            if ch not in node.children:
                return False
            return dfs(node.children[ch], idx + 1)

        return dfs(self, 0)


# @lc code=end


if __name__ == "__main__":
    wd = WordDictionary()

    def run_ops(ops: List[Tuple[str, str]]) -> List[bool]:
        obj = WordDictionary()
        results = []
        for op, arg in ops:
            if op == "add":
                obj.addWord(arg)
            else:
                results.append(obj.search(arg))
        return results

    # 测试用例 (func, args, result)
    test_cases = [
        (
            run_ops,
            [
                [
                    ("add", "bad"),
                    ("add", "dad"),
                    ("add", "mad"),
                    ("search", "pad"),
                    ("search", "bad"),
                    ("search", ".ad"),
                    ("search", "b.."),
                ]
            ],
            [False, True, True, True],
        ),
        (
            run_ops,
            [[("add", "a"), ("search", "."), ("search", "a"), ("search", "aa")]],
            [True, True, False],
        ),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)


#
# @lcpr case=start
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]\n
# @lcpr case=end

#
