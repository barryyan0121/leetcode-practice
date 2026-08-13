from itertools import permutations
from typing import List


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        answer = []
        for top, left, right, bottom in permutations(words, 4):
            if (
                top[0] == left[0]
                and top[3] == right[0]
                and bottom[0] == left[3]
                and bottom[3] == right[3]
            ):
                answer.append([top, left, right, bottom])
        return sorted(answer)


if __name__ == "__main__":
    s = Solution()
    assert s.wordSquares(["able", "area", "echo", "also"]) == [
        ["able", "area", "echo", "also"],
        ["area", "able", "also", "echo"],
    ]
    assert s.wordSquares(["code", "cafe", "eden", "edge"]) == []
