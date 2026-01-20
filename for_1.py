from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)
driver.get("https://www.naver.com")
time.sleep(2)
search_box = driver.find_element(By.CSS_SELECTOR, "input#query")
search_box.click()
time.sleep(0.5)
keyword = "인공지능"
for char in keyword:
    search_box.send_keys(char)
    time.sleep(0.25)
search_box.send_keys(Keys.ENTER)
time.sleep(2)
news_tab = driver.find_element(By.LINK_TEXT, "뉴스")
news_tab.click()
time.sleep(3)
print("뉴스 검색 페이지 도착")
news_list = driver.find_elements(By.CSS_SELECTOR, "a")
count = 0
for a in news_list:
    title = a.text.strip()
    href = a.get_attribute("href")
    if (
        title
        and href
        and href.startswith("https://")
        and ("view" in href or "article" in href)
    ):
        count += 1
        print(f"{count}. {title}")
        print(f"    {href})")
print("총 뉴스 개수:", count)
# driver.quit()
