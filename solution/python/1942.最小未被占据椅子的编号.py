"""1942. 最小未被占据椅子的编号"""

import heapq


class Solution:
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:
        events = sorted((arrive, leave, i) for i, (arrive, leave) in enumerate(times))
        free = []
        next_chair = 0
        occupied = []
        for arrive, leave, friend in events:
            while occupied and occupied[0][0] <= arrive:
                _, chair = heapq.heappop(occupied)
                heapq.heappush(free, chair)
            chair = heapq.heappop(free) if free else next_chair
            next_chair += chair == next_chair
            if friend == targetFriend:
                return chair
            heapq.heappush(occupied, (leave, chair))
        return -1


if __name__ == "__main__":
    test_cases = [(([[1, 4], [2, 3], [4, 6]], 1), 1)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().smallestChair(*args) == expected
