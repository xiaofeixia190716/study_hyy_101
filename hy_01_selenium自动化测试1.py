import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#设置正确的驱动路径
service = Service(executable_path = '/Users/hmt/Documents/pyst2/geckodriver')
driver = webdriver.Firefox(service=service)
try:
    #打开一个网站
    driver.get('https://www.baidu.com')
    wait = WebDriverWait(driver,10000)
    element = wait.until(EC.presence_of_element_located(('name','wd')))

#获取标题
    print(driver.title)
    # print(driver.page_source)
    #查找页面元素 - 输入框
    input_element = driver.find_element('name','wd')
    input_element.send_keys('Selenium')

    #最大化屏幕
    driver.maximize_window()
    # 设置浏览器窗口大小
    driver.set_window_size(1024,768)
    # 全屏
    driver.fullscreen_window()
    time.sleep(2)
    
    

    #按钮点击
    time.sleep(5)
    button_element = driver.find_element(By.ID,'su')
    button_element.click()
    wait = WebDriverWait(driver,10000)
    element = wait.until(EC.presence_of_element_located((By.ID,'su')))
    # time.sleep(5)
    #强制停止页面加载 - 该行代码未生效(网络响应太快，无法测试)
    driver.execute_script('window.stop();')
    driver.back()

    #打开搜索页的二级页面
    button_element2 = driver.find_element(By.CLASS_NAME,'lb')
    button_element2.click()

    
    

except Exception as e:
    print('报错：%s' % e) 

# finally:
    
# # 关闭网站
#     driver.quit()