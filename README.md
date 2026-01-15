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
* **單元測試整合**：使用 **Pytest** 撰寫測試腳本 (`test_104_search.py`)，驗證網頁標題、搜尋功能與資料載入狀態。
* **持續整合 (CI)**：透過 `.github/workflows/main.yml` 設定 GitHub Actions，在每次 Push 代碼時自動啟動 Linux 雲端環境。
* **無頭模式 (Headless Mode)**：實作 Chrome Headless 模式，使測試能在無介面的伺服器環境中穩定運行。

### 2. 動態爬蟲技術 (Web Scraping)
* **RWD 頁面處理**：利用 CSS Advanced Selector (`li:last-child`) 與 JS Executor 解決動態分頁按鈕被遮擋的問題。
* **防禦性程式設計**：加入隨機延遲 (Random Delay) 與異常處理 (Try-Except)，提升爬蟲的抗干擾能力與穩定性。

### 3. 資料持久化 (Data Persistence)
* **SQLite 整合**：自動初始化資料庫結構，並使用 `UNIQUE` 複合鍵防止職缺資料重複寫入。

## 🚀 安裝與執行

### 1. 環境安裝
```bash
pip install -r requirements.txt
```

### 2. 執行自動化測試 (Run Tests)
執行 Pytest 進行網頁功能驗證：
```bash
pytest
```
*若看到綠色 Passed 字樣，代表 104 網站功能正常且腳本執行無誤。*

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
