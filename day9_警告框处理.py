# 警告框处理
# 在webdriver中处理JavaScript生成的alert,confirm和prompt十分简单
# 具体的做法是，首先使用switch_to_alert()方法定位，然后使用text,accpet,dismiss,send_keys等进行操作。


from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 打开搜索设置
link = driver.find_element_by_link_text("设置").click()
driver.find_element_by_link_text("搜索设置").click()

sleep(2)

#保存设置
driver.find_element_by_class_name("prefpanelgo").click()

# 获取警告框
alert = driver.switch_to.alert

# 获取警告框的信息
alert_text = alert.text
print(alert_text)

# 接受警告框
alert.accept()

driver.quit()
