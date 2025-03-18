# APAFormatGen

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](#)
[![Python](https://img.shields.io/badge/Python-3.7+-brightgreen.svg)](#)

嗨～歡迎來到 **APAFormatGen**！  
你是否曾經因為寫報告、論文需要引用文獻，卻為了格式跑來跑去、摸不著頭緒呢？  
有了 **APAFormatGen**，只要簡單幾個步驟，就能自動幫你生成 APA 格式引文！  

## ✨ 專案簡介

這個專案主要提供了一個超簡單的 Python 腳本，透過使用者輸入文獻的相關資訊（例如作者、日期、標題等等），就能一鍵生成標準的 APA 格式引用文字。  
最棒的是，它還能判斷文獻是中文還是英文，並分別輸出適合的格式喔！

## ⚙️ 專案結構
```text
APAFormatGen/
├── README.md                # 你現在看到的說明文件！
├── Source.txt               # 放一些關於引用範例的來源資料
├── main.py                  # 主程式入口：在這裡跟使用者互動，取得輸入並輸出結果
└── citation/
    ├── __init__.py
    ├── citation_generator.py # 引文產生器：負責整合作者、標題、日期、網址...等資訊
    ├── formatting.py         # 文字格式化：依語言判斷如何輸出標題、作者、網站名稱等
    └── __pycache__/         
```

## 🚀 快速開始

1.	安裝 Python 建議先安裝 Python 3.7 以上版本，確保程式能夠在您的環境正常運行。
2.	複製或下載此專案
  •	直接從 GitHub 或其他來源取得專案檔案
  •	解壓縮或將專案放到你想放的資料夾
3.	進入專案資料夾，執行主程式

```bash
cd APAFormatGen
python main.py
```

執行後，螢幕會提示輸入作者、日期、標題、網站名稱與網址。通通填好之後，按下 Enter，就能獲得自動生成的 APA 格式引文啦！

## 🧩 功能介紹
•	自動判斷中文或英文文獻
只要輸入的標題有超過 70% 的字元是中文，程式就會把它認作中文文獻，並用中文的排版規則進行格式化；若不是，就用英文 APA 的格式顯示！
•	作者多人格式
•	中文：透過 、 分隔多位作者
•	英文：透過 , 和 & 分隔作者，並考量人數多寡自動加入省略號或符號
•	日期格式多樣化
能支援「YYYY-MM-DD、YYYY/MM/DD、YYYYMMDD」等多種輸入形式，並輸出成對應的格式。
•	愛怎麼改就怎麼改
整個程式碼都非常簡單易懂，如果有特殊需求想自訂輸出格式，只要到 citation/formatting.py 中動手腳就好囉！

## 🎯 使用範例

假設在執行程式時，我輸入了以下資訊：

```text
作者名稱：王大明、李小華
日期：2023-05-01
文章標題：Python自動化之美
網站名稱：Pythons World
網址：https://example.com
```

程式會自動產生類似這樣的 APA 引文格式：

```text
王大明、李小華（2023年05月01日）。**Python自動化之美**。PYTHONS WORLD。https://example.com
```

就這麼簡單輕鬆！

## 💡 建議＆回饋
•	如果在使用過程中有任何問題或建議，歡迎發 Issue 或送 PR！
•	如果覺得程式有幫上忙，歡迎在專案幫我們按個星星 ⭐️，讓更多人知道這個好東西。

## 🔐 授權方式

本專案採用 MIT License 進行授權。
換句話說，你可以非常自由地使用、修改與散播這個專案，不過請記得在程式碼中保留原作者資訊。

⸻

感謝使用 APAFormatGen，祝你在寫作與引用的世界裡一切順心順手～
如果覺得這個工具很讚，別忘了給個 Star 支持一下，讓更多人跟我們一起省力又省腦！
