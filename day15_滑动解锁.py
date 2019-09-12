from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.helloweba.com/demo/2017/unlock")

# 定位滑动块
slider = driver.find_elements_by_class_name("slide-to-unlock-handle")[0]
action = ActionChains(driver)
action.click_and_hold(slider).perform()

for index in range(200):
	try:
		# 鼠标移动，偏移(x,y)
		action.move_by_offset(2,0).perform()
	except UnexpectedAlertPresentException:
		break
	#重置action 
	action.reset_actions()
	sleep(0.1)

# 打印警告提示
success_text  = driver.switch_to.alert.text 
print(success_text)