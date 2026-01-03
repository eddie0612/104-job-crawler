# 104 Job Crawler (職缺自動化爬蟲)

## 📖 專案說明
這是一個基於 **Python** 與 **Selenium WebDriver** 開發的自動化爬蟲工具。
主要功能為針對 104 人力銀行進行職缺關鍵字搜尋，自動遍歷多個分頁，擷取職缺關鍵資訊並結構化存入 **SQLite** 資料庫。

本專案實作了針對動態網頁 (SPA) 的處理機制，並包含基礎的反爬蟲防禦策略，解決了網頁自動化中常見的動態載入與遮擋問題。

## 🛠️ 技術堆疊
* **語言**: Python 3.x
* **核心庫**: Selenium WebDriver
* **資料庫**: SQLite 3
* **選擇器策略**: CSS Selectors (Advanced), XPath
* **版本控制**: Git

## ✨ 核心功能

### 1. 動態分頁處理 (Dynamic Pagination Handling)
* 針對 RWD 響應式網頁結構，捨棄傳統的文字定位 (Link Text)，改用 **CSS Selector (`li:last-child`)** 精準定位動態變化的「下一頁」按鈕。
* 整合 **JavaScript Executor** 進行事件觸發，解決按鈕可能被廣告視窗或 Cookie 同意條款遮擋的問題 (`ElementClickInterceptedException`)。

### 2. 防禦性程式設計 (Defensive Programming)
* **隨機延遲 (Random Delay)**：在請求之間加入隨機時間間隔，模擬人類操作行為。
* **異常處理 (Exception Handling)**：實作 `try-except` 機制處理網頁載入超時或元素定位失敗，確保爬蟲程序穩定運行。

### 3. 資料持久化與完整性 (Data Persistence)
* **自動初始化**：程式啟動時自動檢測並建立 SQLite 資料庫結構 (`init_db`)。
* **資料去重**：利用 SQL 的 `UNIQUE(job_title, company)` 複合鍵約束與 `INSERT OR IGNORE` 語法，防止重複資料寫入。
* **屬性提取**：區分 `innerText` 與 `title` 屬性，確保擷取到被截斷的完整公司名稱與職缺標題。

## 🚀 安裝與執行

### 1. 環境設定
確認已安裝 Python 3.x 與 Google Chrome 瀏覽器。
安裝專案依賴套件：
```bash
pip install -r requirements.txt
```

### 2. 執行爬蟲
直接執行主程式：
```bash
python crawler.py
```
程式將自動執行以下流程：
1. 初始化 `job_hunter.db` 資料庫。
2. 開啟 Chrome 瀏覽器並導向 104 搜尋頁面。
3. 依序爬取指定頁數 (預設為前 15 頁) 的職缺資訊。
4. 將資料寫入資料庫。

### 3. 資料查看
爬取完成後，資料將儲存於 `job_hunter.db` 檔案中。
可使用任何支援 SQLite 的工具 (如 **DB Browser for SQLite** 或 VS Code 擴充套件) 進行查詢。

## 📂 專案結構
```text
.
├── crawler.py          # 爬蟲主程式 (包含資料庫初始化與邏輯控制)
├── requirements.txt    # 專案依賴清單
├── README.md           # 專案說明文件
└── .gitignore          # Git 忽略設定
```

## ⚠️ 免責聲明
本專案僅供學術研究與技術練習使用，請勿用於任何商業用途或惡意攻擊網站。使用時請遵守目標網站的 `robots.txt` 規範與相關服務條款。
