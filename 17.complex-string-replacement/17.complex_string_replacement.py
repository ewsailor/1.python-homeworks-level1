# 17. Complex String Replacement
import re

def replace_not_at_all(text):
    """
    將句子中所有「not ... at all」模式（可跨行、大小寫無關），換成「good」。
    僅處理完整單字的 not / at all，避免誤判 knot, notebook 等字詞。
    """
    pattern = r"\bnot\b.*?\bat all\b"
    # .*? 是「非貪婪匹配」，找到第一個符合條件的部分就停止，避免過度比對
    # \b 表示單字邊界（word boundary），確保要比對的是「完整單字」，不是像 notebook、knot 這種包含 not 的「子字串」
    return re.sub(pattern, "good", text, flags=re.DOTALL | re.IGNORECASE)
    # flags=re.DOTALL 模式：允許跨行比對
    # flags=re.IGNORECASE 模式：忽略大小寫

def test_replace_not_at_all():
    """測試 replace_not_at_all 函式。"""
    examples = [
    "I'm good at math.", 
    "This company is not poor at all.",
    "I'm not at all happy about it.",
    "It's not smart at all, not helpful at all, and not funny at all! I'm not at all happy about it.", 
    "It's not not at all at all.", 
    "notebook and knot are tricky but not easy at all.", 
    "This is not\nso bad at all.", 
    "This company is nOt poor at All." 
    ]

    for i, s in enumerate(examples, 1):
        print(f"#{i}：{replace_not_at_all(s)}")

if __name__ == "__main__":
    test_replace_not_at_all()