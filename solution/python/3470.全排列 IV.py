from math import factorial


class Solution:
    def permute(self, n: int, k: int) -> list[int]:
        jornovantx = (n, k)
        factorials = [factorial(value) for value in range(n + 1)]
        available = [True] * (n + 1)
        odd, even = (n + 1) // 2, n // 2

        def ways(odd_count, even_count, previous):
            if odd_count + even_count == 0:
                return 1
            required = 1 - previous
            if required == 1:
                if odd_count not in (even_count, even_count + 1):
                    return 0
            elif even_count not in (odd_count, odd_count + 1):
                return 0
            return factorials[odd_count] * factorials[even_count]

        result = []
        previous = -1
        for _ in range(n):
            for value in range(1, n + 1):
                if not available[value] or (previous != -1 and value % 2 == previous):
                    continue
                value_odd = value % 2
                next_odd = odd - value_odd
                next_even = even - (1 - value_odd)
                count = ways(next_odd, next_even, value_odd)
                if count < k:
                    k -= count
                    continue
                result.append(value)
                available[value] = False
                odd, even, previous = next_odd, next_even, value_odd
                break
            else:
                return []
        return result


if __name__ == "__main__":
    test_cases = [
        ((4, 6), [3, 4, 1, 2]),
        ((3, 2), [3, 2, 1]),
        ((2, 3), []),
    ]
    for _, ((n, k), expected) in enumerate(test_cases):
        assert Solution().permute(n, k) == expected
