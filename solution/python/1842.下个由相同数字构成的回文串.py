class Solution:
    def nextPalindrome(self, num: str) -> str:
        half_length = (len(num) + 1) // 2
        left = list(num[:half_length])
        pivot = len(left) - 2
        while pivot >= 0 and left[pivot] >= left[pivot + 1]:
            pivot -= 1
        if pivot < 0:
            return ""
        successor = len(left) - 1
        while left[successor] <= left[pivot]:
            successor -= 1
        left[pivot], left[successor] = left[successor], left[pivot]
        left[pivot + 1 :] = reversed(left[pivot + 1 :])
        prefix = "".join(left)
        return prefix + prefix[-2::-1] if len(num) % 2 else prefix + prefix[::-1]


if __name__ == "__main__":
    solution = Solution()
    assert solution.nextPalindrome("123321") == "132231"
    assert solution.nextPalindrome("999") == ""
    print("1842 passed")
