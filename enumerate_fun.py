
def index_by_value(tup1, x: int) -> tuple:
    result = []
    for index, current_value in enumerate(tup1):
        if current_value == x:
            result.append(index)
    return tuple(result)

def index_by_value(tup1, x: int) -> tuple:
    result = []
    for index in range(len(tup1)):
        if tup1[index] == x:
            result.append(index)
    return tuple(result)

#        0  1  2  3  4  5  6   7   8   9
tup1 = (10, 8, 5, 5, 3, 2, 5, 10, 30, 40)
print(index_by_value(tup1, 5))

for current_value in tup1:
    print(current_value)

for index in range(len(tup1)):
    print(index)

for index, cur_value in enumerate(tup1):
    print(index, cur_value)

lst1 = [1, 5, -3, 22, 12]
print(lst1)
for index, value in enumerate(lst1):
    print(f"[{index}]: {value}", end ="  ")