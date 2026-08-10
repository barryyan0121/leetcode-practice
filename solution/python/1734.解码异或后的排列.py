from typing import List


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        first = 0
        for value in range(1, n + 1):
            first ^= value
        for i in range(1, len(encoded), 2):
            first ^= encoded[i]
        result = [first]
        for value in encoded:
            result.append(result[-1] ^ value)
        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.decode([3, 1]) == [1, 2, 3]
    assert solution.decode([6, 5, 4, 6]) == [2, 4, 1, 5, 3]
    print("1734 passed")
