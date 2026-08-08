class ArrayReader:
    def __init__(self, values: list[int]):
        self.values = values

    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
        return (sum(self.values[l : r + 1]) > sum(self.values[x : y + 1])) - (
            sum(self.values[l : r + 1]) < sum(self.values[x : y + 1])
        )

    def length(self) -> int:
        return len(self.values)


class Solution:
    def getIndex(self, reader: "ArrayReader") -> int:
        left, right = 0, reader.length() - 1
        while left < right:
            mid = (left + right) // 2
            if (right - left + 1) % 2 == 0:
                if reader.compareSub(left, mid, mid + 1, right) > 0:
                    right = mid
                else:
                    left = mid + 1
            else:
                comparison = reader.compareSub(left, mid - 1, mid + 1, right)
                if comparison == 0:
                    return mid
                if comparison > 0:
                    right = mid - 1
                else:
                    left = mid + 1
        return left


if __name__ == "__main__":
    test_cases = [([7, 7, 7, 7, 10, 7, 7, 7], 4), ([6, 6, 12], 2)]
    for _, (values, expected) in enumerate(test_cases):
        assert Solution().getIndex(ArrayReader(values)) == expected
