#
# @lc app=leetcode.cn id=208 lang=python3
# @lcpr version=30202
#
# [208] 实现 Trie (前缀树)
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
        # @lc code=end


if __name__ == "__main__":
    # 测试用例 (func, args, result)
    test_cases = [
        (
            [
                ("init", []),
                ("insert", ["apple"]),
                ("search", ["apple"]),
                ("search", ["app"]),
                ("startsWith", ["app"]),
                ("insert", ["app"]),
                ("search", ["app"]),
            ],
            [None, None, True, False, True, None, True],
        ),
        (
            [
                ("init", []),
                ("insert", ["a"]),
                ("search", ["a"]),
                ("startsWith", ["b"]),
            ],
            [None, None, True, False],
        ),
    ]

    all_passed = True
    for idx, (ops, expected) in enumerate(test_cases):
        try:
            result = []
            trie = None
            for op, args in ops:
                if op == "init":
                    trie = Trie()
                    result.append(None)
                elif op == "insert":
                    result.append(trie.insert(*args))
                elif op == "search":
                    result.append(trie.search(*args))
                else:
                    result.append(trie.startsWith(*args))
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {ops}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {ops}, 期望 = {expected}, 实际 = {result}"
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
# ["Trie","insert","search","startsWith"]\n[[],["apple"],["apple"],["app"]]\n
# @lcpr case=end

#
