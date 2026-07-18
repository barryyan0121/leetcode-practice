class Solution:
    def maxAbsValExpr(self, arr1: list[int], arr2: list[int]) -> int:
        answer = 0
        for sign1 in (-1, 1):
            for sign2 in (-1, 1):
                values = [
                    sign1 * first + sign2 * second + index
                    for index, (first, second) in enumerate(zip(arr1, arr2))
                ]
                answer = max(answer, max(values) - min(values))
        return answer


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4], [-1, 4, 5, 6], 13),
        ([1, -2, -5, 0, 10], [0, -2, -1, -7, -4], 20),
        ([0, 0], [0, 0], 1),
    ]
    for _, (arr1, arr2, expected) in enumerate(test_cases):
        assert Solution().maxAbsValExpr(arr1, arr2) == expected
