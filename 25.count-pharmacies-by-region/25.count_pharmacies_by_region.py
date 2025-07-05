# 25. Count Pharmacies By Region
# 方法 1：defaultdict
# ===== 標準函式庫 =====
import json  # 處理 JSON 格式資料
from collections import defaultdict  # 自動初始化字典值

# ===== 第三方套件 =====
import requests  # 發送 HTTP 請求

# 完整藥局資料來源網址
url = 'https://raw.githubusercontent.com/kiang/pharmacies/master/json/points.json'
# 測試用小型資料集網址（可切換使用）
# url = 'https://gist.githubusercontent.com/ewsailor/732cc7c987eee17e0325be3715df937e/raw/54f2050dd1a8a9f2702141f29a4f31f291a9d5c5/points_small.json'
response = requests.get(url)  # 發送 GET 請求來獲取資料
response_text = response.text  # .text：取得 HTTP 回應內容的純文字（字串）版本，人類看得懂，但程式不能理解結構
pharmacies_data = json.loads(response_text)  # 將 json 格式的字串轉成 Python 物件，如轉成字典或列表

# 計算各地區的藥局數量
med_count = defaultdict(int)  # 建立一個「當 key 不存在時，預設值是 0」的字典
for pharmacy in pharmacies_data['features']:
    region = pharmacy['properties']['county']
    med_count[region] += 1

print(dict(med_count))  # {'臺北市': 339, '': 49, '高雄市': 422, '臺中市': 420, '臺南市': 271, '基隆市': 57, '新竹市': 39, '嘉義市': 67, '新北市': 501, '桃園市': 264, '新竹縣': 46, '宜蘭縣': 76, '苗栗縣': 56, '彰化縣': 179, '南投縣': 67, '雲林縣': 129, '嘉義縣': 84, '屏東縣': 140, '澎湖縣': 11, '花蓮縣': 46, '臺東縣': 23, '金門縣': 6, '連江縣': 1}

# 方法 2
# ===== 標準函式庫 =====
import json  # 處理 JSON 格式資料

# ===== 第三方套件 =====
import requests  # 發送 HTTP 請求

# 完整藥局資料來源網址
url = 'https://raw.githubusercontent.com/kiang/pharmacies/master/json/points.json'
# 測試用小型資料集網址（可切換使用）
# url = 'https://gist.githubusercontent.com/ewsailor/732cc7c987eee17e0325be3715df937e/raw/54f2050dd1a8a9f2702141f29a4f31f291a9d5c5/points_small.json'

response = requests.get(url)  # 發送 GET 請求來獲取資料
response_text = response.text  # .text：取得 HTTP 回應內容的純文字（字串）版本，人類看得懂，但程式不能理解結構
pharmacies_data = json.loads(response_text)  # 將 json 格式的字串轉成 Python 物件，如轉成字典或列表

# 計算各地區的藥局數量
med_count = {}
for pharmacy in pharmacies_data['features']:
    region = pharmacy['properties']['county']
    if region not in med_count:
        med_count[region] = 0
    med_count[region] += 1

print(med_count)  # {'臺北市': 339, '': 49, '高雄市': 422, '臺中市': 420, '臺南市': 271, '基隆市': 57, '新竹市': 39, '嘉義市': 67, '新北市': 501, '桃園市': 264, '新竹縣': 46, '宜蘭縣': 76, '苗栗縣': 56, '彰化縣': 179, '南投縣': 67, '雲林縣': 129, '嘉義縣': 84, '屏東縣': 140, '澎湖縣': 11, '花蓮縣': 46, '臺東縣': 23, '金門縣': 6, '連江縣': 1}