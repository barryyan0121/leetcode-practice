from typing import List


class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack = []
        for value in nums:
            stack.append(value)
            while len(stack) >= 2 and stack[-1] == stack[-2]:
                value = stack.pop() * 2
                stack[-1] = value
        return stack


if __name__ == "__main__":
    assert Solution().mergeAdjacent([3, 1, 1, 2, 2, 2]) == [3, 8]
