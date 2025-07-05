# 05. Split Url
url = "https://www.facebook.com/dscareer"
parts = url.split("/")  # 以 '/' 分割字串
result = parts[2]  # 取出第三個元素，即 'www.facebook.com'
print(result)  # 輸出 'www.facebook.com' 