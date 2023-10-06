lst = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
index = 0
while index < len(lst):
    cnt = lst.count(lst[index])
    if cnt > 1:
        lst[index] = str(lst[index]) * cnt
    index += 1
print(set(lst))