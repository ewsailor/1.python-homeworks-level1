# 23. Climbing Stairs
# 方法 1：
import math
import ast  # Abstract Syntax Tree（抽象語法樹）模組

def safe_eval(user_input):
    """
    安全解析型別：不執行代碼，只允許 Python literal，如 str、int、float、list、tuple、dict、set。
    """
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
    """
    回傳 user_input 代表的「資料型別名稱」字串。
    特別處理空字串的情況。
    """
    if user_input.strip() == "":
        return "空字串或僅含空白"  # 如果輸入是空白或空字串，直接回傳此字串說明，以免使用者輸入空白，程式回傳「型別是字串」，讓使用者困惑
    return safe_eval(user_input)  # 否則，呼叫 safe_eval 函式回傳該輸入的型別名稱

def get_positive_integer():
    """
    確保輸入正整數：持續要求使用者輸入，直到獲得一個「大於 0」的正整數。
    """
    while True:
        user_input = input("請輸入一個「大於 0」的正整數：")
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

def climbing_stairs_combinations(n):
    """
    計算爬樓梯組合數：每次可爬 1 或 2 階，輸入 n 階，回傳所有組合數。
    """
    d = [[x, y] for x in range(n+1) for y in range(n+1) if x + 2*y == n]
    total = sum([math.factorial(x + y) // (math.factorial(x) * math.factorial(y)) for x, y in d])
    return total

def main():
    """
    主程式。
    """
    print("此程式會要求您輸入一個大於 0 的正整數 n，然後計算爬樓梯有幾種可能的走法")
    n = get_positive_integer()
    total = climbing_stairs_combinations(n)
    print(f"{n} 階樓梯有 {total} 種可能的走法")

if __name__ == "__main__":
    main()

# 測試輸入與預期輸出（覆蓋各種非正整數的情況）：
# 說明：輸入為大於 0 的正整數，計算爬樓梯有幾種可能的走法
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
# 說明：輸入為大於 0 的正整數，計算爬樓梯有幾種可能的走法
# 輸入：3
# ➤ 輸出：3 階樓梯有 3 種可能的走法 

# 方法 2：費氏數列
import math
import ast  # Abstract Syntax Tree（抽象語法樹）模組

def safe_eval(user_input):
    """
    安全解析型別：不執行代碼，只允許 Python literal，如 str, int, float, list, tuple, dict, set。
    """
    try:
        node = ast.literal_eval(user_input)
        return type(node).__name__  # 若 user_input 可被安全轉成 Python literal，就傳回其型別名稱，如 int, list, tuple, dict, set
    except:  # 如果輸入不是 literal，即 str, float，會再嘗試轉成 float，否則最後就判定為 "字串"
        try:
            float(user_input)  # 應對某些 ast.literal_eval 不支援的合法數字格式（如 1_000.5），或作為安全保底處理
            return "浮點數"
        except:
            return "字串"

def identify_type(user_input):
    """
    回傳 user_input 代表的「資料型別名稱」字串。
    特別處理空字串的情況。
    """
    if user_input.strip() == "":
        return "空字串或僅含空白"  # 如果輸入是空白或空字串，直接回傳此字串說明，以免使用者輸入空白，程式回傳「型別是字串」，讓使用者困惑
    return safe_eval(user_input)  # 否則，呼叫 safe_eval 函式回傳該輸入的型別名稱

def get_positive_integer():
    """
    持續要求使用者輸入，直到獲得一個「大於 0」的正整數。
    """
    while True:
        user_input = input("請輸入一個「大於 0」的正整數：")
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

def climbing_stairs_combinations(n):
    """
    計算爬樓梯組合數：每次可爬 1 或 2 階，輸入 n 階，回傳所有組合數。
    「爬第 n 階樓梯的方法數」 = 「爬 n−1 階樓梯的方法數」 + 「爬 n−2 階樓梯的方法數」。
    費氏數列：
        f(0) = 0
        f(1) = 1
        f(n) = f(n-1) + f(n-2)    
    """
    steps = [0] * (n + 1)  # 建立一個長度為 n+1 的 list steps，記錄走到每一階的方法數
    steps[0] = 1  # 走到第 0 階（起點）只有 1 種方法，就是什麼都不做
    steps[1] = 1  # 走到第 1 階只有 1 種方法，就是爬 1 階
    for i in range(2, n + 1):  
        steps[i] = steps[i-1] + steps[i-2]  
    return steps[n] 

def main():
    print("此程式會要求您輸入一個大於 0 的正整數 n，然後計算爬樓梯有幾種可能的走法")
    n = get_positive_integer()
    total = climbing_stairs_combinations(n)
    print(f"{n} 階樓梯有 {total} 種可能的走法")

if __name__ == "__main__":
    main()