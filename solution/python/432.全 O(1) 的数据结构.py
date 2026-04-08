#
# @lc app=leetcode.cn id=432 lang=python3
# @lcpr version=30203
#
# [432] 全 O(1) 的数据结构
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


class Node:
    def __init__(self, count: int):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


# @lc code=start
class AllOne:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key2node = {}

    def _add_after(self, node: Node, new_node: Node) -> None:
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node

    def _remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key in self.key2node:
            node = self.key2node[key]
            nxt = node.next
            if nxt == self.tail or nxt.count != node.count + 1:
                nxt = Node(node.count + 1)
                self._add_after(node, nxt)
            nxt.keys.add(key)
            self.key2node[key] = nxt
            node.keys.remove(key)
            if not node.keys:
                self._remove(node)
        else:
            first = self.head.next
            if first == self.tail or first.count != 1:
                first = Node(1)
                self._add_after(self.head, first)
            first.keys.add(key)
            self.key2node[key] = first

    def dec(self, key: str) -> None:
        node = self.key2node[key]
        if node.count == 1:
            del self.key2node[key]
        else:
            prev = node.prev
            if prev == self.head or prev.count != node.count - 1:
                prev = Node(node.count - 1)
                self._add_after(node.prev, prev)
            prev.keys.add(key)
            self.key2node[key] = prev
        node.keys.remove(key)
        if not node.keys:
            self._remove(node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))


# @lc code=end


if __name__ == "__main__":

    def assert_valid_result(
        result: List[Optional[str]], expected: List[Optional[Union[str, set[str]]]]
    ) -> None:
        assert len(result) == len(expected)
        for idx, (got, want) in enumerate(zip(result, expected)):
            if isinstance(want, set):
                assert got in want, (idx, got, want)
            else:
                assert got == want, (idx, got, want)

    def run_ops(ops: List[Tuple[str, Optional[str]]]) -> List[Optional[str]]:
        obj = AllOne()
        res = []
        for op, val in ops:
            if op == "inc":
                obj.inc(val)
                res.append(None)
            elif op == "dec":
                obj.dec(val)
                res.append(None)
            elif op == "max":
                res.append(obj.getMaxKey())
            else:
                res.append(obj.getMinKey())
        return res

    # 测试用例 (func, args, result)
    test_cases = [
        (
            run_ops,
            [
                [
                    ("inc", "hello"),
                    ("inc", "hello"),
                    ("inc", "leet"),
                    ("max", None),
                    ("min", None),
                    ("dec", "hello"),
                    ("max", None),
                    ("min", None),
                ]
            ],
            [None, None, None, "hello", "leet", None, {"hello", "leet"}, {"hello", "leet"}],
        ),
        (
            run_ops,
            [[("inc", "a"), ("inc", "b"), ("inc", "b"), ("min", None), ("max", None)]],
            [None, None, None, "a", "b"],
        ),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert_valid_result(result, expected)
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
# ["AllOne","inc","inc","inc","inc","inc","dec","dec","getMaxKey","getMinKey"]\n
# [[],["hello"],["hello"],["leet"],["leet"],["leet"],["hello"],["hello"],[],[]]\n
# @lcpr case=end

#
