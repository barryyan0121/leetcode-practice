"""2833. 离原点最远的点"""


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        return abs(moves.count("L") - moves.count("R")) + moves.count("_")


if __name__ == "__main__":
    assert Solution().furthestDistanceFromOrigin("L_RL__R") == 3
