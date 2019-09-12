# webdriver无法直接定位frame/iframe表单内嵌页面上的元素。只能通过switch_to.frame()切换
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.126.com")

sleep(2)

login_frame = driver.find_element_by_css_selector('ifrmae[id^="x-URS-iframe"]')
driver.switch_to.frame(login_frame)
driver.find_element_by_name("email").send_keys("username")
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_id("dologin").click()
# 回到最外层的页面
driver.switch_to.default_content()

driver.quit()

