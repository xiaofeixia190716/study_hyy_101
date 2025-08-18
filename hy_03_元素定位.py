from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path='/Users/hmt/Documents/pyst2/geckodriver')
driver = webdriver.Firefox(service=service)

try:
    driver.get('https://mail.qq.com/')

    


    #全屏
    driver.maximize_window()
    driver.refresh()

    # time.sleep(5)

    #切换到密码登陆状态
    # pwd_login_page = driver.find_element(By.ID,'switcher_plogin')
    # pwd_login_page = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[10]/a[2]')))

    pwd_login_page = driver.find_element(By.LINK_TEXT, "联系我们")
    pwd_login_page.click()

    time.sleep(2)

    # pwd_login_page2 = driver.find_element(By.ID , 'switcher_plogin')
    # pwd_login_page2.click()


    # pwd_login_page = driver.find_element(By.CSS_SELECTOR, "a[id='switcher_plogin']")
    # pwd_login_page = driver.find_element(By.ID ,'QQMailSdkTool_login_loginBox_tab_item_wx')
    # pwd_login_page = driver.find_element(By.LINK_TEXT, '密码登录')
    # pwd_login_page = driver.find_element(By.CSS_SELECTOR, '#switcher_plogin')
    # pwd_login_page = driver.execute_script("return document.querySelector('dynamic_selector');")
    # print(pwd_login_page)

    #通过id定位输入框并输入文本 

    # element = driver.find_element(By.ID, 's')
    # element.send_keys('testuser')

    # #通过name定位输入框并输入文本
    # element = driver.find_element(By.NAME, 'u')
    # element.send_keys('1205451499')


except Exception as e:
    print('报错：%s' % e)

    
finally:
    time.sleep(5)
    driver.quit()
