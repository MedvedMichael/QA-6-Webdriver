from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.foxtrot.com.ua/')
search_bar = driver.find_element_by_class_name('header-search__field')

search_bar.clear()
search_bar.send_keys('Samsung Galaxy')
search_bar.send_keys(Keys.RETURN)
time.sleep(1)

container = driver.find_elements_by_class_name('listing__body-wrap')[0]
found_elements = container.find_elements_by_class_name('card__title')
for element in found_elements:
    curr_title = element.get_attribute('title').lower()
    assert 'samsung' in curr_title and 'galaxy' in curr_title

print('Test is done :)')
driver.close()
