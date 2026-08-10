class Solution:
    def sumBase(self, n: int, k: int) -> int:
        result = 0
        while n:
            result += n % k
            n //= k
        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.sumBase(34, 6) == 9
    print("1837 passed")
