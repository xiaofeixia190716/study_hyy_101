from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time


#设置正确的驱动路径
service = Service(executable_path = '/Users/hmt/Documents/pyst2/geckodriver')
driver = webdriver.Firefox(service=service)
try:
    #打开一个网站
    driver.get('https://www.runoob.com')
    
    #进入下一层页面
    # driver.forward()
    time.sleep(5)

    #最大化页面
    driver.maximize_window()

    #获取标题
    title = driver.title
    print('页面标题：',title)
    #获取url
    url = driver.current_url
    print('页面url：',url)
    
    #获取第二个网站
    driver.get('https://www.jyshare.com')

    #返回上一个页面
    driver.back()

    #刷新当前页面
    driver.refresh()
    
except Exception as e:
    print('报错：%s' % e)


finally:
    
    driver.quit()