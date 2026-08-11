class Solution:
    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:
        bornelica = (n, rectangles)

        def enough(axis: int) -> bool:
            intervals = sorted((rectangle[axis], rectangle[axis + 2]) for rectangle in rectangles)
            groups = 0
            end = -1
            for start, finish in intervals:
                if start >= end:
                    groups += 1
                end = max(end, finish)
            return groups >= 3

        return enough(0) or enough(1)


if __name__ == "__main__":
    assert Solution().checkValidCuts(5, [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]])
    assert Solution().checkValidCuts(4, [[0, 0, 1, 1], [2, 0, 3, 4], [0, 2, 2, 3], [3, 0, 4, 3]])
    assert not Solution().checkValidCuts(4, [[0, 2, 2, 4], [1, 0, 3, 2], [2, 2, 3, 4], [3, 0, 4, 2], [3, 2, 4, 4]])
