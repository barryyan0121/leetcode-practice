class Solution:
    def addNegabinary(self, arr1: list[int], arr2: list[int]) -> list[int]:
        answer = []
        carry = 0
        left, right = len(arr1) - 1, len(arr2) - 1
        while left >= 0 or right >= 0 or carry:
            total = carry
            if left >= 0:
                total += arr1[left]
                left -= 1
            if right >= 0:
                total += arr2[right]
                right -= 1
            answer.append(total & 1)
            carry = -(total >> 1)
        while len(answer) > 1 and answer[-1] == 0:
            answer.pop()
        return answer[::-1]


if __name__ == "__main__":
    test_cases = [([1, 1, 1, 1, 1], [1, 0, 1], [1, 0, 0, 0, 0]), ([0], [0], [0])]
    for _, (arr1, arr2, expected) in enumerate(test_cases):
        assert Solution().addNegabinary(arr1, arr2) == expected
