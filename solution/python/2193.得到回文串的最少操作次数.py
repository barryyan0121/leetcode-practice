"""2193. 得到回文串的最少操作次数"""


class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        chars = list(s)
        moves = 0
        left, right = 0, len(chars) - 1
        while left < right:
            match = right
            while match > left and chars[match] != chars[left]:
                match -= 1
            if match == left:
                chars[left], chars[left + 1] = chars[left + 1], chars[left]
                moves += 1
            else:
                while match < right:
                    chars[match], chars[match + 1] = chars[match + 1], chars[match]
                    match += 1
                    moves += 1
                left += 1
                right -= 1
        return moves


if __name__ == "__main__":
    assert Solution().minMovesToMakePalindrome("aabb") == 2
