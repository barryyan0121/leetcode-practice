# @lc app=leetcode.cn id=1642 lang=python3


class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        import heapq

        climbs = []
        for index in range(len(heights) - 1):
            climb = heights[index + 1] - heights[index]
            if climb <= 0:
                continue
            heapq.heappush(climbs, climb)
            if len(climbs) > ladders:
                bricks -= heapq.heappop(climbs)
                if bricks < 0:
                    return index
        return len(heights) - 1


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.furthestBuilding, ([4, 2, 7, 6, 9, 14, 12], 5, 1), 4),
        (solution.furthestBuilding, ([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2), 7),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1642 题 "可以到达的最远建筑" 所有测试用例通过')
