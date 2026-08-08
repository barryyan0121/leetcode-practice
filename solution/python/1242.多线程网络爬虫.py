from typing import List


class Solution:
    def crawl(self, startUrl: str, htmlParser: "HtmlParser") -> List[str]:
        host = startUrl.split("/")[2]
        seen = {startUrl}
        stack = [startUrl]
        while stack:
            for url in htmlParser.getUrls(stack.pop()):
                if url.split("/")[2] == host and url not in seen:
                    seen.add(url)
                    stack.append(url)
        return list(seen)


if __name__ == "__main__":

    class HtmlParser:
        def getUrls(self, url: str) -> List[str]:
            return {
                "http://news.yahoo.com": [
                    "http://news.yahoo.com/news",
                    "http://news.google.com",
                ],
                "http://news.yahoo.com/news": ["http://news.yahoo.com"],
            }.get(url, [])

    test_cases = [
        (
            "http://news.yahoo.com",
            {"http://news.yahoo.com", "http://news.yahoo.com/news"},
        )
    ]
    for _, (start_url, expected) in enumerate(test_cases):
        assert set(Solution().crawl(start_url, HtmlParser())) == expected
