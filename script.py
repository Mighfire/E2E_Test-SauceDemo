from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://www.saucedemo.com/"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_login = browser.find_element(By.CSS_SELECTOR, "[data-test=username]")
    input_login.send_keys("standard_user")
    input_pass = browser.find_element(By.CSS_SELECTOR, "[data-test=password]")
    input_pass.send_keys("secret_sauce")
    button = browser.find_element(By.CSS_SELECTOR, "[data-test=login-button]")
    button.click()

    button_add = browser.find_element(By.CSS_SELECTOR, "[data-test=add-to-cart-sauce-labs-fleece-jacket]")
    button_add.click()
    button_cart = browser.find_element(By.CSS_SELECTOR, "[data-test=shopping-cart-link]")
    button_cart.click()

    cart_element = browser.find_element(By.CSS_SELECTOR, "a[data-test=item-5-title-link] .inventory_item_name")
    assert "Sauce Labs Fleece Jacket" in cart_element.text, "Item not found in cart"
    button_checkout = browser.find_element(By.CSS_SELECTOR, "[data-test=checkout]")
    button_checkout.click()

    input_fn = browser.find_element(By.CSS_SELECTOR, "[data-test=firstName]")
    input_fn.send_keys("Ivan")
    input_ln = browser.find_element(By.CSS_SELECTOR, "[data-test=lastName]")
    input_ln.send_keys("Petrov")
    input_zip = browser.find_element(By.CSS_SELECTOR, "[data-test=postalCode]")
    input_zip.send_keys("123456")
    button_continue = browser.find_element(By.CSS_SELECTOR, "[data-test=continue]")
    button_continue.click()
    button_finish = browser.find_element(By.CSS_SELECTOR, "[data-test=finish]")
    button_finish.click()

    complete = browser.find_element(By.CSS_SELECTOR, "[data-test=complete-header]")
    assert "Thank you for your order!" in complete.text, "Order isn't completed"

    print('Тест завершен без ошибок')

finally:
    time.sleep(5)
    browser.quit()
