from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            mat = [list(row) for row in zip(*mat[::-1])]
        return False


if __name__ == "__main__":
    solution = Solution()
    assert solution.findRotation([[0, 1], [1, 0]], [[1, 0], [0, 1]]) is True
    print("1886 passed")
