from collections import defaultdict
from heapq import heappop, heappush


class AuctionSystem:
    def __init__(self):
        self.bids = {}
        self.heaps = defaultdict(list)

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        self.bids[(itemId, userId)] = bidAmount
        heappush(self.heaps[itemId], (-bidAmount, -userId, userId))

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        self.addBid(userId, itemId, newAmount)

    def removeBid(self, userId: int, itemId: int) -> None:
        self.bids.pop((itemId, userId), None)

    def getHighestBidder(self, itemId: int) -> int:
        heap = self.heaps[itemId]
        while heap:
            _, _, userId = heap[0]
            if (itemId, userId) in self.bids and self.bids[(itemId, userId)] == -heap[
                0
            ][0]:
                return userId
            heappop(heap)
        return -1


if __name__ == "__main__":
    auction = AuctionSystem()
    auction.addBid(1, 1, 5)
    auction.addBid(2, 1, 5)
    assert auction.getHighestBidder(1) == 2
    auction.updateBid(1, 1, 6)
    assert auction.getHighestBidder(1) == 1
    auction.removeBid(1, 1)
    assert auction.getHighestBidder(1) == 2
