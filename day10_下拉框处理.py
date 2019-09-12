# webdriver提供了Select类来处理下拉框
# Select类：用于定位<select>标签
# select_by_value() : 通过value值定位下拉选项
# select_by_visible_text(): 通过text值定位下拉选项
# select_by_index(): 根据下拉选项的索引值进行选择。从0开始。


from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select 
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

# 打开搜索设置
link = driver.find_element_by_link_text("设置")
# 鼠标悬停
ActionChains(driver).move_to_element(link).perform()

driver.find_element_by_xpath("/html/body/div[1]/div[6]/a[1]").click()

sleep(2)

# 搜索结果显示条数
sel = driver.find_element_by_xpath("//select[@id='nr']")

# value = "20"
Select(sel).select_by_value('20')
sleep(2)

# <option>每页显示50条</option>
Select(sel).select_by_visible_text("每页显示50条")
sleep(2)

# 根据索引进行选择
Select(sel).select_by_index(0)
sleep(2)

driver.quit()