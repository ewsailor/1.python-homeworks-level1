# 22. Unique Permutations
# 方法 1
string = input("請輸入字串：")  # abc
unique_chars = list(set([string[i] for i in range(len(string))]))  # 用 Set 去掉重複的字母，並轉換成 list，不過因為有用 set() 所以是無序的

from itertools import permutations  # 匯入 itertools 模組，這個模組提供了很多處理迴圈和排列組合的工具

dic = [''.join(i) for i in permutations(unique_chars)]  # 產生所有排列結果（permutations） 的 tuple，然後把 tuple 的字元連起來變成字串

print(dic)  # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

# 方法 1 的另一種寫法
# string = input("請輸入字串：")  # abc
# dic = list(set([string[i] for i in range(len(string))])) 
#
# import itertools 
#
# def F(chars):  # 定義一個函式 F，參數是 chars（一個字元 list）
#     perms = list(itertools.permutations(chars)) 
#     # 用 itertools.permutations 函式，產生 chars 所有可能的排列（permutations），每一個排列都是一個 tuple，最後將結果轉換成 list
#     # 例如 chars = ['A', 'B', 'C']，排列會有 ('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C') 等等
#     return [''.join(p) for p in perms]  # 將每一個 tuple 轉換成字串，並返回一個包含所有排列的字串 list
#
# print(F(dic))  # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

# 方法 2：產生所有可能的排列（permutations），包含重複字元的情況。例如輸入 "AAB"，會產生 "AAB", "ABA", "BAA" 等
# 如果輸入的字串有重複字元，排列結果中也會有重複的排列（因為每個字元位置都被視為不同）
string = input("請輸入字串：")  # abc
dic = []

def permute(s, i, length):  # i：目前要交換的起始位置，length：字串的長度
    if i == length:  # 如果 i 等於字串的長度，表示已經處理完所有字元，將目前的排列加入結果列表
        dic.append(''.join(s))  # 將目前的排列轉換成字串，並加入結果列表
    else:  # 如果 i 不等於 length，表示還有元素需要交換
        for j in range(i, length):  # 從 i 到 length-1 之間的每個位置：目前要交換的元素位置
            s[i], s[j] = s[j], s[i]  # 交換元素位置
            permute(s, i+1, length)  # 遞迴處理下一個位置  遞迴調用 permute 函式，將 i 加 1，繼續交換下一個元素
            s[i], s[j] = s[j], s[i]  # 交換元素位置

permute(list(string), 0, len(string))  # 將字串轉換成 list 並傳入遞迴函式 
print(dic)  # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
