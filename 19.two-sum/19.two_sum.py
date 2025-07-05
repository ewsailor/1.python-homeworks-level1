# 19. Two Sum
# 方法 1：Hash Map 
nums = [3,2,4]
target = 6

def two_sum(nums, target):
    num_to_index = {} 
    for i, num in enumerate(nums):
        complement = target - num 
        if complement in num_to_index:
            return [num_to_index[complement], i]  # 如果差值已經存在於 num_to_index 中，返回差值的 index 和當前的 index
        num_to_index[num] = i
    return []  # 如果找不到符合條件的組合，返回空列表
d = two_sum(nums, target)
print(d)  # [1,2]  

# 方法 2：j 從 i+1 開始，避免重複檢查同一組合（如 [1, 2] 和 [2, 1]）
nums = [3,2,4]
target = 6

l = [[i,j] for i in range(len(nums)) for j in range(i+1, len(nums)) if nums[i]+nums[j] == target]
print(l[0])  # 找出所有組合，然後取第一個
 
# 上述推導式的展開 
# nums = [3,2,4]
# target = 6
#
# for i in range(len(nums)): 
#     for j in range(i+1, len(nums)): 
#         if nums[i] + nums[j] == target: 
#             print([i, j])
#             break

# 方法 3：會重複檢查同一組合
nums = [3,2,4]
target = 6

l = [[i,j] for i in range(len(nums)) for j in range(len(nums)) if nums[i]+nums[j] == target and i != j]
print(l[0])  # [1, 2]

# 上述推導式的展開 
# nums = [3,2,4]
# target = 6
#
# def find_pair():
#     for i in range(len(nums)): 
#         for j in range(len(nums)):
#             if target - nums[i] == nums[i]:
#                 continue
#             if nums[i] + nums[j] == target: 
#                 return [i, j]  # 找到答案就直接返回
#
# print(find_pair())

# 方法 4：in
nums = [3,2,4]
target = 6

for i in range(len(nums)):
    if target - nums[i] == nums[i]:  # 如果 target - nums[i] 等於 nums[i]，則跳過，因為不能用同樣的元素 2 次，即使用 2 次 3
        continue
    if target - nums[i] in nums:
        print([i, nums.index(target - nums[i])])  # [1,2]  
        break  # 如果不加上 break，會印出所有符合條件的索引，即 [1,2] 和 [2,1]

# 方法 5：標誌變數（為了跳出多層迴圈，但在 Python 中，直接用 return 會更簡潔）
nums = [3,2,4]
target = 6
found = False  # 新增標誌變數

for i in range(len(nums)): 
    if found:  # 如果已經找到答案，跳出外層迴圈
        break
    for j in range(len(nums)):
        if target - nums[i] == nums[i]:
            continue
        if nums[i] + nums[j] == target: 
            print([i, j])  # [1,2]  
            found = True  # 設置標誌
            break