# 11. Split Even Odd
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 用 list comprehension 分別收集奇數與偶數
odds = [x for x in L if x % 2 == 1]
evens = [x for x in L if x % 2 == 0]

# 合併：先奇後偶
L = odds + evens

print(L)  # [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]