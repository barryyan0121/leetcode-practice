"""2288. 价格减免"""


class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        result = []
        for word in sentence.split():
            if len(word) > 1 and word[0] == "$" and word[1:].isdigit():
                cents = int(word[1:]) * (100 - discount)
                result.append(f"${cents // 100}.{cents % 100:02d}")
            else:
                result.append(word)
        return " ".join(result)
