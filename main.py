from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Запуск без графического интерфейса
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Запускаем браузер без указания пути к WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.implicitly_wait(4)
driver.get("https://api.ipify.org")
print(driver.find_element(By.TAG_NAME, "pre").text)

driver.quit()
