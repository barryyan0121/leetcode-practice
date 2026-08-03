# @lc app=leetcode.cn id=1348 lang=python3

from collections import defaultdict


class TweetCounts:
    def __init__(self):
        self.tweets = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(
        self, freq: str, tweetName: str, startTime: int, endTime: int
    ):
        size = {"minute": 60, "hour": 3600, "day": 86400}[freq]
        counts = [0] * ((endTime - startTime) // size + 1)
        for time in self.tweets[tweetName]:
            if startTime <= time <= endTime:
                counts[(time - startTime) // size] += 1
        return counts


if __name__ == "__main__":
    test_cases = ["minute frequency"]
    for _, _case in enumerate(test_cases):
        pass
    tweets = TweetCounts()
    tweets.recordTweet("tweet3", 0)
    tweets.recordTweet("tweet3", 10)
    tweets.recordTweet("tweet3", 60)
    assert tweets.getTweetCountsPerFrequency("minute", "tweet3", 0, 59) == [2]
    assert tweets.getTweetCountsPerFrequency("minute", "tweet3", 0, 60) == [2, 1]
    print('第 1348 题 "推文计数" 所有测试用例通过')
