from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
import time

def she():

    service = Service(executable_path='/Users/hmt/Documents/pyst2/geckodriver')
    driver = webdriver.Firefox(service=service)
    return driver

driver = she()
driver.get('https://www.baidu.com/')

# sendkeys方法写入
a1 = driver.find_element(By.ID , 'kw')
a1.send_keys('qq邮箱')
time.sleep(1)

#click点击方法使用
a2 = driver.find_element(By.ID , 'su')
a2.click()
time.sleep(2)

#clear()清空输入框内容
a3 = driver.find_element(By.ID , 'kw')
a3.clear()
time.sleep(2)

#获取元素属性值
a4 = driver.find_element(By.ID , 'kw')
att_1 = a4.get_attribute('id')
print(att_1)

a5 = driver.find_element(By.CLASS_NAME , 'tts-b-hl')
att_2 = a5.get_attribute('class')
a5.click()
print(att_2)

try:
    wait = WebDriverWait(driver, 20)  # 延长等待时间

    # 1. 切换到第一层 iframe（外层 iframe）
    outer_frame = wait.until(EC.frame_to_be_available_and_switch_to_it(
        (By.CSS_SELECTOR, "iframe.QQMailSdkTool_login_loginBox_qq_iframe")
    ))

    # 2. 切换到第二层 iframe（内层 iframe，ptlogin2.qq.com）
    inner_frame = wait.until(EC.frame_to_be_available_and_switch_to_it(
        (By.ID, "ptlogin_iframe")
    ))

    # 3. 现在可以定位 "密码登录" 按钮
    password_login_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "switcher_plogin"))  # 方法1：By.ID
        # EC.element_to_be_clickable((By.LINK_TEXT, "密码登录"))  # 方法2：By.LINK_TEXT
        # EC.element_to_be_clickable((By.CSS_SELECTOR, "a#switcher_plogin.link"))  # 方法3：CSS
    )
    password_login_btn.click()
    print("成功切换到密码登录！")

except Exception as e:
    print("定位失败:", e)
    # 如果常规方法失败，尝试用 JavaScript 直接点击
    try:
        password_login_btn = driver.find_element(By.ID, "switcher_plogin")
        driver.execute_script("arguments[0].click();", password_login_btn)
        print("通过 JS 点击成功！")
    except:
        print("JS 点击也失败，请手动检查页面结构。")

finally:
    # 切换回默认内容（避免后续操作报错）
    driver.switch_to.default_content()
    # driver.quit()








# driver.quit()