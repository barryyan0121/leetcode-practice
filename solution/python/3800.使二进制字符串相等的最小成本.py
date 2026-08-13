class Solution:
    def minimumCost(
        self, s: str, t: str, flipCost: int, swapCost: int, crossCost: int
    ) -> int:
        zero_to_one = sum(a == "0" and b == "1" for a, b in zip(s, t))
        one_to_zero = sum(a == "1" and b == "0" for a, b in zip(s, t))
        opposite = min(zero_to_one, one_to_zero)
        answer = opposite * min(swapCost, 2 * flipCost)
        remaining = abs(zero_to_one - one_to_zero)
        answer += (remaining // 2) * min(crossCost + swapCost, 2 * flipCost)
        answer += (remaining % 2) * flipCost
        return answer


if __name__ == "__main__":
    s = Solution()
    assert s.minimumCost("01000", "10111", 10, 2, 2) == 16
    assert s.minimumCost("001", "110", 2, 100, 100) == 6
    assert s.minimumCost("1010", "1010", 5, 5, 5) == 0
