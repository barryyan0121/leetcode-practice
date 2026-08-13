"""2868. 单词游戏"""


class Solution:
    def canAliceWin(self, a: list[str], b: list[str]) -> bool:
        alice = [""] * 26
        bob = [""] * 26
        for word in a:
            index = ord(word[0]) - 97
            alice[index] = max(alice[index], word)
        for word in b:
            index = ord(word[0]) - 97
            bob[index] = max(bob[index], word)
        current = min(a)
        turn = 1
        while True:
            words = bob if turn else alice
            index = ord(current[0]) - 97
            if words[index] > current:
                current = words[index]
            elif index == 25 or not words[index + 1]:
                return bool(turn)
            else:
                current = words[index + 1]
            turn ^= 1


if __name__ == "__main__":
    assert not Solution().canAliceWin(["avokado", "dabar"], ["brazil"])
    assert Solution().canAliceWin(
        ["ananas", "atlas", "banana"], ["albatros", "cikla", "nogomet"]
    )
