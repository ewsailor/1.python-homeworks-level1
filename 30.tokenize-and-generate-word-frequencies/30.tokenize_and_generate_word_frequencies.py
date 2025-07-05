# 30. Tokenize And Generate Word Frequencies
# ===== 標準函式庫 =====
import re  # 處理正則表達式
from urllib.parse import urljoin  # 安全拼接網址用
from collections import defaultdict  # 自動初始化字典值 

# ===== 第三方套件 =====
import requests  # 發送 HTTP 請求 
from bs4 import BeautifulSoup  # 解析 HTML 原始碼，方便抓取指定元素
import jieba  # 斷詞工具

# jieba.load_userdict("dict.txt.big")  # 初始化設定：載入自訂字典，讓 jieba 支援自訂詞彙，讓斷詞更精準

MAX_NEWS = 2  # 可調整要抓幾則新聞

def get_article_content(url):
    """
    取得新聞內容。
    """
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

def count_words(articles):
    """
    計算每個詞彙出現的次數，回傳 {詞彙: 出現次數} 的字典。
    """
    word_count = defaultdict(int)
    for article in articles:
        words = jieba.lcut(article['content'])
        # print(f"article: {article}")
        # print(f"article['content']: {article['content']}")
        # print(f"words: {words}")
        for word in words:
            word_count[word] += 1
    return word_count

def group_words_by_frequency(word_count):
    """
    將詞頻字典依照出現次數分組，回傳 {出現次數: [詞彙, ...]} 的字典。
    """
    freq_dict = defaultdict(list)
    for word, count in word_count.items():
        freq_dict[count].append(word)
    return freq_dict

def main():
    """
    主程式。
    """
    base_url = 'https://udn.com'  # 未來想改主站網址（例如換成 https://news.udn.com），只需改 base_url，不需要改程式碼裡每個用到完整網址的地方
    list_path = '/news/breaknews/1'  # 列表頁的路徑
    list_url = urljoin(base_url, list_path) 

    response = requests.get(list_url)
    soup = BeautifulSoup(response.text, 'html.parser')  # 用 BeautifulSoup 讓 HTML 轉為可以用 Python 操作的資料結構，以能用 .find()、.find_all() 等方法

    # 資料蒐集：蒐集新聞內容
    articles = [] 
    for link in soup.find_all('h3', class_='rounded-thumb__title')[:MAX_NEWS]:
        if not link.a:  # 如果沒有 <a> 標籤，代表這則新聞缺少超連結，無法進一步抓取詳細內容
            continue  # 因此用 continue 跳過這一筆，繼續下一筆資料的處理
        news_url = urljoin(base_url, link.a['href'])  # 取得「每則新聞內容」的完整網址
        news_content = get_article_content(news_url)
        articles.append({'content': news_content})

    # 資料處理：詞頻統計
    word_count = count_words(articles)
    freq_dict = group_words_by_frequency(word_count)

    # 資料輸出：輸出詞頻統計結果
    for count in sorted(freq_dict, reverse=True):
        print(f"{count}: {freq_dict[count]}")

if __name__ == "__main__":
    main()