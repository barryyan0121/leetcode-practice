#
# @lc app=leetcode.cn id=1032 lang=python3
#
# [1032] 字符流
#

import os
import sys
from collections import deque
from typing import List


# @lc code=start
class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = {}
        self.stream = deque(maxlen=max(map(len, words)))
        for word in words:
            node = self.trie
            for letter in reversed(word):
                node = node.setdefault(letter, {})
            node["$"] = {}

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        node = self.trie
        for current in reversed(self.stream):
            if current not in node:
                return False
            node = node[current]
            if "$" in node:
                return True
        return False


# @lc code=end


def run_stream(words, letters):
    checker = StreamChecker(words)
    return [checker.query(letter) for letter in letters]


if __name__ == "__main__":
    test_cases = [
        (
            run_stream,
            (["cd", "f", "kl"], "abcdefghijkl"),
            [
                False,
                False,
                False,
                True,
                False,
                True,
                False,
                False,
                False,
                False,
                False,
                True,
            ],
        ),
        (run_stream, (["a"], "ba"), [False, True]),
        (run_stream, (["ab", "ba"], "aba"), [False, True, True]),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
