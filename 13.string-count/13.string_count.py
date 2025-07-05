# 13. String Count
from collections import Counter

str = input("請輸入字串：")  # 使用者輸入 Hello World

counter = Counter(str)  # 直接把字串丟進 Counter，會自動統計每個字元出現次數
result = dict(counter)  # 將 Counter 轉為普通字典
print(result)  # {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'W': 1, 'r': 1, 'd': 1}