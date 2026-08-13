"""2237. 计算街道上满足所需亮度的位置数量"""


class Solution:
    def meetRequirement(
        self, n: int, lights: list[list[int]], requirement: list[int]
    ) -> int:
        difference = [0] * (n + 1)
        for position, radius in lights:
            difference[max(0, position - radius)] += 1
            difference[min(n, position + radius + 1)] -= 1
        answer = current = 0
        for i in range(n):
            current += difference[i]
            answer += current >= requirement[i]
        return answer

if __name__ == "__main__":
    assert Solution().meetRequirement(5, [[0, 1], [1, 0]], [1, 1, 0, 0, 0]) == 5
