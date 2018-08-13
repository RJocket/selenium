from selenium import webdriver
import time

# 配置文件地址
profile_directory = R'C:\Users\R\AppData\Roaming\Mozilla\Firefox\Profiles\yjdic0n5.default'
# 加载配置文件
profile =webdriver.FirefoxProfile(profile_directory)
# 启用配置文件 打开浏览器
driver =webdriver.Firefox(profile)

# 1.打开浏览器 webdriver.Ie()	webdriver.Chrome()
# driver =webdriver.Firefox()

# 2.打开网页
driver.get("https://www.baidu.com")

# 3.打开网页后，页面加载需时间，最好设置休眠
# 休眠3秒钟
time.sleep(3)
'''
# 4.有时页面未来得及同步数据，可模拟刷新操作
driver.refresh()

# 打开新网页
driver.get("https://www.cnblogs.com/zidonghua/p/7430083.html")
time.sleep(5)
# 5.返回上一页
driver.back()
time.sleep(3)
# 6.返回下一页
driver.forward()
'''
# 7.设置浏览器大小
driver.set_window_size(800,600)
time.sleep(2)

# 8.最大化窗口
driver.maximize_window()

# 9.截屏，并将截屏图片保存在指定路径+名称+后缀
driver.get_screenshot_as_file("D:\\py_workspace\\test.png")

# 10.退出，有close 和quit 两种方式
# close 用于关闭当前窗口，当窗口打开较多时，close能用于关闭部分窗口；
# quit 用于结束进程，关闭所有窗口。结束城市时，用quit可以回收C盘的临时文件。
driver.quit()




