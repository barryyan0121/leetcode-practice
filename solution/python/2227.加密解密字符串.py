"""2227. 加密解密字符串"""


class Encrypter:
    def __init__(self, keys: list[str], values: list[str], dictionary: list[str]):
        self.mapping = dict(zip(keys, values))
        self.counts = {}
        for word in dictionary:
            encrypted = self.encrypt(word)
            self.counts[encrypted] = self.counts.get(encrypted, 0) + 1

    def encrypt(self, word1: str) -> str:
        if any(char not in self.mapping for char in word1):
            return "#"
        return "".join(self.mapping[char] for char in word1)

    def decrypt(self, word2: str) -> int:
        return self.counts.get(word2, 0)
