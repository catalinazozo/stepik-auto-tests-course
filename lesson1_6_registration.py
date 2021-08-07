from selenium import webdriver
import time

try:
    link = " http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_css_selector("div.first_block .form-group.first_class input")
    first_name.send_keys("Ivan")
    last_name = browser.find_element_by_css_selector("div.first_block .form-group.second_class input")
    last_name.send_keys("Petrov")
    email = browser.find_element_by_css_selector("div.first_block .form-group.third_class input")
    email.send_keys("email@email.com")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(10)

    welcome_text_elt = browser.find_element_by_tag_name("h1")

    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
