# 18. Self Dividing Number
import ast  # Abstract Syntax Tree（抽象語法樹）模組

def safe_eval(user_input):
    """安全解析 user_input 為 Python 型別：不執行代碼，只允許 Python literal，如 str、int、float、list、tuple、dict、set。"""
    try:
        node = ast.literal_eval(user_input)
        return type(node).__name__  # 若 user_input 可被安全轉成 Python literal，就傳回其型別名稱，如 int、list、tuple、dict、set
    except:  # 如果輸入不是 literal，即 str、float，會再嘗試轉成 float，否則最後就判定為 "字串"
        try:
            float(user_input)  # 應對某些 ast.literal_eval 不支援的合法數字格式（如 1_000.5），或作為安全保底處理
            return "浮點數"
        except:
            return "字串"

def identify_type(user_input):
    """型別辨識函式：回傳 user_input 代表的「資料型別名稱」字串，特別處理空字串的情況。"""
    if user_input.strip() == "":
        return "空字串或僅含空白"  # 如果輸入是空白或空字串，直接回傳此字串說明，以免使用者輸入空白，程式回傳「型別是字串」，讓使用者困惑
    return safe_eval(user_input)  # 否則，呼叫 safe_eval 函式回傳該輸入的型別名稱

def get_positive_integer(prompt):
    """確保輸入正整數：持續要求使用者輸入，直到獲得一個「大於 0」的正整數。"""
    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            if value > 0:
                return value
            else:
                print(f"⚠️\t您輸入的整數 {value}「小於等於 0」，請輸入一個「大於 0」的正整數")
        except ValueError:
            type_name = identify_type(user_input)
            display = user_input or '空白/空字串'
            print(f"❌\t您輸入的 {display} 為「{type_name}」，非正整數，請輸入一個「大於 0」的正整數")

def is_self_dividing(num):
    """回傳 True 表示 num 是自除數，False 表示不是自除數。"""
    digits = [int(i) for i in str(num)]
    if 0 in digits:
        return False
    for digit in digits:
        if num % digit != 0:
            return False
    return True

def get_self_dividing_numbers(a, b):
    """回傳區間 [a, b] 內所有自除數的列表。"""
    return [i for i in range(a, b+1) if is_self_dividing(i)]

def max_gap_pair(nums):
    """回傳差距最大的相鄰自除數對 (小, 大)，若不足兩個則回傳 None。"""
    if len(nums) < 2:
        return None
    max_diff = -1  # 初始化最大差值為 -1（任何實際差值都會比它大）
    result_pair = None  # 初始化結果對為 None
    for i in range(len(nums)-1):
        diff = nums[i+1] - nums[i]  # 計算相鄰自除數的差值
        if diff > max_diff:  # 如果差值大於目前最大差值，則更新最大差值和結果對
            max_diff = diff
            result_pair = (nums[i], nums[i+1])
    return result_pair

def main():
    """主程式。"""
    print("此程式會要求您輸入兩個大於 0 的正整數，找出區間內所有自除數中差距最大的相鄰兩個自除數")
    a = get_positive_integer("請輸入區間的第一個正整數：")
    b = get_positive_integer("請輸入區間的第二個正整數：")
    if a > b:
        a, b = b, a
    nums = get_self_dividing_numbers(a, b)
    print(f"區間 [{a}, {b}] 內的自除數有：{nums}")
    pair = max_gap_pair(nums)
    if pair:
        print(f"差距最大的相鄰自除數為：{pair}")
    else:
        print("區間內沒有足夠的自除數可計算差距")

if __name__ == "__main__":
    main() 

# 測試輸入與預期輸出（覆蓋各種非正整數的情況）：
# 說明：輸入兩個大於 0 的正整數，找出區間內所有自除數中，差距最大的相鄰兩個自除數
#
# 一、字串
# 輸入：a
# ➤ 輸出：❌      您輸入的 a 為「字串」，非正整數，請輸入一個「大於 0」的正整數
#
# 二、負整數
# 輸入：-3
# ➤ 輸出：⚠️      您輸入的整數 -3「小於等於 0」，請輸入一個「大於 0」的正整數
#
# 三、零
# 輸入：0
# ➤ 輸出：⚠️      您輸入的整數 0「小於等於 0」，請輸入一個「大於 0」的正整數
#
# 四、浮點數
# 輸入：正浮點數 3.3、負浮點數 -2.5
# ➤ 輸出：❌      您輸入的 3.3 為「float」，非正整數，請輸入一個「大於 0」的正整數
# ➤ 輸出：❌      您輸入的 -2.5 為「float」，非正整數，請輸入一個「大於 0」的正整數
#
# 五、空字串 / 空白
# 輸入：（直接按 Enter）、（空白字元）
# ➤ 輸出：❌      您輸入的 空白/空字串 為「空字串或僅含空白」，非正整數，請輸入一個「大於 0」的正整數
#
# 六、容器
# 輸入：List [1,2]、Tuple (5,)、Dictionary {2:3}、Set {2, 3, 7}
# ➤ 輸出：❌      您輸入的 [1,2] 為「list」，非正整數，請輸入一個「大於 0」的正整數
# ➤ 輸出：❌      您輸入的 (5,) 為「tuple」，非正整數，請輸入一個「大於 0」的正整數
# ➤ 輸出：❌      您輸入的 {2:3} 為「dict」，非正整數，請輸入一個「大於 0」的正整數
# ➤ 輸出：❌      您輸入的 {2, 3, 7} 為「set」，非正整數，請輸入一個「大於 0」的正整數
#
# 七、合法正整數
# 說明：輸入兩個大於 0 的正整數，找出區間內所有自除數中，差距最大的相鄰兩個自除數
# 輸入：20 10
# ➤ 輸出：區間 [10, 20] 內的自除數有：[11, 12, 15]
# ➤ 輸出：差距最大的相鄰自除數為：(12, 15)
# 輸入：10 20
# ➤ 輸出：區間 [10, 20] 內的自除數有：[11, 12, 15]
# ➤ 輸出：差距最大的相鄰自除數為：(10, 11)