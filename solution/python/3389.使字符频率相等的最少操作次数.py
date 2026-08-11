from collections import Counter


class Solution:
    def makeStringGood(self, s: str) -> int:
        count = Counter(s)
        occurrences = [count[chr(ord("a") + index)] for index in range(26)]
        answer = len(s)
        dp = [0] * 27
        for target in range(max(occurrences) + 1):
            dp[25] = min(occurrences[25], abs(occurrences[25] - target))
            for index in range(24, -1, -1):
                current, following = occurrences[index], occurrences[index + 1]
                dp[index] = dp[index + 1] + min(current, abs(current - target))
                if following < target:
                    if current < target:
                        dp[index] = min(
                            dp[index], dp[index + 2] + max(current, target - following)
                        )
                    else:
                        dp[index] = min(
                            dp[index],
                            dp[index + 2] + max(current - target, target - following),
                        )
            answer = min(answer, dp[0])
        return answer


if __name__ == "__main__":
    assert Solution().makeStringGood("acab") == 1
    assert Solution().makeStringGood("wddw") == 0
    assert Solution().makeStringGood("aaabc") == 2
