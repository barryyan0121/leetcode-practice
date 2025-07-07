#
# @lc app=leetcode.cn id=1353 lang=python3
# @lcpr version=30201
#
# [1353] 最多可以参加的会议数目
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *
import heapq

# @lc code=start
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        # 拿到最大的结束时间
        max_day = max(event[1] for event in events)
        # 按照开始时间排序
        events.sort()
        pq = []
        ans, j = 0, 0
        # 遍历每一天
        # j 用来记录 events 中的下一个事件
        # pq 用来存储当前可以参加的事件的结束时间
        # 如果 pq 中的事件结束时间小于当前天数 i，则说明这个事件已经结束，不能参加
        # 如果 pq 中有事件，则参加结束时间最早的事件，并将其从 pq 中移除
        # 每参加一个事件，ans 加 1
        for i in range(1, max_day + 1):
            while j < n and events[j][0] <= i:
                heapq.heappush(pq, events[j][1])
                j += 1
            while pq and pq[0] < i:
                heapq.heappop(pq)
            if pq:
                heapq.heappop(pq)
                ans += 1

        return ans

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [[1,2],[2,3],[3,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[2,3],[3,4],[1,2]]\n
# @lcpr case=end

#

