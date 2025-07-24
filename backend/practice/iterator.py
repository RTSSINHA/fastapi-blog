class InfiniteNaturalNumbers():

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        num = self.num
        self.num += 1
        return num

value = InfiniteNaturalNumbers()
print(next(value))
print(next(value))


# prices = [10, 20, 30, 40, 50]

# price_iter = prices.__iter__()

# while True:
#     try:
#         print(price_iter.__next__())
#     except StopIteration:
#         break


