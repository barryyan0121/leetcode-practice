"""2456. 最流行的视频创作者"""


class Solution:
    def mostPopularCreator(
        self, creators: list[str], ids: list[str], views: list[int]
    ) -> list[list[str]]:
        total = {}
        best = {}
        for creator, video_id, view in zip(creators, ids, views):
            total[creator] = total.get(creator, 0) + view
            if (
                creator not in best
                or view > best[creator][0]
                or (view == best[creator][0] and video_id < best[creator][1])
            ):
                best[creator] = (view, video_id)
        maximum = max(total.values())
        return [
            [creator, best[creator][1]]
            for creator in total
            if total[creator] == maximum
        ]


if __name__ == "__main__":
    assert Solution().mostPopularCreator(
        ["alice", "bob", "alice", "chris"],
        ["one", "two", "three", "four"],
        [5, 10, 5, 4],
    ) == [["alice", "one"], ["bob", "two"]]
