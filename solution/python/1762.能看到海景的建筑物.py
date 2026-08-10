from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        result = []
        tallest = -1
        for index in range(len(heights) - 1, -1, -1):
            if heights[index] > tallest:
                result.append(index)
                tallest = heights[index]
        return result[::-1]


if __name__ == "__main__":
    solution = Solution()
    assert solution.findBuildings([4, 2, 3, 1]) == [0, 2, 3]
    assert solution.findBuildings([4, 3, 2, 1]) == [0, 1, 2, 3]
    print("1762 passed")
