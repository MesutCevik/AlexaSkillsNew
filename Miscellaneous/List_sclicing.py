# list4sclicing = [7, '*', 9, '+', '(', 10, '*', 17, ')', '-', 42]
#
# if '(' and ')' in list4sclicing:
#     p1 = list4sclicing[list4sclicing.index('(') + 1: list4sclicing.index(')')]
#     print(p1)
#
# p2= list4sclicing[2:9]
#
# print(list4sclicing)
# print(p2)


list4del = [7, '*', 9, '+', '(', 10, '*', 17, ')', '-', 42]
bracket_open = None
bracket_close = None

if '(' and ')' in list4del:
    bracket_open = list4del.index('(')
    print(f"Index of bracket open: {bracket_open}.")
    bracket_close = list4del.index(')')
    print(f"Index of bracket close: {bracket_close}.")
    print()

else:
    print("I can´t calculate this!")

del list4del[bracket_open: bracket_close + 1]
print(list4del)
print()
result = 10 * 17

list4del.insert(bracket_open, result)
print(f"Das Ergebnis muss sein: 170. Errechnet wurde: {result}. "
      f"Hier die überarbeitete Mathe-Aufgabe: {list4del}")

listB = ["T", "X", "J", 9, ")", "X"]
index_of_X = listB.index('X', 2)

print(f"Index of X is: {index_of_X}")
