class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def ok(start: int) -> int:
            need = [0, 0]
            h = 0
            while True:
                h += 1
                need[(h + start) & 1] += h
                if need[0] > red or need[1] > blue:
                    return h - 1

        return max(ok(0), ok(1))


if __name__ == "__main__":
    assert Solution().maxHeightOfTriangle(2, 4) == 3
    assert Solution().maxHeightOfTriangle(10, 1) == 2
