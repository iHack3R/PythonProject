from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Users\\udit_kumar\\OneDrive - S&P Global\\Documents\\browser_drivers\\chromedriver.exe")
driver.get("https://www.google.com/")
driver.find_element(By.XPATH, "//input[@title='Search']").send_keys("Selenium")
driver.find_element(By.XPATH, "//div[@class='CqAVzb lJ9FBc']//input[@name='btnK']").click()
driver.implicitly_wait(5)
driver.close()
