from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("隐秘的角落")
driver.find_element_by_id("su").click()
time.sleep(6)
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("蛋黄的长裙")
#driver.find_element_by_id("su").click()
# click可以用submit来替代
driver.find_element_by_id("su").submit()

time.sleep(6)
driver.quit()