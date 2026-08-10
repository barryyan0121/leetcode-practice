from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]


if __name__ == "__main__":
    solution = Solution()
    assert solution.findCenter([[1, 2], [2, 3], [4, 2]]) == 2
    print("1791 passed")
