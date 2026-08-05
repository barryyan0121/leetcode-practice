class Solution:
    def goodSubsetofBinaryMatrix(self, grid: list[list[int]]) -> list[int]:
        masks = {}
        for i, row in enumerate(grid):
            mask = sum(v << j for j, v in enumerate(row))
            if mask == 0:
                return [i]
            masks[mask] = i
        for a, i in masks.items():
            for b, j in masks.items():
                if not a & b:
                    return sorted((i, j))
        return []


if __name__ == "__main__":
    assert Solution().goodSubsetofBinaryMatrix([[0, 1], [1, 0]]) == [0, 1]
