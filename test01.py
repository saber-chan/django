#python+selenium自动化练习01：断言打开页面并进行搜索
# coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
# driver.implicitly_wait(2)

driver.get("https://www.baidu.com")
driver.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")
driver.find_element_by_xpath("//*[@id='su']").click()

time.sleep(3)
# 断言方法判断
ele_string = driver.find_element_by_xpath("//*[@id='2']/h3/a").text
if (ele_string == u"Selenium - Web Browser Automation"):
    print("结果和预期结果匹配！")
    # 打开官网
    driver.find_element_by_xpath("//*[@id='1']/h3/a").click()
    print("测试成功，成功打开目标网址！")

# 定义当前窗口句柄（百度）
baidu_handle = driver.current_window_handle
# 获取当前窗口句柄集合
handles = driver.window_handles
# print(handles)
# 获取新窗口
new_handle = None
for handle in handles:
    if handle != baidu_handle:
        # 捕获新打开的窗口
        new_handle = handle
# print('switch to ', handle)
# 新窗口打开搜索结果
driver.switch_to.window(new_handle)
time.sleep(10)

driver.quit()