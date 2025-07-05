# 20. String Position Distribution
# 方法 1：defaultdict
from collections import defaultdict

string = 'Here are UPPERCASE and lowercase chars.'
result = defaultdict(list)  # 處理「Key 不存在」的情況：如果 key 還沒出現，自動把其 value 初始化成一個空的 list

for idx, char in enumerate(string, start=1):  # 列出字元及其對應位置（從 1 開始）
    result[char].append(idx)  # 可以直接用 append，不需檢查 key 是否存在

# 將 defaultdict 轉換成一般字典並印出
print(dict(result))  # {'H': [1], 'e': [2, 4, 8, 27, 32], 'r': [3, 7, 28, 37], ' ': [5, 9, 19, 23, 33], 'a': [6, 20, 30, 36], 'U': [10], 'P': [11, 12], 'E': [13, 18], 'R': [14], 'C': [15], 'A': [16], 'S': [17], 'n': [21], 'd': [22], 'l': [24], 'o': [25], 'w': [26], 'c': [29, 34], 's': [31, 38], 'h': [35], '.': [39]}

# 轉換前
print(result)  # defaultdict(<class 'list'>, {'H': [1], 'e': [2, 4, 8, 27, 32], 'r': [3, 7, 28, 37], ' ': [5, 9, 19, 23, 33], 'a': [6, 20, 30, 36], 'U': [10], 'P': [11, 12], 'E': [13, 18], 'R': [14], 'C': [15], 'A': [16], 'S': [17], 'n': [21], 'd': [22], 'l': [24], 'o': [25], 'w': [26], 'c': [29, 34], 's': [31, 38], 'h': [35], '.': [39]})

# 如果想照字典順序排序
print(dict(sorted(result.items())))  # {' ': [5, 9, 19, 23, 33], '.': [39], 'A': [16], 'C': [15], 'E': [13, 18], 'H': [1], 'P': [11, 12], 'R': [14], 'S': [17], 'U': [10], 'a': [6, 20, 30, 36], 'c': [29, 34], 'd': [22], 'e': [2, 4, 8, 27, 32], 'h': [35], 'l': [24], 'n': [21], 'o': [25], 'r': [3, 7, 28, 37], 's': [31, 38], 'w': [26]}

# 方法 2：dict.setdefault(key, default)
string = 'Here are UPPERCASE and lowercase chars.'
result = {}

for idx, char in enumerate(string, start=1): 
    result.setdefault(char, []).append(idx) 
    # 如果 key 存在字典中，回傳對應的值
    # 如果 key 不存在，將 default 當作初始值插入，然後回傳該值：{char, []} 

print(dict(result))

# 方法 2 的另一種寫法
# string = 'Here are UPPERCASE and lowercase chars.'
# result = {}
#
# for idx, char in enumerate(string, start=1): 
#     result.setdefault(char, [])
#     result[char].append(idx) 
#
# print(dict(result))

# 方法 3：collections.defaultdict
import collections as cc  # 匯入 Python 的標準模組 collections，並將其簡稱為 cc，讓你在後續使用模組中的功能時不需要打全名，例如 collections.defaultdict 就可以寫成 cc.defaultdict

string = 'Here are UPPERCASE and lowercase chars.'
result = cc.defaultdict(list)

for idx, char in enumerate(string, start=1): 
    result[char].append(idx)

print(dict(result))

# 方法 4：自己建立空 list 再加值
string = 'Here are UPPERCASE and lowercase chars.'
result = {}  # 使用一般 dict

for idx, char in enumerate(string, start=1):
    if char not in result:
        result[char] = []  # 如果這個 key 還沒出現，就初始化為空 list
    result[char].append(idx)  # 然後再把位置加進去

print(result)

# 方法 4 的另一種寫法
# string = 'Here are UPPERCASE and lowercase chars.'
#
# dic = {}
# count = 1
#
# for s in string:
#     if s not in dic:
#         dic[s] = []
#     dic[s].append(count)
#     count += 1
#
# print(dic)

def count_words(articles):
    word_count = defaultdict(int)
    for article in articles:
        words = jieba.lcut(article['content'])
        for word in words:
            word_count[word] += 1
    return word_count

def main(): 
    word_count = count_words(articles)

    freq_dict = defaultdict(list)
    for word, count in word_count.items():
        freq_dict[count].append(word)

    for count in sorted(freq_dict, reverse=True):
        print(f"{count}: {freq_dict[count]}")