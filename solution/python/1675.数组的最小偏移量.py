# @lc app=leetcode.cn id=1675 lang=python3


class Solution:
    def minimumDeviation(self, nums: list[int]) -> int:
        import heapq

        values = [-value * 2 if value % 2 else -value for value in nums]
        heapq.heapify(values)
        minimum = -max(values)
        answer = -values[0] - minimum
        while values[0] % 2 == 0:
            maximum = -heapq.heappop(values)
            maximum //= 2
            minimum = min(minimum, maximum)
            heapq.heappush(values, -maximum)
            answer = min(answer, -values[0] - minimum)
        return answer


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minimumDeviation, ([1, 2, 3, 4],), 1),
        (solution.minimumDeviation, ([4, 1, 5, 20, 3],), 3),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1675 题 "数组的最小偏移量" 所有测试用例通过')
