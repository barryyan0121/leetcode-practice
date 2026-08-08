class SparseVector:
    def __init__(self, nums: list[int]):
        self.values = {index: value for index, value in enumerate(nums) if value}

    def dotProduct(self, vec: "SparseVector") -> int:
        if len(self.values) > len(vec.values):
            return vec.dotProduct(self)
        return sum(
            value * vec.values.get(index, 0) for index, value in self.values.items()
        )


if __name__ == "__main__":
    test_cases = [([1, 0, 0, 2, 3], [0, 3, 0, 4, 0], 8)]
    for _, (first, second, expected) in enumerate(test_cases):
        assert SparseVector(first).dotProduct(SparseVector(second)) == expected
