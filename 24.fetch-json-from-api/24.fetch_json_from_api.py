# 24. Fetch Json From Api
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

# 格式化輸出
# json.dumps()：將 Python 資料格式，轉成 JSON 格式的字串
# indent=2：每層縮排 2 個空格，增加可讀性
# ensure_ascii=False：確保非 ASCII 字元（例如中文）不會被轉成 Unicode 編碼（例如「臺北市」會正確顯示，而不是 Unicode 編碼）
print(json.dumps(pharmacies_data, indent=2, ensure_ascii=False))