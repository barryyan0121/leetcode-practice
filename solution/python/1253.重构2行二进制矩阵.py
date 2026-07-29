from typing import List


class Solution:
    def reconstructMatrix(
        self, upper: int, lower: int, colsum: List[int]
    ) -> List[List[int]]:
        top = [int(value == 2) for value in colsum]
        bottom = top[:]
        upper -= sum(top)
        lower -= sum(bottom)
        for index, value in enumerate(colsum):
            if value == 1:
                if upper:
                    top[index] = 1
                    upper -= 1
                else:
                    bottom[index] = 1
                    lower -= 1
        return [top, bottom] if upper == lower == 0 else []


if __name__ == "__main__":
    test_cases = [
        ((2, 1, [1, 1, 1]), [[1, 1, 0], [0, 0, 1]]),
        ((2, 3, [2, 2, 1, 1]), []),
    ]
    for _, ((upper, lower, colsum), expected) in enumerate(test_cases):
        assert Solution().reconstructMatrix(upper, lower, colsum) == expected
