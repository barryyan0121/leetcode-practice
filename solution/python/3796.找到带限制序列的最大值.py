from typing import List


class Solution:
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        limit = [10**18] * n
        limit[0] = 0
        for index, value in restrictions:
            limit[index] = value
        for i in range(n - 2, -1, -1):
            limit[i] = min(limit[i], limit[i + 1] + diff[i])
        current = 0
        answer = 0
        for i in range(1, n):
            current = min(current + diff[i - 1], limit[i])
            answer = max(answer, current)
        return answer


if __name__ == "__main__":
    s = Solution()
    assert s.findMaxVal(10, [[3, 1], [8, 1]], [2, 2, 3, 1, 4, 5, 1, 1, 2]) == 6
    assert s.findMaxVal(8, [[3, 2]], [3, 5, 2, 4, 2, 3, 1]) == 12
