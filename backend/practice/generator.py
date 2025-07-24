def return_values():

    yield 1
    yield 2
    yield "Three"

values = return_values()

while True:
    try:
        print(values.__next__())
    except StopIteration:
        break
