class Solution:
    def countShips(self, sea: "Sea", topRight: "Point", bottomLeft: "Point") -> int:
        if (
            bottomLeft.x > topRight.x
            or bottomLeft.y > topRight.y
            or not sea.hasShips(topRight, bottomLeft)
        ):
            return 0
        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1
        middle_x = (topRight.x + bottomLeft.x) // 2
        middle_y = (topRight.y + bottomLeft.y) // 2
        return sum(
            self.countShips(sea, Point(right_x, right_y), Point(left_x, left_y))
            for left_x, left_y, right_x, right_y in (
                (bottomLeft.x, bottomLeft.y, middle_x, middle_y),
                (middle_x + 1, bottomLeft.y, topRight.x, middle_y),
                (bottomLeft.x, middle_y + 1, middle_x, topRight.y),
                (middle_x + 1, middle_y + 1, topRight.x, topRight.y),
            )
        )


if __name__ == "__main__":

    class Point:
        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y

    class Sea:
        def __init__(self, ships):
            self.ships = ships

        def hasShips(self, top_right, bottom_left):
            return any(
                bottom_left.x <= x <= top_right.x and bottom_left.y <= y <= top_right.y
                for x, y in self.ships
            )

    test_cases = [({(1, 1), (2, 2)}, Point(3, 3), Point(0, 0), 2)]
    for _, (ships, top_right, bottom_left, expected) in enumerate(test_cases):
        assert Solution().countShips(Sea(ships), top_right, bottom_left) == expected
