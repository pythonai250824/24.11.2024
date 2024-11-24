
# mutable
# [1, 3, 4]
# dict = { 'danny': 1, 1: 'one' ... }
# immutable
# tuple = (1, 3, {1: 9}) --

def func1(d1) -> None:
    d1.update({'new': 1})

d2 = {}
func1(d2)
# d2 == {'new': 1}

# a
tuple1 = (99,)
# b
tuple2 = (77, 88, 99)
# c
def get_up_len(tup) -> int:
    return len(tup)
# d
def comb_tup(tup1, tup2) -> int:
    result = tup1 + tup2
    tup1 = tup1 + tup2
    return result
# e
def common_tup(tup1, tup2) -> tuple:
    result: list = []
    # better to run on the shorter tuple
    for item in tup1:
        if item in tup2:
            result.append(item)
    return tuple(result)
print(common_tup((1, 2, 3, 4), (3, 4, 5, 6)))
# word = ""
# for i in  range(1000):
#     word += str(i)
# 1234567891011
# f
def uncommon_tup(tup1, tup2) -> tuple:
    # (1, 2)
    # (2, 3, 4, 5, 6)
    # 1
    result: list = []
    common = common_tup(tup1, tup2)
    for item in tup1:
        if not item in common:
            result.append(item)
    for item in tup2:
        if not item in common:
            result.append(item)
    return tuple(result)
    # 2
    result2: list = []
    common = common_tup(tup1, tup2)
    for item in tup1 + tup2:
        if not item in common:
            result2.append(item)
    return tuple(result2)
    # 3
    return tuple(item for item in tup1+tup2 \
                 if item not in common_tup(tup1, tup2))
    # 4
    return tuple(item for item in tup1+tup2\
                 if item not in tup1 and item not in tup2)

print(uncommon_tup((1, 2, 3), (2, 3, 5, 7)))

#h
def reverse_tup(tup1) -> tuple:
    return tup1[::-1]

print(reverse_tup((1, 2, 3)))

def no_dupl(tup1) -> tuple:
    # 1
    result = []
    for item in tup1:
        if not item in result:
            result.append(item)
    return tuple(result)
    # 2
    no_dup = dict()
    for item in tup1:
        no_dup[item] = 'stam'  # 2 1 2 1 2 1
        # chocolate cake cake
        # { 'chocolate': 1, 'cake': 2 }
        # {2: 'stam', 1: 'stam'}
    return tuple(no_dup.keys())

print(no_dupl((1, 1, 3, 3, 1, 2, 0)))

# write in function
names = []
grades = []
name: str = input('name? ["done" to finish]')
while not name == "done":
    names.append(name)
    name = input('name? ["done" to finish]')
grade: int = int(input('grade? ["-999" to finish]'))
while not grade == -999:
    grades.append(grade)
    grade = int(input('grade? ["-999" to finish]'))
print(tuple(zip(names, grades)))
# 1 2 3 4
# a b c d e f g
#(1, a), (2, b), (3, c), (4, d)

def index_by_value(tup1, value) -> tuple:
    result = []
    for index in range(len(tup1)):
        if tup1[index] == value:
            result.append(index)
    return tuple(result)

print(index_by_value((10, 8, 5, 5, 3, 2, 5, 10, 30, 40), 5))

