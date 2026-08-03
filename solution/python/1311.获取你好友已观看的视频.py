# @lc app=leetcode.cn id=1311 lang=python3

from collections import Counter, deque
from typing import List


class Solution:
    def watchedVideosByFriends(
        self,
        watchedVideos: List[List[str]],
        friends: List[List[int]],
        id: int,
        level: int,
    ) -> List[str]:
        queue, distance = deque([id]), {id: 0}
        while queue:
            person = queue.popleft()
            if distance[person] == level:
                break
            for friend in friends[person]:
                if friend not in distance:
                    distance[friend] = distance[person] + 1
                    queue.append(friend)
        counts = Counter(
            video
            for person, dist in distance.items()
            if dist == level
            for video in watchedVideos[person]
        )
        return sorted(counts, key=lambda video: (counts[video], video))


if __name__ == "__main__":
    test_cases = [
        (
            Solution().watchedVideosByFriends,
            (
                [["A", "B"], ["C"], ["B", "C"], ["D"]],
                [[1, 2], [0, 3], [0, 3], [1, 2]],
                0,
                1,
            ),
            ["B", "C"],
        ),
        (
            Solution().watchedVideosByFriends,
            (
                [["A", "B"], ["C"], ["B", "C"], ["D"]],
                [[1, 2], [0, 3], [0, 3], [1, 2]],
                0,
                2,
            ),
            ["D"],
        ),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1311 题 "获取你好友已观看的视频" 所有测试用例通过')
