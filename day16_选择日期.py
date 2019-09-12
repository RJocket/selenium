# 参考前面的操作，通过ActionChains类可以实现上下滑动选择日期。这里换用TouchActions类实现。

from time import sleep
from selenium import webdriver

opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c',  False)
driver = webdriver.Chrome(chrome_options=opt)

driver.get("http://www.jq22.com/yanshi4976")
sleep(2)
driver.switch_to.frame("iframe")
driver.find_element_by_id("appDate").click()

# 定位到要滑动的年月日
dwwos = driver.find_elements_by_class_name("dwwo")
year = dwwos[0]
month = dwwos[1]
day = dwwos[2]

action = webdriver.TouchActions(driver)
# scroll_from_element(on_element,xoffset,yoffset)
action.scroll_from_element(year,0,5).perform()
action.scroll_from_element(month,0,30).perform()
action.scroll_from_element(day,0,30).perform()