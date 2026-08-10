"""2198. 单因数三元组"""


class Solution:
    def singleDivisorTriplet(self, nums: list[int]) -> int:
        counts = [0] * 101
        for value in nums:
            counts[value] += 1
        values = [value for value in range(1, 101) if counts[value]]
        answer = 0
        for i, a in enumerate(values):
            for j in range(i, len(values)):
                b = values[j]
                for k in range(j, len(values)):
                    c = values[k]
                    if sum((a + b + c) % value == 0 for value in (a, b, c)) != 1:
                        continue
                    if a == b == c:
                        answer += counts[a] * (counts[a] - 1) * (counts[a] - 2)
                    elif a == b:
                        answer += counts[a] * (counts[a] - 1) * counts[c] * 3
                    elif b == c:
                        answer += counts[a] * counts[b] * (counts[b] - 1) * 3
                    else:
                        answer += counts[a] * counts[b] * counts[c] * 6
        return answer


if __name__ == "__main__":
    assert Solution().singleDivisorTriplet([4, 6, 7, 3, 2]) == 12
    assert Solution().singleDivisorTriplet([1, 2, 2]) == 6
    assert Solution().singleDivisorTriplet([1, 1, 1]) == 0
