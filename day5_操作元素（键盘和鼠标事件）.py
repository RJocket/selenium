from selenium import webdriver

driver = webdriver.Firefox()
driver.get("Http://www.baidu.com")

# 获得输入框的尺寸大小
size = driver.find_element_by_id("kw").size
print(size)

# 底部备案信息
text = driver.find_element_by_id("cp").text
print(text)

# 元素属性值
attribute = driver.find_element_by_id("kw").get_attribute('type')
attribute = driver.find_element_by_id("kw").get_attribute('name')
print (attribute)

# 判断元素是否可见
result = driver.find_element_by_id("kw").is_displayed()

driver.quit()

# 1.鼠标操作
# 在webdriver中所有与鼠标操作的方法都封装在 ActionChains 中
from selenium.webdriver import ActionChains
# from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.baidu.cn")

above = driver.find_element_by_link_text("设置")
# 鼠标悬停
ActionChains(driver).move_to_element(above).perform()
driver.quit

# move_to_element():鼠标悬停
# perform:执行ActionChains类中存储的行为
# double_click():双击 ； context_click():右击 ； drag_and_drop():拖动

# 2.键盘操作
# 使用Keys模块
from selenium.webdriver.common.keys import keys

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"a")


