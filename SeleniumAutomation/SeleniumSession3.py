import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import locators
import login
service = Service('E:\\webdrivers\\chromedriver.exe')
driver = webdriver.Chrome(service=service)
url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
driver.get(url)
driver.maximize_window()
time.sleep(5)
# username = driver.find_element(By.XPATH,"//*[@name='username']")
# password = driver.find_element(By.XPATH,"//*[@name='password']")
usernamef = driver.find_element(*locators.uname)
passwordf = driver.find_element(*locators.pswd)

usernamef.send_keys(*login.uname)
passwordf.send_keys(*login.pswrd)
# driver.find_element(By.XPATH,'//button').click()
driver.find_element(*locators.login_btn).click()
time.sleep(5)
#driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
driver.find_element(*locators.admin).click()
time.sleep(5)
driver.find_element(*locators.pim).click()
time.sleep(5)
add = driver.find_element(*locators.ADD_BUTTON)
add.click()
time.sleep(5)
driver.find_element(*locators.fname).send_keys('abcdef')
driver.find_element(*locators.lname).send_keys('qwerty')
time.sleep(3)
driver.find_element(*locators.toggle_switch).click()

time.sleep(5)
driver.quit()
