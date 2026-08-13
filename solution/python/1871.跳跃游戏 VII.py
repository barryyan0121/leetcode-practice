from typing import List


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        reachable = [False] * len(s)
        reachable[0] = True
        window = 0
        for index in range(1, len(s)):
            if index - minJump >= 0 and reachable[index - minJump]:
                window += 1
            if index - maxJump - 1 >= 0 and reachable[index - maxJump - 1]:
                window -= 1
            reachable[index] = s[index] == "0" and window > 0
        return reachable[-1]


if __name__ == "__main__":
    solver = Solution()
    assert solver.canReach("011010", 2, 3)
    assert not solver.canReach("01101110", 2, 3)
