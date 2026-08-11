#
# @lc app=leetcode.cn id=2254 lang=python3
# @lcpr version=30203
#
# [2254] 设计视频共享平台
#

import heapq
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class VideoSharingPlatform:
    def __init__(self):
        self.videos = {}
        self.available = []
        self.next_id = 0

    def upload(self, video: str) -> int:
        if self.available:
            video_id = heapq.heappop(self.available)
        else:
            video_id = self.next_id
            self.next_id += 1
        self.videos[video_id] = [video, 0, 0, 0]
        return video_id

    def remove(self, videoId: int) -> None:
        if videoId in self.videos:
            del self.videos[videoId]
            heapq.heappush(self.available, videoId)

    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        if videoId not in self.videos:
            return "-1"
        video = self.videos[videoId]
        video[1] += 1
        return video[0][startMinute : min(endMinute + 1, len(video[0]))]

    def like(self, videoId: int) -> None:
        if videoId in self.videos:
            self.videos[videoId][2] += 1

    def dislike(self, videoId: int) -> None:
        if videoId in self.videos:
            self.videos[videoId][3] += 1

    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        if videoId not in self.videos:
            return [-1]
        video = self.videos[videoId]
        return [video[2], video[3]]

    def getViews(self, videoId: int) -> int:
        return self.videos[videoId][1] if videoId in self.videos else -1


# @lc code=end


if __name__ == "__main__":
    platform = VideoSharingPlatform()
    assert platform.upload("123") == 0
    assert platform.upload("456") == 1
    platform.remove(4)
    platform.remove(0)
    assert platform.upload("789") == 0
    assert platform.watch(1, 0, 5) == "456"
    assert platform.watch(1, 0, 1) == "45"
    platform.like(1)
    platform.dislike(1)
    platform.dislike(1)
    assert platform.getLikesAndDislikes(1) == [1, 2]
    assert platform.getViews(1) == 2
    print('第 2254 题 "设计视频共享平台" 所有测试用例通过')
