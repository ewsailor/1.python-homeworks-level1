# 09. Remove Duplicates And Sort
# 方法 1
L = [1, 1, 3, 9, 7, 8, 8, 8]
L = list(set(L)) 
L.sort(reverse=True) 
print(L)  # [9, 8, 7, 3, 1]

# 方法 2
L = [1, 1, 3, 9, 7, 8, 8, 8]
L_sorted = sorted(set(L), reverse=True)
print(L_sorted)  # [9, 8, 7, 3, 1]

# 方法 3
from collections import Counter

L = [1, 1, 3, 9, 7, 8, 8, 8]
counter = Counter(L)
L = sorted(counter.keys(), reverse=True)
print(L)  # [9, 8, 7, 3, 1]

