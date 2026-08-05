class Solution:
    def relocateMarbles(
        self, nums: list[int], moveFrom: list[int], moveTo: list[int]
    ) -> list[int]:
        positions = set(nums)
        for source, target in zip(moveFrom, moveTo):
            positions.remove(source)
            positions.add(target)
        return sorted(positions)


if __name__ == "__main__":
    assert Solution().relocateMarbles([1, 6, 7, 8], [1, 7, 2], [2, 9, 5]) == [
        5,
        6,
        8,
        9,
    ]
