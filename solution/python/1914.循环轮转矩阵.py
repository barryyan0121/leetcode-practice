"""1914. 循环轮转矩阵"""


class Solution:
    def rotateGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        rows, cols = len(grid), len(grid[0])
        for layer in range(min(rows, cols) // 2):
            values = []
            values.extend(grid[layer][j] for j in range(layer, cols - layer - 1))
            values.extend(
                grid[i][cols - layer - 1] for i in range(layer, rows - layer - 1)
            )
            values.extend(
                grid[rows - layer - 1][j] for j in range(cols - layer - 1, layer, -1)
            )
            values.extend(grid[i][layer] for i in range(rows - layer - 1, layer, -1))
            shift = k % len(values)
            values = values[shift:] + values[:shift]
            index = 0
            for j in range(layer, cols - layer - 1):
                grid[layer][j] = values[index]
                index += 1
            for i in range(layer, rows - layer - 1):
                grid[i][cols - layer - 1] = values[index]
                index += 1
            for j in range(cols - layer - 1, layer, -1):
                grid[rows - layer - 1][j] = values[index]
                index += 1
            for i in range(rows - layer - 1, layer, -1):
                grid[i][layer] = values[index]
                index += 1
        return grid


if __name__ == "__main__":
    assert Solution().rotateGrid([[40, 10], [30, 20]], 1) == [[10, 20], [40, 30]]
