#
# @lc app=leetcode.cn id=535 lang=python3
# @lcpr version=30203
#
# [535] TinyURL 的加密与解密
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Codec:
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    prefix = "http://tinyurl.com/"

    def __init__(self):
        self.long2short: Dict[str, str] = {}
        self.short2long: Dict[str, str] = {}
        self.counter = 1

    def _to_base62(self, value: int) -> str:
        chars = []
        while value:
            value, rem = divmod(value, 62)
            chars.append(self.alphabet[rem])
        return "".join(reversed(chars)) or "0"

    def encode(self, longUrl: str) -> str:
        if longUrl in self.long2short:
            return self.long2short[longUrl]
        short = self.prefix + self._to_base62(self.counter)
        self.counter += 1
        self.long2short[longUrl] = short
        self.short2long[short] = longUrl
        return short

    def decode(self, shortUrl: str) -> str:
        return self.short2long.get(shortUrl, "")


# @lc code=end


if __name__ == "__main__":
    codec = Codec()

    def run_case(urls: List[str]) -> bool:
        codec = Codec()
        encoded = [codec.encode(url) for url in urls]
        assert len(set(encoded)) == len(urls)
        for url, short in zip(urls, encoded):
            assert codec.decode(short) == url
        assert codec.encode(urls[0]) == encoded[0]
        return True

    test_cases = [
        (run_case, (["https://leetcode.com/problems/design-tinyurl"],), True),
        (
            run_case,
            (["https://example.com/a", "https://example.com/b"],),
            True,
        ),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)


#
# @lcpr case=start
# ["Codec","encode","decode"]\n
# [[],["https://leetcode.com/problems/design-tinyurl"],["http://tinyurl.com/1"]]\n
# @lcpr case=end
#
