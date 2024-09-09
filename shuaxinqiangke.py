#%%
USER_NAME = ''
PASSWORD = ''
CLASS = '06312'
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# options = Options()
# options.add_argument("start-maximized")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.get("https://www.baidu.com")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# ser = Service("./chromedriver_linux64/chromedriver")
ser = Service("./chromedriver-win64/chromedriver-win64/chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
# driver.get('https://www.baidu.com')

from selenium.webdriver.common.by import By
# 打开网页
driver.get('http://classes.tju.edu.cn/eams/stdElectCourse!defaultPage.action')

# 登录
un = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[2]/form/div/div[1]/div[2]/input')
un.send_keys(USER_NAME)

pswd = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[2]/form/div/div[2]/div[2]/input')
pswd.send_keys(PASSWORD)

import time
time.sleep(10)

# 找到进入选课按钮并点击
button = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/form/a') # 使用XPath选择按钮
button.click()

# 获取所有窗口句柄
all_windows = driver.window_handles

# 切换到指定窗口
driver.switch_to.window(all_windows[1]) # 通过索引切换到指定的窗口

# 找到可选课程
try:
    kexuan = driver.find_element(By.XPATH,'/html/body/div[9]/div[1]/div[2]')
    kexuan.click()
except:
    print("未找到可选课程按钮")

# 找到目标课程
from selenium.webdriver.common.keys import Keys
# sousuo = driver.find_element(By.XPATH,'/html/body/div[9]/div[3]/div[1]/table[1]/thead/tr[1]/th[2]/div/input')
# # sousuo = driver.find_element(By.XPATH,'//*[@id="electableLessonList"]/thead/tr[1]/th[2]/div/input')
# # sousuo = driver.find_element(By.NAME,'electableLesson.no')
# sousuo.send_keys(CLASS)
# sousuo.send_keys(Keys.ENTER)
# time.sleep(3)


# 查询按钮
from selenium.webdriver.common.action_chains import ActionChains
# actions = ActionChains(driver)
# cha = driver.find_element(By.XPATH,'/html/body/div[9]/div[3]/div[1]/table[1]/thead/tr[1]/th[10]/input')
# # cha = driver.find_element(By.ID,'electableLessonList_filter_submit')
# actions.move_to_element(cha).click().perform()
# cha.click()
# # cha.submit()

cnt = 0
# 选课
while True:
    # 点一下可选课程，免得不小心退课了
    kexuan = driver.find_element(By.XPATH,'/html/body/div[9]/div[1]/div[2]')
    kexuan.click()
    # 找到目标课程
    sousuo = driver.find_element(By.XPATH, '/html/body/div[9]/div[3]/div[1]/table[1]/thead/tr[1]/th[2]/div/input')
    # sousuo = driver.find_element(By.XPATH,'//*[@id="electableLessonList"]/thead/tr[1]/th[2]/div/input')
    # sousuo = driver.find_element(By.NAME,'electableLesson.no')
    sousuo.send_keys(CLASS)
    sousuo.send_keys(Keys.ENTER)
    time.sleep(2)
    # 点击查询按钮
    actions = ActionChains(driver)
    cha = driver.find_element(By.XPATH, '/html/body/div[9]/div[3]/div[1]/table[1]/thead/tr[1]/th[10]/input')
    # cha = driver.find_element(By.ID,'electableLessonList_filter_submit')
    actions.move_to_element(cha).click().perform()
    cha.click()
    time.sleep(1)
    # 点击选课按钮
    xuan = driver.find_element(By.XPATH,'/html/body/div[9]/div[3]/div[1]/table[1]/tbody/tr/td[12]/a')
    xuan.click()
    # 弹出确定窗口
    aler = driver.switch_to.alert
    print(aler.text,end='')
    print(cnt)
    # 防止不小心退课或发生其他事
    if aler.text=='上限人数已满，请稍后再试':
        aler.accept() #确定、同意；三种弹窗都可使用
        # time.sleep(1)
        cnt=cnt+1
        driver.refresh()
    else:
        # 选课成功或出现异常就不点击弹框的确定按钮了
        break


# 关闭浏览器
# driver.quit()