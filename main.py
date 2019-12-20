from selenium import webdriver
import re
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com/maps/place/Bei+Oma+Kleinmann/@50.9295372,6.9384262,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipO38CGk5WiJfhDbUjBwZbMclY4oS49V7oZ7dN2O!2e10!3e12!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipO38CGk5WiJfhDbUjBwZbMclY4oS49V7oZ7dN2O%3Dw114-h86-k-no!7i1024!8i768!4m13!1m7!3m6!1s0x47bf24fe53a1dd51:0xe5a4b6a2f8b104bf!2sBei+Oma+Kleinmann!8m2!3d50.9295329!4d6.9383544!10e1!3m4!1s0x47bf24fe53a1dd51:0xe5a4b6a2f8b104bf!8m2!3d50.9295329!4d6.9383544?hl=ru")
timeout = 3

xpath = '//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]/div[1]/div/a/div[1]/div'

try:
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    print("Page loaded")

foto = driver.find_element_by_xpath(xpath)

style_attr = foto.get_attribute("style")
regex = r'\"(.*?)\"'

matches = re.finditer(regex, style_attr, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    url = match.group()
    print(url)

driver.close()