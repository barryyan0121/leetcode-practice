class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        length = len(word) - numFriends + 1
        mask = (1 << 64) - 1
        base = 911382323
        power = [1] * (len(word) + 1)
        prefix = [0] * (len(word) + 1)
        for index, char in enumerate(word):
            power[index + 1] = power[index] * base & mask
            prefix[index + 1] = (prefix[index] * base + ord(char)) & mask

        def same(left: int, right: int, size: int) -> bool:
            return ((prefix[left + size] - prefix[left] * power[size]) & mask) == (
                (prefix[right + size] - prefix[right] * power[size]) & mask
            )

        def greater(left: int, right: int) -> bool:
            low, high = 0, length + 1
            while high - low > 1:
                middle = (low + high) // 2
                if same(left, right, middle):
                    low = middle
                else:
                    high = middle
            return low == length or word[left + low] > word[right + low]

        best = 0
        for start in range(1, numFriends):
            if greater(start, best):
                best = start
        return word[best : best + length]


if __name__ == "__main__":
    assert Solution().answerString("dbca", 2) == "dbc"
    assert Solution().answerString("gggg", 4) == "g"
