from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe")
driver.get("https://www.google.com")
print(driver.title)