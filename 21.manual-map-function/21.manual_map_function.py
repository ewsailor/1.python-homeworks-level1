# 21. Manual Map Function
def add1(n):
    return n + 1

def isPrime(n):
    if n <= 1:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5)+1))

# isPrime(n) 的另一種寫法
# def isPrime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True 

def f(L, F): 
    return [F(i) for i in L]

# 使用自定義函式
L = [1,2,3,4,5,6]
F = add1
print(f(L, F))  # [2,3,4,5,6,7]

L = [2,3,4,5,6,7]
F = isPrime
print(f(L, F))  # [True, True, False, True, False, True]

# 用 map() 函式：返回迭代器（iterator），所以要用 list() 轉換為列表
# L = [1,2,3,4,5,6]
#
# def add1(n):
#     return n + 1
#
# print(list(map(add1, L)))  # [2,3,4,5,6,7]
#
#  # 使用 lambda 函式搭配 map
# L = [1,2,3,4,5,6]
# print(list(map(lambda x: x + 1, L)))  # [2,3,4,5,6,7]
#
# L = [2,3,4,5,6,7]
# print(list(map(isPrime, L)))  # [True, True, False, True, False, True]