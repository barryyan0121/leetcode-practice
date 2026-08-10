"""2818. 应用操作最大化分数"""


class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        modulo = 10**9 + 7
        scores = []
        for value in nums:
            number, score, factor = value, 0, 2
            while factor * factor <= number:
                if number % factor == 0:
                    score += 1
                    while number % factor == 0:
                        number //= factor
                factor += 1
            scores.append(score + (number > 1))
        left = [-1] * len(nums)
        stack = []
        for index, score in enumerate(scores):
            while stack and scores[stack[-1]] < score:
                stack.pop()
            left[index] = stack[-1] if stack else -1
            stack.append(index)
        right = [len(nums)] * len(nums)
        stack = []
        for index in range(len(nums) - 1, -1, -1):
            while stack and scores[stack[-1]] <= scores[index]:
                stack.pop()
            right[index] = stack[-1] if stack else len(nums)
            stack.append(index)
        choices = sorted(
            (
                (value, (index - left[index]) * (right[index] - index))
                for index, value in enumerate(nums)
            ),
            reverse=True,
        )
        answer = 1
        for value, count in choices:
            use = min(k, count)
            answer = answer * pow(value, use, modulo) % modulo
            k -= use
            if not k:
                break
        return answer


if __name__ == "__main__":
    assert Solution().maximumScore([8, 3, 9, 3, 8], 2) == 81
