# webdriver中操作Cookie的方法
# get_cookies():操作所有Cookie
# get_cookie(name):返回字典中key为"name"的Cookie
# add_cookie(cookie_dict):添加Cookie
# delete_cookie(name,optionsString):删除名为OpenString 的Cookie
# delete_all_cookies():删除所有Cookie

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#获得所有Cookie信息并打印
cookie = driver.get_cookies()
print(cookie)

# 添加cookie信息
driver.add_cookie({'name':'key-aaaa','value':'value-bbbbb'})

# 遍历指定的cookie
for cookie in driver.get_cookies():
	print("%s -> %s"%(cookie['name'],cookie['value']))