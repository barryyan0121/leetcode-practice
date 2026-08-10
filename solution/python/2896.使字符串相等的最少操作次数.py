"""2896. 使字符串相等的最少操作次数"""


class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        positions = [
            index for index, (left, right) in enumerate(zip(s1, s2)) if left != right
        ]
        if len(positions) % 2:
            return -1
        if not positions:
            return 0
        dynamic = [0, x]
        for index in range(2, len(positions) + 1):
            dynamic.append(
                min(
                    dynamic[-1] + x,
                    dynamic[-2] + 2 * (positions[index - 1] - positions[index - 2]),
                )
            )
        return dynamic[-1] // 2


if __name__ == "__main__":
    assert Solution().minOperations("1100011000", "0101001010", 2) == 4
