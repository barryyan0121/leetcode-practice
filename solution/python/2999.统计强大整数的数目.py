class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        if any(int(char) > limit for char in s):
            return 0
        suffix = int(s)

        def count(value: int) -> int:
            if value < suffix:
                return 0
            digits = str(value)
            answer = 0
            for length in range(len(s), len(digits) + 1):
                prefix_len = length - len(s)
                if prefix_len == 0:
                    if length < len(digits) or suffix <= value:
                        answer += 1
                    continue
                if length < len(digits):
                    answer += limit * (limit + 1) ** (prefix_len - 1)
                    continue
                bound = digits[:prefix_len]
                ways = 0
                valid = True
                for index, char in enumerate(bound):
                    digit = int(char)
                    low = 1 if index == 0 else 0
                    ways += max(
                        0,
                        min(limit, digit - 1) - low + 1,
                    ) * (
                        limit + 1
                    ) ** (prefix_len - index - 1)
                    if digit < low or digit > limit:
                        valid = False
                        break
                if valid and suffix <= int(digits[prefix_len:]):
                    ways += 1
                answer += ways
            return answer

        return count(finish) - count(start - 1)


if __name__ == "__main__":
    solution = Solution()
    assert solution.numberOfPowerfulInt(1, 6000, 4, "124") == 5
    assert solution.numberOfPowerfulInt(15, 215, 6, "10") == 2
    assert solution.numberOfPowerfulInt(1000, 2000, 4, "3000") == 0
