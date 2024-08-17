from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# driver.get("https://akshaybabu.github.io")
# print(driver.title)
driver1 = webdriver.Chrome(executable_path= ChromeDriverManager().install())
driver1.get("https://www.google.com")
print(driver1.title)
print(driver1.name)
print(driver1.page_source)
