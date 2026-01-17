import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # --- 設定瀏覽器選項 ---
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # 初始化 Driver
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_104_title(driver):
    """測試案例 1: 檢查連線是否正常 (標題檢查)"""
    driver.get("https://www.104.com.tw/jobs/main/")
    assert "104" in driver.title, "標題應該包含 '104'"

def test_search_results(driver):
    """測試案例 2: 模擬搜尋並驗證結果"""
    # 直接前往搜尋結果頁面 (搜尋: 軟體測試)
    driver.get("https://www.104.com.tw/jobs/search/?keyword=軟體測試")
    
    # 等待職缺列表載入 (最多等 10 秒)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".info-container"))
    )
    
    # 抓取所有職缺卡片
    job_cards = driver.find_elements(By.CSS_SELECTOR, ".info-container")
    # 驗證 (Assertion)
    print(f"找到 {len(job_cards)} 筆職缺")
    assert len(job_cards) > 0, "錯誤：搜尋結果為空，找不到任何職缺！"
    
    for card in job_cards[:3]:
        title_elm = card.find_element(By.CSS_SELECTOR,"a[data-gtm-joblist*='職缺名稱']")
        title = title_elm.get_attribute("title")
        company_elm = card.find_element(By.CSS_SELECTOR,"a[data-gtm-joblist*='公司名稱']")
        company = company_elm.get_attribute("title")
        
        assert len(title) > 0, "職缺標題不該是空白的"
        assert len(company) > 0, "公司名稱不該是空白的"
        
def test_pagination(driver):
    """測試案例 3:翻頁功能測試"""
    driver.get("https://www.104.com.tw/jobs/search/?keyword=軟體測試")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".info-container"))
    )
    #紀錄現在網址
    old_url = driver.current_url
    next_btn = driver.find_element(By.CSS_SELECTOR,"li.paging__item:last-child a")
    driver.execute_script("arguments[0].click();",next_btn)
    WebDriverWait(driver, 10).until(EC.url_changes(old_url))
    #記錄新網址
    new_url = driver.current_url
    assert old_url != new_url,"翻頁失敗"