class Solution:
    @staticmethod
    def _numbers_and_exponent(n: int) -> tuple[int, int]:
        if n <= 0:
            return 0, 0
        numbers = exponent = 0
        bit = 0
        while (1 << bit) <= n:
            block = 1 << (bit + 1)
            full, remainder = divmod(n + 1, block)
            count = full * (1 << bit) + max(0, remainder - (1 << bit))
            numbers += count
            exponent += count * bit
            bit += 1
        return numbers, exponent

    def _prefix_exponent(self, position: int) -> int:
        left, right = 0, position
        while left < right:
            middle = (left + right + 1) // 2
            if self._numbers_and_exponent(middle)[0] <= position:
                left = middle
            else:
                right = middle - 1

        numbers, exponent = self._numbers_and_exponent(left)
        remaining = position - numbers
        value = left + 1
        bit = 0
        while remaining:
            if value >> bit & 1:
                exponent += bit
                remaining -= 1
            bit += 1
        return exponent

    def findProductsOfElements(self, queries: list[list[int]]) -> list[int]:
        answer = []
        for start, end, modulo in queries:
            exponent = self._prefix_exponent(end + 1) - self._prefix_exponent(start)
            answer.append(pow(2, exponent, modulo))
        return answer


if __name__ == "__main__":
    test_cases = [([[1, 3, 7]], [4]), ([[2, 5, 3], [7, 7, 4]], [2, 2])]
    for _, (queries, expected) in enumerate(test_cases):
        assert Solution().findProductsOfElements(queries) == expected
