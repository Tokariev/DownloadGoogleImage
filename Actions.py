import selenium.webdriver as webdriver



def move_to_elem(driver, elem):
    action = webdriver.ActionChains(driver)
    action.move_to_element(elem)
    action.perform()