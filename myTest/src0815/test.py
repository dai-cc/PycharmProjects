import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

# 用id定位
# driver.find_element_by_id("kw").send_keys("白夜追凶")
# driver.find_element_by_id("su").click()
# time.sleep(6)

# 用name定位
# 百度一下的按钮没有name属性，所以不能用name定位
# 在保证name唯一的时候才可以用name定位哦
# driver.find_element_by_name("wd").send_keys("白夜追凶")
# driver.find_element_by_id("su").click()
# time.sleep(6)

# 用class也不一定能够定位成功,比如说这里
# 这里搜索框的class_name有两个类
# driver.find_element_by_class_name("s_ipt nobg_s_fm_hover").send_keys("白夜追凶")

# 通过链接打开，link_text
# driver.find_element_by_link_text("hao123").click()
# time.sleep(6)

# driver.find_element_by_link_text("新闻").click()
# time.sleep(6)

# 通过部分链接打开，比如说这里打开新闻
# driver.find_element_by_partial_link_text("新").click()
# time.sleep(6)

# 通过标签定位
# driver.find_element_by_tag_name("input").click()

# 万能的方法，可以定位所有的东西
# driver.find_element_by_xpath("//*[@id='kw']").send_keys("白夜追踪")
# driver.find_element_by_xpath("//*[@name='wd']").send_keys("白夜追踪")
# driver.find_element_by_xpath("//*[@id='su']").click()

driver.find_element_by_css_selector("#kw").send_keys("白夜追踪")
driver.find_element_by_css_selector("#su").click()
time.sleep(6)
driver.quit()