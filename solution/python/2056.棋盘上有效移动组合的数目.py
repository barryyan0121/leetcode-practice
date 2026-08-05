"""2056. 棋盘上有效移动组合的数目"""


class Solution:
    def countCombinations(self, pieces: list[str], positions: list[list[int]]) -> int:
        directions = {
            "rook": ((1, 0), (-1, 0), (0, 1), (0, -1)),
            "bishop": ((1, 1), (1, -1), (-1, 1), (-1, -1)),
            "queen": (
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1),
                (1, 1),
                (1, -1),
                (-1, 1),
                (-1, -1),
            ),
        }
        choices = []
        for piece, (row, col) in zip(pieces, positions):
            moves = [(row, col, 0)]
            if piece == "knight":
                moves.extend(
                    (row + dr, col + dc, 1)
                    for dr, dc in (
                        (1, 2),
                        (1, -2),
                        (-1, 2),
                        (-1, -2),
                        (2, 1),
                        (2, -1),
                        (-2, 1),
                        (-2, -1),
                    )
                    if 1 <= row + dr <= 8 and 1 <= col + dc <= 8
                )
            else:
                for dr, dc in directions[piece]:
                    for distance in range(1, 8):
                        nr, nc = row + dr * distance, col + dc * distance
                        if not (1 <= nr <= 8 and 1 <= nc <= 8):
                            break
                        moves.append((nr, nc, distance))
            choices.append(moves)

        answer = 0

        def search(index: int, selected: list[tuple[int, int, int]]) -> None:
            nonlocal answer
            if index == len(choices):
                for time in range(max(move[2] for move in selected) + 1):
                    occupied = set()
                    for (row, col, duration), (start_row, start_col) in zip(
                        selected, positions
                    ):
                        if duration:
                            row = (
                                start_row
                                + (row - start_row) * min(time, duration) // duration
                            )
                            col = (
                                start_col
                                + (col - start_col) * min(time, duration) // duration
                            )
                        if (row, col) in occupied:
                            return
                        occupied.add((row, col))
                answer += 1
                return
            for move in choices[index]:
                search(index + 1, selected + [move])

        search(0, [])
        return answer


if __name__ == "__main__":
    test_cases = [(('["rook"]', "[[1, 1]]"), 15)]
    test_cases = [((["rook"], [[1, 1]]), 15)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countCombinations(*args) == expected
