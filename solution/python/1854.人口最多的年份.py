from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        changes = [0] * 101
        for birth, death in logs:
            changes[birth - 1950] += 1
            changes[death - 1950] -= 1
        current = answer = 0
        year = 1950
        for offset, change in enumerate(changes):
            current += change
            if current > answer:
                answer, year = current, 1950 + offset
        return year


if __name__ == "__main__":
    solution = Solution()
    assert solution.maximumPopulation([[1993, 1999], [2000, 2010]]) == 1993
    print("1854 passed")
