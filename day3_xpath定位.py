'''
HTML 旨在显示信息，而 XML 旨在传输信息。
XML 没有预定义的标签。XML 允许创作者定义自己的标签和自己的文档结构。
在 HTML 中使用的标签（以及 HTML 的结构）是预定义的。HTML 文档只使用在 HTML 标准中定义过的标签（比如 <p> 、<h1> 等等）。
'''

from selenium import webdriver
import time
profile_dictionary = R"C:\Users\R\AppData\Roaming\Mozilla\Firefox\Profiles\yjdic0n5.default"
profile=webdriver.FirefoxProfile(profile_dictionary)
driver = webdriver.Firefox(profile)

driver.get("Http://www.baidu.com")
# 1. xpath 属性定位
# 1）通过元素ID、class、name等属性定位  *代表任意标签
# driver.find_element_by_xpath("//*[@id='kw']").send_keys("python")
# driver.find_element_by_xpath("//*[@class='s_ipt']").send_keys("python")
# driver.find_element_by_xpath("//*[@name='wd']").send_keys("python")

# 2)如果一个元素id、name、class属性都没有，这时候也可以通过其它属性定位到
# 3) xpath:标签   *代表任意标签；如果有具体标签直接写标签即可
# driver.find_element_by_xpath("//input[@autocomplete='off']").send_keys("python")

# 4)xpath:层级 1.如果一个元素，它的属性不是很明显，无法直接定位到，这时候我们可以先找父元素2.再找下个层级就能定位到了。
# 要是其父属性也不是很明显，就找它父元素的父元素。
# driver.find_element_by_xpath("//form[@id='form']/span/input").send_keys("python") 

# 5)xpath：索引 如果一个元素和其兄弟元素tag相同，那么使用层级来定位，就需要索引指定。索引从1开始算起
# driver.find_element_by_xpath("//select[@id='nr']/option[1]").click()
# driver.find_element_by_xpath("//select[@id='nr']/option[2]").click()

# 6)xpath :逻辑运算 与或非 and or not 
# driver.find_element_by_xpath("//*[@id='kw' and @autocomplete= 'off']").send_keys("python")

# 7) xpath :模糊匹配
# 掌握了模糊匹配功能，基本上没有定位不到的。
# 比如我要定位百度页面的超链接“hao123”,在上一篇中讲过可以通过by_link,也可以通过by_partial_link，模糊匹配定位到。
# 当然xpath也可以有同样的功能，并且更为强大。 contains,starts-with,ends-with,matchs
# 匹配文本
# driver.find_element_by_xpath("//*[contains(text(),'hao123')]").click()
# 模糊匹配某个属性
# driver.find_element_by_xpath("//*[contains(@id,'kw')]").send_keys("python")
# 模糊匹配以什么开头
# driver.find_element_by_xpath("//*[starts-with(@id,'s_kw_')]").click()
#模糊匹配以什么结尾
# driver.find_element_by_xpath("//*[ends-with(@id,'kw_wrap')]").click()
#正则表达式
# driver.find_element_by_xpath("//*[matches(text(),'hao13')]").click()



time.sleep(2)
driver.quit() 