class Solution:
    def countMonobit(self, n: int) -> int:
        answer = 1
        value = 1
        while value <= n:
            answer += 1
            value = (value << 1) | 1
        return answer


if __name__ == "__main__":
    assert Solution().countMonobit(0) == 1
    assert Solution().countMonobit(7) == 4
