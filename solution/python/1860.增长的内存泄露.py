from typing import List


class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        second = 1
        while True:
            if memory1 >= memory2:
                if memory1 < second:
                    return [second, memory1, memory2]
                memory1 -= second
            else:
                if memory2 < second:
                    return [second, memory1, memory2]
                memory2 -= second
            second += 1


if __name__ == "__main__":
    solution = Solution()
    assert solution.memLeak(2, 2) == [3, 1, 0]
    print("1860 passed")
