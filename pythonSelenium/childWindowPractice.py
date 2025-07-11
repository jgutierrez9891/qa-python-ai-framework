import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])
email = driver.find_element(By.XPATH, "//p[@class='im-para red']/strong/a").text
driver.close()
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.ID,'username').send_keys(email)
driver.find_element(By.ID,'password').send_keys('123456')
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(2)
assert "Incorrect username/password." == driver.find_element(By.CLASS_NAME,'alert-danger').text


