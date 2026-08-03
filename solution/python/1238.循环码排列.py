from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        return [start ^ index ^ (index >> 1) for index in range(1 << n)]


if __name__ == "__main__":
    test_cases = [(2, 3), (3, 2)]
    for _, (n, start) in enumerate(test_cases):
        answer = Solution().circularPermutation(n, start)
        assert answer[0] == start and len(set(answer)) == 1 << n
        assert all(
            (a ^ b).bit_count() == 1 for a, b in zip(answer, answer[1:] + answer)
        )
