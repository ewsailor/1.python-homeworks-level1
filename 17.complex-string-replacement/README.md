# 17. Complex String Replacement

## 目標 Goals
- 將字串當中的「not ... at all」換成「good」，中間的「...」代表任意字串或沒有內容 

## 要求 Requirements
- 使用者輸入 #01：This company is not poor at all.
- 印出 #01：This company is good.
- 使用者輸入 #02：I'm not at all happy about it.
- 印出 #02：I'm good happy about it.

## 測試案例 Test Cases
| Test # | 描述 Description                                 | 輸入 Input                                          | 預期輸出 Expected Output            |
| ------ | ------------------------------------------- | ---------------------------------------------- | -------------------------- |
| 1      | 沒有 not ... at all，印出原字串                       | `I'm good at math.`                            | `I'm good at math.`        |
| 2      | `not`、`at all` 之間，有字串 | `This company is not poor at all.`             | `This company is good.`    |
| 3      | `not`、`at all` 之間，沒有字串           | `I'm not at all happy about it.`               | `I'm good happy about it.` |
| 4      | 多組 not ... at all       | `It's not smart at all, not helpful at all, and not funny at all! I'm not at all happy about it.` | `It's good, good, and good! I'm good happy about it.`       |
| 5      | 多重 not 與 at all（測試最小取代範圍）                      | `It's not not at all at all.`                  | `It's good at all.`        |
| 6      | 測試單字邊界：確保比對的是「完整單字」，不是像 `notebook`、`knot` 這種包含 not 的「子字串」     | `notebook and knot are tricky but not easy at all.`                         | `notebook and knot are tricky but good.`     |
| 7      | 測試跨行匹配                             | `This is not\nso bad at all.`                  | `This is good.`            |
| 8      | 測試大小寫無關                            | `This company is nOt poor at All.`                               | `This company is good.`                     |

## 備註
- 本練習為「Python 資料科學教戰營第 1 階段」課程作業之一，點此[連結](https://github.com/ewsailor/1.python-homeworks-level1/blob/main/README.md)可看所有作業