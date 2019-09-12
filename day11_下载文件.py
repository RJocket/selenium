# 下载文件。可以设置文件默认下载路径。不同浏览器下载设置方式不同

# Firefox浏览器下载

# import os
# from selenium import webdriver

# fp = webdriver.FirefoxProfile()

# # 在firefox中输入about:config可以找到参数
# # 0代表默认下载路径；2：代表指定目录
# fp.set_preference("browser.download.folderList",2)
# # browser.download.dir 制定下载目录；os.getcwd()获取当前文件所在位置，即下载文件保存的目录
# fp.set_preference("browser.download.dir",os.getcwd())
# # 指定下载文件的类型，即Content_type 值，"binary/octet-stream" 代表二进制文件
# fp.set_preference("browser.helperApps.neverAsk.saveToDisk","binary/octet-stream")

# driver = webdriver.Firefox(firefox_profile=fp)
# driver.get("https://pypi.org/project/selenium/#files")
# driver.find_element_by_partial_link_text("selenium-3.141.0.tar.gz").click()


# Chrome浏览器下载
import os
from selenium import webdriver
options = webdriver.ChromeOptions()
# 设置为0，代表禁止弹出下载窗口
prefs = {'profile.default_content_setting.popups':0,
		'download.default_directory':os.getcwd()}
options.add_experimental_option('prefs',prefs)

driver = webdriver.Chrome(chrome_options = options)
driver.get("https://pypi.org/project/selenium/#files")
driver.find_element_by_partial_link_text("selenium-3.141.0.tar.gz").click()
