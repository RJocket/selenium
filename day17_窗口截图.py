# 建议png格式
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 截取当前窗口，指定保存位置
driver.get_screenshot_as_file("D:\\py_workspace\\test.png")
sleep(2)
driver.quit()
