class Solution:
    def canMouseWin(self, grid: list[str], catJump: int, mouseJump: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        open_cells = [grid[r][c] != "#" for r in range(rows) for c in range(cols)]
        mouse = cat = food = 0
        for r in range(rows):
            for c in range(cols):
                position = r * cols + c
                if grid[r][c] == "M":
                    mouse = position
                elif grid[r][c] == "C":
                    cat = position
                elif grid[r][c] == "F":
                    food = position

        def jumps(position: int, distance: int) -> list[int]:
            row, col = divmod(position, cols)
            result = [position]
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                for step in range(1, distance + 1):
                    nr, nc = row + dr * step, col + dc * step
                    if not (0 <= nr < rows and 0 <= nc < cols):
                        break
                    target = nr * cols + nc
                    if not open_cells[target]:
                        break
                    result.append(target)
            return result

        mouse_moves = [
            jumps(position, mouseJump) if open_cells[position] else []
            for position in range(rows * cols)
        ]
        cat_moves = [
            jumps(position, catJump) if open_cells[position] else []
            for position in range(rows * cols)
        ]

        state_count = rows * cols * rows * cols * 2

        def state_id(mouse_position: int, cat_position: int, turn: int) -> int:
            return (mouse_position * rows * cols + cat_position) * 2 + turn

        result = [-1] * state_count
        degree = [0] * state_count
        predecessors = [[] for _ in range(state_count)]
        queue = []
        for mouse_position in range(rows * cols):
            if not open_cells[mouse_position]:
                continue
            for cat_position in range(rows * cols):
                if not open_cells[cat_position]:
                    continue
                for turn in (0, 1):
                    current = state_id(mouse_position, cat_position, turn)
                    if mouse_position == food:
                        result[current] = 1
                    elif cat_position == food or mouse_position == cat_position:
                        result[current] = 0
                    else:
                        successors = (
                            [
                                state_id(next_mouse, cat_position, 1)
                                for next_mouse in mouse_moves[mouse_position]
                            ]
                            if turn == 0
                            else [
                                state_id(mouse_position, next_cat, 0)
                                for next_cat in cat_moves[cat_position]
                            ]
                        )
                        degree[current] = len(successors)
                        for successor in successors:
                            predecessors[successor].append(current)
                    if result[current] != -1:
                        queue.append(current)

        head = 0
        while head < len(queue):
            current = queue[head]
            head += 1
            for previous in predecessors[current]:
                if result[previous] != -1:
                    continue
                turn = previous & 1
                if (turn == 0 and result[current] == 1) or (
                    turn == 1 and result[current] == 0
                ):
                    result[previous] = result[current]
                    queue.append(previous)
                else:
                    degree[previous] -= 1
                    if degree[previous] == 0:
                        result[previous] = 0 if turn == 0 else 1
                        queue.append(previous)
        return result[state_id(mouse, cat, 0)] == 1


if __name__ == "__main__":
    test_cases = [
        ((["####F", "#C...", "M...."], 1, 2), True),
        ((["M.C...F"], 1, 4), True),
        ((["M.C...F"], 1, 3), False),
        ((["C...#", "...#F", "....#", "M...."], 2, 5), False),
        (([".M...", "..#..", "#..#.", "C#.#.", "...#F"], 3, 1), True),
    ]
    for index, (args, expected) in enumerate(test_cases):
        assert Solution().canMouseWin(*args) == expected, index
