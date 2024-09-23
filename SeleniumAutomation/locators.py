from selenium.webdriver.common.by import By

#Class Locators
toggle_switch =(By.CLASS_NAME,'oxd-switch-input oxd-switch-input--active --label-right')

#Name locators
uname = (By.NAME,'username')
pswd = (By.NAME,'password')
fname = (By.NAME,'firstName')
lname = (By.NAME,'lastName')

#Tag_name locators
login_btn = (By.TAG_NAME,'button')

#Link-Text locators
admin = (By.LINK_TEXT,'Admin')
pim = (By.LINK_TEXT,'PIM')

#XPATH Locators
ADD_BUTTON = (By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
