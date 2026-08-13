"""2211. 统计道路上的碰撞次数"""


class Solution:
    def countCollisions(self, directions: str) -> int:
        directions = directions.lstrip("L").rstrip("R")
        return len(directions) - directions.count("S")


if __name__ == "__main__":
    assert Solution().countCollisions("RLRSLL") == 5
