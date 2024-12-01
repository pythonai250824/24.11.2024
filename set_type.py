# list [1, 2, 3]
# dict { key: value }
# tuple (1, 2, {'Israel'...})
# highest_prices = [...] will change
# highest_prices = (...) will NOT change
# set - no duplications

s1: set = {1, 2, 3}
print(s1)
print(len(s1))
s2 = s1
s2.clear()
print(s1)

# lst1 = []
# x = int(input())
# while x != -999:
#     if not x in lst1:
#         lst1.append(x)
#     x = int(input())

print({2, 1, 2, 1, 2, 1, 2, 1, 2})
lst2 = [2, 1, 2, 2, 1, 2, 1, 2, 1, 2]
print(set(lst2))

# set2 = set()
# x = int(input())
# while x != -999:
#     set2.add(x)
#     x = int(input())

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.intersection(set2))  # 3
print(set1 & set2)  # 3
lesson1 = {"danny", "shoshi", "shimon"}
lesson2 = {"danny", "sofi", "ronny"}
print(lesson1 & lesson2)  # who participated in both lessons?

set3 = {1, 2, 30}
t = {40, 5, 6, 8, 9}
result1 = set3.isdisjoint(t)  # is nothing in common?
print(result1)
lesson1 = {"danny", "shoshi", "shimon"}
lesson2 = {"dan", "sofi", "ronny"}
print(lesson1.isdisjoint(lesson2))  # were all the students in lesson2 new?

# no_common = True
# for name in lesson1:
#     if name in lesson2:
#         no_common = False
#         break

topics_ta = {
    "Fractions and Percentages", "Ratios and Proportions",
    "Basic Algebra", "Geometry", "Data Handling", "Probability Basics",
    "Cells and Systems", "Force and Motion"}
topics_herz = {
    "Fractions and Percentages", "Ratios and Proportions",
    "Basic Algebra", "Geometry", "Data Handling",
    "Probability Basics", "Cells and Systems", "Force and Motion",
    "Weather and Climate", "Atoms and Molecules", "Grammar and Writing"}
print(topics_ta.issubset(topics_herz))  # are all topics in ta taught in herz? yes
print(topics_herz.issubset(topics_ta))  # are all topics in herz taught in ta? no
print(topics_ta <= topics_herz)  # are all topics in ta taught in herz? yes
print({1, 3} < {1, 3})  # without =, equal is not included

study1 = {"Math", "English", "Python"}
univ = {"Math", "Python" }
print(study1.issuperset(univ))  # i study everything taught in the univ or more
print(study1 >= univ)  # i study everything taught in the univ
print({1, 2} > {1, 2})  # without =, equal is not included

set8 = {1, 2, 3, 40}
print(40 in set8)
set8.remove(40)
print(set8)
print(set8.pop())  # remove a random item
print(set8)

run_mar_elat = {"yossi", "shimon", "diana"}
run_mar_bee7 = {"yossi", "batel", "miri"}
print(run_mar_elat.difference(run_mar_bee7))  # who run only in elat?
print(run_mar_bee7.difference(run_mar_elat))  # who run only in beer7?
print(run_mar_elat - run_mar_bee7)
print(run_mar_bee7 - run_mar_elat)
print(run_mar_bee7 & run_mar_elat)
print(set(sorted(run_mar_elat)))

run_mar_elat = {"yossi", "shimon", "diana"}
run_mar_bee7 = {"yossi", "batel", "miri"}
print(run_mar_elat.symmetric_difference(run_mar_bee7))  # who run only in elat?
#                                                         or only in beer7
print(run_mar_elat ^ run_mar_bee7)   # who run only in elat?
#                                      or only in beer7

#print({1, 2} + {3, 4})  # error
#print(set(list({1, 2, 3, 4}) + list({3, 4, 3, 4, 5})))  # add
run_mar_elat = {"yossi", "shimon", "diana"}
run_mar_bee7 = {"yossi", "batel", "miri"}
run_mar_elat.update(run_mar_bee7)  # {a + b} changes the original
# oneline:
# print(run_mar_elat.update(run_mar_bee7) or run_mar_elat) # {a + b}

# run_mar_elat.add(run_mar_bee7)  # error
print(run_mar_elat)

run_mar_elat = {"yossi", "shimon", "diana"}
run_mar_bee7 = {"yossi", "batel", "miri"}
print(run_mar_elat.union(run_mar_bee7))  # {a + b}
print(run_mar_elat | run_mar_bee7)  # does not change the original

#print((run_mar_elat | run_mar_bee7) - (run_mar_elat & run_mar_bee7))  # sym diff

#### frozen set
fs = frozenset([1, 2, 3])
#fs.pop()  # Error
#fs.remove()  # Error
