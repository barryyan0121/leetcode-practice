"""2069. 模拟行走机器人 II"""


class Robot:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.row = self.col = 0
        self.direction = 0
        self.directions = ("East", "North", "West", "South")

    def step(self, num: int) -> None:
        perimeter = 2 * (self.width + self.height) - 4
        num %= perimeter
        if num == 0:
            num = perimeter
        vectors = ((1, 0), (0, 1), (-1, 0), (0, -1))
        for _ in range(num):
            dr, dc = vectors[self.direction]
            nr, nc = self.row + dr, self.col + dc
            if not (0 <= nr < self.width and 0 <= nc < self.height):
                self.direction = (self.direction + 1) % 4
                dr, dc = vectors[self.direction]
                nr, nc = self.row + dr, self.col + dc
            self.row, self.col = nr, nc

    def getPos(self) -> list[int]:
        return [self.row, self.col]

    def getDir(self) -> str:
        return self.directions[self.direction]


if __name__ == "__main__":
    test_cases = [((6, 3, 2), ([2, 0], "East"))]
    for _, (args, expected) in enumerate(test_cases):
        robot = Robot(args[0], args[1])
        robot.step(args[2])
        assert (robot.getPos(), robot.getDir()) == expected
