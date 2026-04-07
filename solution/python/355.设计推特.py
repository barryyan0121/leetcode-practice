#
# @lc app=leetcode.cn id=355 lang=python3
# @lcpr version=30203
#
# [355] 设计推特
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *
from heapq import heappush, heappop


# @lc code=start
class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets.setdefault(userId, []).append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following.get(userId, set()).copy()
        users.add(userId)
        heap = []
        for uid in users:
            for time, tweetId in self.tweets.get(uid, [])[-10:]:
                heappush(heap, (-time, tweetId))
        result = []
        while heap and len(result) < 10:
            _, tweetId = heappop(heap)
            result.append(tweetId)
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)


# @lc code=end


if __name__ == "__main__":
    # 测试用例 (func, args, result)
    def run_operations(ops: List[str], values: List[List[int]]) -> List[Optional[List[int]]]:
        twitter = None
        result = []
        for op, value in zip(ops, values):
            if op == "Twitter":
                twitter = Twitter()
                result.append(None)
            elif op == "postTweet":
                twitter.postTweet(value[0], value[1])
                result.append(None)
            elif op == "getNewsFeed":
                result.append(twitter.getNewsFeed(value[0]))
            elif op == "follow":
                twitter.follow(value[0], value[1])
                result.append(None)
            elif op == "unfollow":
                twitter.unfollow(value[0], value[1])
                result.append(None)
        return result

    test_cases = [
        (
            run_operations,
            (
                ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed"],
                [[], [1, 5], [1], [1, 2], [2, 6], [1]],
            ),
            [None, None, [5], None, None, [6, 5]],
        ),
        (
            run_operations,
            (
                ["Twitter", "postTweet", "postTweet", "follow", "getNewsFeed", "unfollow", "getNewsFeed"],
                [[], [1, 5], [1, 3], [1, 2], [1], [1, 2], [1]],
            ),
            [None, None, None, None, [3, 5], None, [3, 5]],
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
# ["Twitter","postTweet","getNewsFeed"]\n[[],[1,5],[1]]\n
# @lcpr case=end
