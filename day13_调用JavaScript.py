# 有些页面操作不能靠webdriver API实现，如：滚动条拖动。可借助JavaScript脚本。
# 用于调整浏览器滚动条的JavaScript
# <!--window.scrollTo(左边距，上边距)；-->

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.set_window_size(800,600)

driver.find_element_by_id("kw").send_keys("selenium")

js = "window.scrollTo(100,450)"
driver.execute_script(js)

sleep(2)

driver.quit()

# JavaScript可以在textarea文本框中输入内容，因为不能通过sendkeys()输入文本信息
# text = "input text"
# js = "document.getElementById('id').value='"+text+"';"
# driver.execute_script(js)