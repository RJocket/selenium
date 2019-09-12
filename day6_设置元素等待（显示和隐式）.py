# 显示等待
#webdriver等待某个条件成立则继续执行，否则在达到最长时长时抛出超时异常
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebdriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 判断元素是否存在 超时时间5s,轮询时间0.5s 
# WebdriverWait常与until，until_not连用

element = WebdriverWait(driver,5,0.5).until(
	EC.visibility_of_element_located((By.ID,"kw")))

element.send_keys('selenium')
driver.quit()


# 隐式等待
# 隐式等待设置时间并非固定等待时间，不影响脚本执行速度。它会等待页面上的所有元素，如果元素存在则继续；否则轮询判断，超时则抛出异常。
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Firefox()

# 设置隐式等待时间
driver.implicity_wait(10)
driver.get("http://www.baidu.com")

try:
	print(time.ctime())
	driver.find_element_by_id("kw22").send_keys("selenium")

except NoSuchElementException as e:
	print(e)
finally:
	print(time.ctime())
	driver.quit()