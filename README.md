# 104 Job Crawler & Automation Testing

![CI Status](https://github.com/eddie0612/104-job-crawler/actions/workflows/main.yml/badge.svg)

## 📖 專案說明
這是一個結合 **Python Selenium** 與 **Pytest** 的自動化測試與爬蟲專案。
主要功能除了針對 104 人力銀行進行職缺爬取與資料分析外，更整合了 **GitHub Actions** 實現 CI/CD 持續整合流程，確保每次程式碼更新時，都能自動執行 UI 測試腳本以驗證系統穩定性。

本專案展示了從「資料爬取」、「資料庫設計」到「自動化測試部署」的完整開發流程。

## 🛠️ 技術堆疊 (Tech Stack)
* **語言**: Python 3.x
* **自動化框架**: Selenium WebDriver
* **測試框架**: Pytest
* **CI/CD**: GitHub Actions
* **資料庫**: SQLite 3
* **版本控制**: Git

## ✨ 核心功能

### 1. 自動化測試與 CI/CD (Automated Testing)
* **功能邏輯驗證**：撰寫測試腳本驗證 **搜尋結果**、**資料完整性** (確保標題與公司名稱非空值)，以及最關鍵的 **翻頁功能 (Pagination)** 邏輯。
* **智慧等待機制 (Explicit Wait)**：捨棄 `time.sleep`，全面採用 `WebDriverWait` 搭配 `EC.url_changes` 與 `presence_of_element`，確保測試在動態網頁載入時的穩定性。
* **持續整合 (CI)**：透過 GitHub Actions 設定，在每次 Push 代碼時自動啟動 Linux 雲端環境與無頭模式 (Headless Mode) 執行測試。

### 2. 動態爬蟲技術 (Web Scraping)
* **穩定元素定位**：優先使用 `data-gtm` 等數據追蹤屬性進行定位，降低因網頁改版導致爬蟲失效的風險。
* **JS 交互處理**：利用 JavaScript Executor (`execute_script`) 解決動態分頁按鈕被廣告或浮動視窗遮擋的問題。
* **防禦性程式設計**：加入異常處理 (Try-Except) 與隨機延遲，提升爬蟲的抗干擾能力。

### 3. 資料持久化 (Data Persistence)
* **SQLite 整合**：自動初始化資料庫結構，並使用 `UNIQUE` 複合鍵防止職缺資料重複寫入。

## 🚀 安裝與執行

### 1. 環境安裝
```bash
pip install -r requirements.txt

### 2. 執行自動化測試 (Run Tests)
執行 Pytest 進行網頁功能驗證：
```bash
pytest
```
*若看到綠色 Passed 字樣，代表 104 網站功能正常且腳本執行無誤。*

### 2. 執行自動化測試(Run Tests)
執行 Pytest 進行網頁功能驗證：
```bash
pytest
```

### 3. 執行爬蟲 (Run Crawler)
啟動主程式進行資料爬取：
```bash
python crawler.py
```

## 📂 專案結構
```text
.
├── .github/workflows/  # GitHub Actions CI 設定檔
├── crawler.py          # 爬蟲主程式 (資料爬取)
├── test_104_search.py  # Pytest 測試腳本 (功能驗證)
├── job_hunter.db       # SQLite 資料庫 (自動生成)
├── requirements.txt    # 套件依賴清單
└── README.md           # 專案說明文件
```
