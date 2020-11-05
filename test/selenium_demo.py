from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome(executable_path="C:\\Users\\Renu\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("http://127.0.0.1:8000/calci")
driver.maximize_window()
driver.find_element_by_id("n1").send_keys("1")
driver.find_element_by_id("n2").send_keys("2")
select=Select(driver.find_element_by_id("op"))
time.sleep(1)
select.select_by_value('add')
time.sleep(2)
driver.find_element_by_id("b1").click()
time.sleep(5)
print(driver.title)
driver.quit()


