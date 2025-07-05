# 26. Sort Mask Stock By Region 
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

# 計算每個地區的剩餘成人口罩數量
mask_adult_count = defaultdict(int)  # 建立一個「當 key 不存在時，預設值是 0」的字典
for pharmacy in pharmacies_data['features']:
    region = pharmacy['properties']['county']    
    mask_adult = pharmacy['properties']['mask_adult']
    mask_adult_count[region] += mask_adult

# 將結果從大到小排列
mask_adult_count = dict(sorted(mask_adult_count.items(), key=lambda item: item[1], reverse=True)) 

print(dict(mask_adult_count))  # {'新北市': 670270, '臺中市': 536710, '高雄市': 424170, '臺南市': 393900, '桃園市': 331940, '臺北市': 322490, '彰化縣': 219400, '雲林縣': 196990, '屏東縣': 184250, '苗栗縣': 131080, '嘉義縣': 113180, '嘉義市': 107840, '宜蘭縣': 106900, '南投縣': 91240, '基隆市': 80100, '': 69210, '花蓮縣': 57330, '新竹縣': 51350, '新竹市': 45630, '臺東縣': 28510, '金門縣': 15510, '澎湖縣': 12600, '連江縣': 7930}