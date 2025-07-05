# 28. Save Mask Stock To Db
# ===== 標準函式庫 =====
import json  # 處理 JSON 格式資料
import sqlite3  # 操作 SQLite 資料庫
from datetime import datetime  # 取得當前時間
from collections import defaultdict  # 自動初始化字典值 

# ===== 第三方套件 =====
import requests  # 發送 HTTP 請求

def main():
    # 1. 取得藥局 JSON 資料
    # 完整藥局資料來源網址
    url = 'https://raw.githubusercontent.com/kiang/pharmacies/master/json/points.json'
    # 測試用小型資料集網址（可切換使用）
    # url = 'https://gist.githubusercontent.com/ewsailor/732cc7c987eee17e0325be3715df937e/raw/54f2050dd1a8a9f2702141f29a4f31f291a9d5c5/points_small.json'
    response = requests.get(url)  # 發送 GET 請求來獲取資料
    pharmacies_data = json.loads(response.text)  # 將 json 格式的字串轉成 Python 物件，如轉成字典或列表

    # 2. 建立資料庫與資料表
    conn = sqlite3.connect('masks.db')  # 連線 SQLite 資料庫
    c = conn.cursor()  # 從資料庫連線中建立「游標物件」，即資料庫操作工具，可執行 SQL 指令與讀取結果
    c.execute(''' 
        CREATE TABLE IF NOT EXISTS masks (
            city TEXT,
            counts INTEGER,
            createdAt DATETIME
        )
    ''')
    c.execute('DELETE FROM masks')
    conn.commit()

    # 3. 計算每個地區的剩餘口罩數量
    mask_count = defaultdict(int)  # 建立一個「當 key 不存在時，預設值是 0」的字典
    for pharmacy in pharmacies_data['features']:
        region = pharmacy['properties']['county']    
        mask_adult = pharmacy['properties']['mask_adult']
        mask_child = pharmacy['properties']['mask_child']
        mask_count[region] += mask_adult + mask_child

    # 4. 取出每一筆資料，並寫入資料庫
    now = datetime.now()
    for city, count in mask_count.items():
        print(f"INSERT INTO masks VALUES ('{city}', {count}, '{now}')")  # 每次寫入時都會印出 SQL 指令（方便除錯）
        c.execute("INSERT INTO masks VALUES (?, ?, ?)", (city, count, now))  # 使用問號來表示要插入的值，避免 SQL 注入攻擊
    conn.commit()

    # 5. 查詢並印出資料
    c.execute("SELECT * FROM masks")
    results = c.fetchall()
    for row in results:  # 不直接 print(c.fetchall()) 是因為，會印出一個「list of tuple」，格式較難閱讀
        print(row)
    
    # 6. 關閉連線
    #  # 儲存所有變更並關閉資料庫連線
    conn.commit()
    conn.close() 

if __name__ == "__main__":
    main()