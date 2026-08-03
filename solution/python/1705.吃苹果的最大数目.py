# @lc app=leetcode.cn id=1705 lang=python3


class Solution:
    def eatenApples(self, apples: list[int], days: list[int]) -> int:
        import heapq

        heap = []
        eaten = day = 0
        while day < len(apples) or heap:
            if day < len(apples) and apples[day]:
                heapq.heappush(heap, (day + days[day], apples[day]))
            while heap and heap[0][0] <= day:
                heapq.heappop(heap)
            if heap:
                expiry, count = heapq.heappop(heap)
                eaten += 1
                if count > 1:
                    heapq.heappush(heap, (expiry, count - 1))
            day += 1
        return eaten


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.eatenApples, ([1, 2, 3, 5, 2], [3, 2, 1, 4, 2]), 7),
        (solution.eatenApples, ([3, 0, 0, 0, 0, 2], [3, 0, 0, 0, 0, 2]), 5),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1705 题 "吃苹果的最大数目" 所有测试用例通过')
