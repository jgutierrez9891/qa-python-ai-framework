from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
#click on column header
driver.find_element(By.ID, "downloadButton").click()

#edit the excel with updated value

file_input = driver.find_element(By.ID, "fileinput")
file_input.send_keys("C:\\Users\\joal9\\VARIOS\\2025\\python_selenium\\pythonSelenium\\download.xlsx")


file_upload = (By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)")
WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(file_upload))

print(driver.find_element(*file_upload).text)
