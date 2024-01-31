#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount
    def add_item(self, title, price, quantity=1):
        self.most_recent_item = [title, price, quantity]
        self.total += price * quantity
        while quantity > 0:
          self.items.append(title)
          quantity -= 1
    def apply_discount(self):
        discount = (self.discount/100)*self.total
        self.total -= discount
        print(f"After the discount, the total comes to ${int(self.total)}.") if self.discount > 0 else print("There is no discount to apply.")
    def void_last_transaction(self):
        self.items.pop()
        while self.most_recent_item[2] > 0:
          self.total -= self.most_recent_item[1]
          self.most_recent_item[2] -= 1