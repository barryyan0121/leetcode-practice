# @lc app=leetcode.cn id=1472 lang=python3


class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        self.history = self.history[: self.current + 1] + [url]
        self.current += 1

    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]


if __name__ == "__main__":

    def run_case():
        browser = BrowserHistory("leetcode.com")
        browser.visit("google.com")
        browser.visit("facebook.com")
        return browser.back(1) == "google.com" and browser.forward(1) == "facebook.com"

    test_cases = [(run_case, (), True)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1472 题 "设计浏览器历史记录" 所有测试用例通过')
