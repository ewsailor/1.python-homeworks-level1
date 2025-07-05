# 08. Merge Sets
# 方法 1：update
d1 = {1:10, 2:20}
d2 = {3:30, 4:40}
d3 = {5:50, 6:60}

d = {}
for dic in [d1, d2, d3]:
    d.update(dic)
print(d)  # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} 

# 方法 2：dict unpacking（解包）（Python 3.5+）
d1 = {1:10, 2:20}
d2 = {3:30, 4:40}
d3 = {5:50, 6:60}

d = {**d1, **d2, **d3}
print(d)  # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# 方法 3：| 運算子（Python 3.9+）
d1 = {1:10, 2:20}
d2 = {3:30, 4:40}
d3 = {5:50, 6:60}

d = d1 | d2 | d3
print(d)  # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# 方法 4：使用 ChainMap（來自 collections 模組）
from collections import ChainMap

d1 = {1:10, 2:20}
d2 = {3:30, 4:40}
d3 = {5:50, 6:60}

d = dict(ChainMap(d3, d2, d1))  # 順序為右邊優先：後面的會覆蓋前面的 key
print(d)  # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# 方法 5：先透過 list(dic.items()) 將字典轉成由 (key, value) 組成的列表
# 再透過 + 符號將三個列表連接起來
# 最後再透過 dict() 將列表轉回字典
d1 = {1:10, 2:20}
d2 = {3:30, 4:40}
d3 = {5:50, 6:60}

d = dict(list(d1.items()) + list(d2.items()) + list(d3.items()))

# 輸出合併後的字典
print(d)  # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# print(d1.items())  # dict_items([(1, 10), (2, 20)])
# print(list(d1.items()))  # [(1, 10), (2, 20)]