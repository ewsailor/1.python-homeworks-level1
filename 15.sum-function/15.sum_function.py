# 15. Sum Function
# 方法 1
def f(*args):
    return sum(args)

print(f(1, 2, 3))  # 6
print(f(1, 2, 3, 4, 5))  # 15

# 方法 2
def f(*args):
    total = 0
    for number in args: 
        total += number 
    return total
print(f(1, 2, 3))  # 6
print(f(1, 2, 3, 4, 5))  # 15