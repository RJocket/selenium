from selenium import webdriver
import time
# 源码中，元素定位最终调用的也是CSS _selector

profile_dictionary=R"C:\Users\R\AppData\Roaming\Mozilla\Firefox\Profiles\yjdic0n5.default"
profile = webdriver.FirefoxProfile(profile_dictionary)
driver = webdriver.Firefox(profile)

driver.get("http://www.baidu.com")


# <input id="kw" class="s_ipt" type="text" autocomplete="off" maxlength="100" name="wd"/>

# 1.id，class，tag等常规属性的css_selector定位。
# css 使用#号代表id属性，如：#kw
# css 使用.代表class属性，如：.s_ipt
# css 直接使用标签，无特殊符号，如：input

# driver.find_element_by_css_selector("#kw").send_keys("python")
# driver.find_element_by_css_selector(".s_ipt").send_keys("pyhton")
# 由于多个input标签，这里会报错，只是为了说明这种写法
# driver.find_element_by_css_selector("input").send_keys("python")

# 2.除了id,class,tag等常规属性之外，其他属性的css_selector定位
# driver.find_element_by_css_selector("[name ='wd']").send_keys("pyhton")
# driver.find_element_by_css_selector("[autocomplete='off']").send_keys("python")
# driver.find_element_by_css_selector("[type='text']").send_keys("python")

# 3.css 标签与属性的组合定位
# 标签与id属性组合
# driver.find_element_by_css_selector("input#kw").send_keys("python")
# 标签与class属性组合
# driver.find_element_by_css_selector("input.s_ipt").send_keys("pyhton")
# 标签与其他属性组合
# driver.find_element_by_css_selector("input[id='kw']").send_keys("python")

# 4.css 层级关系
# 1.在前面一篇xpath中讲到层级关系定位，这里css也可以达到同样的效果
# 2.如xpath：
# //form[@id='form']/span/input和
# //form[@class='fm']/span/input也可以用css实现

# driver.find_element_by_css_selector("form#form>span>input").send_keys("python")
# driver.find_element_by_css_selector("form.fm>span>input").send_keys("python")

# 5.CSS索引
# css也可以通过索引option：nth-child(1)来定位子元素，这点与xpath写法用很大差异，其实很好理解，直接翻译过来就是第几个小孩。
# driver.find_element_by_css_selector("select#nr>option:nth-child(1)").click()
# driver.find_element_by_css_selector("select#nr>option:nth-child(2)").click()

# 6.css逻辑运算
# css同样也可以实现逻辑运算，同时匹配两个属性，这里跟xpath不一样，无需写and关键字
driver.find_element_by_css_selector("input[id='kw'][name='wd']").send_keys("python")



time.sleep(2)
driver.quit()