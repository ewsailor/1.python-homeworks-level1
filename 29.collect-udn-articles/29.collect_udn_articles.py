# 29. Collect Udn Articles
# ===== 標準函式庫 =====
import re  # 處理正則表達式
from urllib.parse import urljoin  # 安全拼接網址用

# ===== 第三方套件 =====
import requests  # 發送 HTTP 請求 
from bs4 import BeautifulSoup  # 解析 HTML 原始碼，方便抓取指定元素

MAX_NEWS = 2  # 可調整要抓幾則新聞

def get_article_content(url):
    try:
        res = requests.get(url, timeout=10)  # 避免網路卡住程式無限等待
        res.raise_for_status()  # 檢查 HTTP 回應是否成功（非 200 會拋錯）
        soup = BeautifulSoup(res.text, 'html.parser')
        paragraphs = soup.find_all('div', class_='article-content__paragraph')  # 尋找所有內文段落
        print(f"DEBUG: {url} 抓到 {len(paragraphs)} 個段落")  # 用來除錯，確認有抓到段落
        
        cleaned_lines = []
        for p in paragraphs:
            text = re.sub(r'[\s\u3000]', '', p.text.strip())  # 去除空白
            if text:  # 非空字串才保留
                cleaned_lines.append(text)
                
        raw_content = '\n'.join(cleaned_lines)  # 合併段落，並用換行符號分隔
        formatted_content = re.sub(r'([。！？])', r'\1\n', raw_content)  # 句號、問號、驚嘆號後換行，並用 \1\n 留下「原本的標點符號」，再「換行」
        return formatted_content
    except requests.RequestException as e:  # 只捕捉 requests 相關例外，其他錯誤讓它拋出（方便 debug）
        print(f"Error fetching article: {url}, reason: {e}")
        return ""

def main():
    base_url = 'https://udn.com'  # 未來想改主站網址（例如換成 https://news.udn.com），只需改 base_url，不需要改程式碼裡每個用到完整網址的地方
    list_path = '/news/breaknews/1'  # 列表頁的路徑
    list_url = urljoin(base_url, list_path) 

    response = requests.get(list_url)
    soup = BeautifulSoup(response.text, 'html.parser')  # 用 BeautifulSoup 讓 HTML 轉為可以用 Python 操作的資料結構，以能用 .find()、.find_all() 等方法

    news_data = [] 
    for link in soup.find_all('h3', class_='rounded-thumb__title')[:MAX_NEWS]:
        if not link.a:  # 如果沒有 <a> 標籤，代表這則新聞缺少超連結，無法進一步抓取詳細內容
            continue  # 因此用 continue 跳過這一筆，繼續下一筆資料的處理
        news_title = link.a.text.strip()  
        news_url = urljoin(base_url, link.a['href'])  # 取得「每則新聞內容」的完整網址
        news_content = get_article_content(news_url)
        news_data.append({
            'title': news_title, 
            'url': news_url, 
            'content': news_content
        })

    for news in news_data:
        print(f"標題：{news['title']}\n網址：{news['url']}\n內容：\n{news['content']}\n{'='*80}")

if __name__ == "__main__":
    main()

# 印出結果
# DEBUG: https://udn.com/news/story/124499/8775913?from=udn-catehotnews_ch2 抓到 1 個段落
# DEBUG: https://udn.com/news/story/7268/8775968?from=udn-catehotnews_ch2 抓到 1 個段落
# 標題：三峽重大車禍余姓老翁今晨不治 死亡人數再添1人肇事原因成謎
# 網址：https://udn.com/news/story/124499/8775913?from=udn-catehotnews_ch2
# 內容：
# 新北市三峽重大車禍，涉嫌肇事的余姓男子仍在醫院加護病房治療中，肇事的78歲余姓老翁被送往亞東醫院搶救，歷經2次手術與12天治療後，今天早上7時20分因傷勢嚴重，不幸離世，整體事故死者再添1人。
# 新北市三峽區北大國小外道路19日下午4時許發生重大車禍；余姓男子（78歲）涉駕車闖紅燈高速衝撞，造成3死、12輕重傷（含駕駛），死傷者大多數為學生。
# 編輯推薦三峽肇事駕駛若死亡不代表沒責任！
# 蘇家宏律師：遺產還是能賠償余姓老翁事發後傷重，在亞東醫院加護病房搶救多天，也曾經歷2次手術，但生命徵象不是很穩定，一度有微微張眼，檢察官、警察也正要 等他意識清楚要製作筆錄，今早卻傳出人已身故的消息。
# 老翁的2個兒子在事發後已從國外趕回台灣協助處理。
# 近日新北市三峽發生重大車禍，造成3死12傷。
# 聯合報系資料照車禍三峽
# ================================================================================
# 標題：快去取「午時水」！命理師曝：端午5大轉運妙招
# 網址：https://udn.com/news/story/7268/8775968?from=udn-catehotnews_ch2
# 內容：
# 端午節民間習俗取「午時水」，台中市名門命理教育協會創會理事長楊登嵙分享，端午節午時是一年中陽氣最旺，更是招好運、去霉運的最佳時刻，他還分享端午五大轉運妙招。
# 楊登嵙說，「端午節」是全年陽氣最盛之日，午時為上午11時到下午1時，在湧泉、瀑布、井裡或家裡水龍頭所取的水為「午時水」，又稱「純陽水」，若能在這時間將 此水置於陽光下曝曬至少30分鐘，吸收陽光的正陽能量更好，效果更佳。
# 楊登嵙說明，午時水除了可用於日常灑淨、沐浴、泡澡，甚至可加上硃砂用於書符，效果更加乘。
# 也可以在端午節中午使用午時水沾濕榕樹或艾草葉，由房屋內部向外灑淨，也有助提升整體宅運。
# 透天厝則建議由頂樓往下至門口依序進行，象徵將霉氣逐層排出。
# 楊登嵙也分享端午五大轉運妙招：1.發財水：午時將168元或268元硬幣加午時水與少量鹽煮沸，冷卻後置於大門斜對角財位，有助財氣聚集。
# 2.文昌筆催文昌：2025年文昌星位於九宮格西方，可在此放置四支毛筆並以紅線串起，吊掛於書桌或辦公室，幫助考運與決策力。
# 3.立雞蛋求好運：午時將雞蛋豎立於財位，據信可帶來整年好運。
# 住家或辦公室財位在大門斜對角角落，若不知道財位，也可選在客廳或辦公桌正中間，開店者可選在櫃檯中間立蛋。
# 4.粽子旺文昌：粽中加紅棗成棗粽，諧音「早中」，寓意早日高中金榜。
# 5.招桃花與貴人：正午時於臥室噴灑花香香水或於神明廳點檀香，有助提升人緣與招引貴人。
# 楊登嵙強調，透過端午節當日打掃家裡、開窗通風，讓陽光灑入，霉氣退散，轉換氣場、提振精神；財位布局、文昌擺設、香氣招緣，到立蛋見運的互動儀式，端午節也可成為家庭與職場共同參與的儀式日。
# ☛此為民俗說法，不代表本新聞網立場，切勿過度迷信。
# 命理師楊登嵙說明，端午可取「午時水」招財開運。
# 圖／楊登嵙提供雞蛋端午節
# ================================================================================