import sqlite3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def init_db():
    conn = sqlite3.connect('job_hunter.db')
    cursor = conn.cursor()
    
    sql = """
    CREATE TABLE IF NOT EXISTS jobs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_title TEXT NOT NULL,
        company TEXT NOT NULL,
        salary TEXT,
        location TEXT,
        link TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(job_title,company)
    );
    """
    cursor.execute(sql)
    conn.commit()
    conn.close()
    
    
def save_to_db(data_list):
    conn = sqlite3.connect('job_hunter.db')
    cursor = conn.cursor()
    
    try:
        sql = "INSERT OR IGNORE INTO jobs (job_title,company,location,salary,link) VALUES(?,?,?,?,?)"
        cursor.executemany(sql,data_list)
        conn.commit()
        print(f"成功儲存{len(data_list)}筆資料")
    except Exception as e:
        print(f"資料庫錯誤:{e}")
        conn.rollback()
    finally:
        conn.close()
        
def start_crawler():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    
    try:
        print("開始爬蟲")
        driver.get("https://www.104.com.tw/jobs/search/?keyword=軟體測試&order=1&jobsource=2018indexpoc&ro=0")
        page = 1
        while(True):
            WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,".info-container"))
            )
            job_cards = driver.find_elements(By.CSS_SELECTOR,".info-container")
            print(f"找到{len(job_cards)}個職缺")
            
            crawled_data = []  # 用來暫存這一頁符合條件的資料
            for card in job_cards:
                try:
                    title_elm = card.find_element(By.CSS_SELECTOR,"a[data-gtm-joblist*='職缺名稱']")
                    title = title_elm.get_attribute("title")
                    
                    keywords = ["測試", "Test", "QA", "Quality", "驗證"]
                    if not any(keyword in title for keyword in keywords):
                        continue  # 如果標題不包含任何關鍵字，跳過這筆
                    
                    link = title_elm.get_attribute("href")
                    company_elm = card.find_element(By.CSS_SELECTOR,"a[data-gtm-joblist*='公司名稱']")
                    company = company_elm.get_attribute("title")
                    salary_elm = card.find_element(By.CSS_SELECTOR,"[data-gtm-joblist*='薪資']")
                    salary = salary_elm.text
                    location_elm = card.find_element(By.CSS_SELECTOR,"[data-gtm-joblist*='地區']")
                    location = location_elm.text
                    
                    print(f"抓到{title} {company}")
                    
                    crawled_data.append((title,company,location,salary,link))
                except:
                    continue
            if crawled_data:
                save_to_db(crawled_data)
            try:
                # 尋找「下一頁」按鈕
                next_btn = driver.find_element(By.CSS_SELECTOR,"li.paging__item:last-child a")
                driver.execute_script("arguments[0].click();",next_btn)
                page += 1
                # 設定安全機制：超過15頁就停止，避免無限迴圈
                if page > 15:
                    break
                print(f"前往第{page}頁~")
                
            except Exception as e:
                print("已抵達最後一頁")
                break
    finally:
        driver.quit()
if __name__ == "__main__":
    init_db()
    start_crawler()