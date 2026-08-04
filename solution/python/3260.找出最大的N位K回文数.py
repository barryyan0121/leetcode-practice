class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        half = (n + 1) // 2
        weights = []
        power = 1
        powers = [1] * n
        for index in range(1, n):
            power = power * 10 % k
            powers[index] = power
        for index in range(half):
            mirror = n - 1 - index
            weights.append(
                (powers[index] + (0 if mirror == index else powers[mirror])) % k
            )

        suffix = [0] * (half + 1)
        suffix[half] = 1
        for index in range(half - 1, -1, -1):
            mask = 0
            digits = range(1, 10) if index == 0 else range(10)
            for digit in digits:
                shift = digit * weights[index] % k
                for remainder in range(k):
                    if suffix[index + 1] >> remainder & 1:
                        mask |= 1 << ((shift + remainder) % k)
            suffix[index] = mask

        result = []
        remainder = 0
        for index, weight in enumerate(weights):
            digits = range(9, 0, -1) if index == 0 else range(9, -1, -1)
            for digit in digits:
                needed = (-remainder - digit * weight) % k
                if suffix[index + 1] >> needed & 1:
                    result.append(str(digit))
                    remainder = (remainder + digit * weight) % k
                    break
        left = "".join(result)
        return left + left[: n // 2][::-1]


if __name__ == "__main__":
    test_cases = [((3, 5), "595"), ((1, 4), "8"), ((5, 6), "89898")]
    for _, ((n, k), expected) in enumerate(test_cases):
        assert Solution().largestPalindrome(n, k) == expected
