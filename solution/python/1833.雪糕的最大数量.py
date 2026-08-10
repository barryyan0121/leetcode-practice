from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = 0
        for cost in sorted(costs):
            if cost > coins:
                break
            coins -= cost
            count += 1
        return count


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxIceCream([1, 3, 2, 4, 1], 7) == 4
    print("1833 passed")
