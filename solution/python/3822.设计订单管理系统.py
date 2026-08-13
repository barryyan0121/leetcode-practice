from typing import List


class OrderManagementSystem:
    def __init__(self):
        self.orders = {}
        self.groups = {}

    def addOrder(self, orderId: int, orderType: str, price: int) -> None:
        self.orders[orderId] = (orderType, price)
        self.groups.setdefault((orderType, price), set()).add(orderId)

    def modifyOrder(self, orderId: int, newPrice: int) -> None:
        order_type, old_price = self.orders[orderId]
        self.groups[(order_type, old_price)].remove(orderId)
        self.orders[orderId] = (order_type, newPrice)
        self.groups.setdefault((order_type, newPrice), set()).add(orderId)

    def cancelOrder(self, orderId: int) -> None:
        order_type, price = self.orders.pop(orderId)
        self.groups[(order_type, price)].remove(orderId)

    def getOrdersAtPrice(self, orderType: str, price: int) -> List[int]:
        return list(self.groups.get((orderType, price), set()))


if __name__ == "__main__":
    system = OrderManagementSystem()
    system.addOrder(1, "buy", 1)
    system.addOrder(2, "buy", 1)
    assert set(system.getOrdersAtPrice("buy", 1)) == {1, 2}
    system.modifyOrder(1, 3)
    system.cancelOrder(2)
    assert system.getOrdersAtPrice("buy", 1) == []
