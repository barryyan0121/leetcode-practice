class Solution:
    def minimumNumbers(self, num, k):
        if num == 0:
            return 0
        for i in range(1, 11):
            if i * k <= num and (i * k) % 10 == num % 10:
                return i
        return -1


if __name__ == "__main__":
    assert Solution().minimumNumbers(58, 9) == 2
