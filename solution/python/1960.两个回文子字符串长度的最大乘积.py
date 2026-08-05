"""1960. 两个回文子字符串长度的最大乘积"""


class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)

        def odd_radii(text: str) -> list[int]:
            result = [0] * n
            left, right = 0, -1
            for i in range(n):
                radius = (
                    min(result[left + right - i], right - i + 1) if i <= right else 1
                )
                while (
                    i - radius >= 0
                    and i + radius < n
                    and text[i - radius] == text[i + radius]
                ):
                    radius += 1
                result[i] = radius
                if i + radius - 1 > right:
                    left, right = i - radius + 1, i + radius - 1
            return result

        odd = odd_radii(s)

        def ending_values(odd_radii: list[int]) -> list[int]:
            from collections import deque

            odd_queue = deque()
            values = [0] * n
            for end in range(n):
                if odd_radii[end]:
                    odd_queue.append((end, end + odd_radii[end] - 1))
                while odd_queue and odd_queue[0][1] < end:
                    odd_queue.popleft()
                if odd_queue:
                    values[end] = max(values[end], 2 * (end - odd_queue[0][0]) + 1)
            return values

        left_best = ending_values(odd)
        right_best = ending_values(odd_radii(s[::-1]))[::-1]
        for i in range(1, n):
            left_best[i] = max(left_best[i], left_best[i - 1])
        for i in range(n - 2, -1, -1):
            right_best[i] = max(right_best[i], right_best[i + 1])
        return max(left_best[i] * right_best[i + 1] for i in range(n - 1))


if __name__ == "__main__":
    test_cases = [(("ababbb",), 9), (("zaaaxbbby",), 9)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxProduct(*args) == expected
