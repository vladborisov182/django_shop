#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

def init_driver():
    
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000")
    return driver

def check_wishlist_button(driver):
    
    driver.find_element_by_class_name("product-name").click()
    assert 'Войдите чтобы добавить товар в избранное' in driver.find_element_by_class_name("alert").text
    driver.find_element_by_link_text("Войти").click()
    driver.find_element_by_name("login").send_keys("vladborisov")
    driver.find_element_by_name("password").send_keys("rastaforay22081995")
    driver.find_element_by_class_name("btn-primary").click()
    driver.find_element_by_link_text("Избранное").click()
    assert 'Избранное' in driver.title
    assert 'Список избранного пуст' in driver.find_element_by_class_name("text-muted").text
    driver.find_element_by_link_text("Посмотреть товары").click()
    driver.find_element_by_class_name("product-name").click()
    driver.find_element_by_class_name("btn-wishlist-add").click()
    assert 'Удалить из избранного' in driver.find_element_by_class_name("btn-wishlist-del").text
    driver.find_element_by_class_name("btn-wishlist-del").click()
    assert 'Добавить в избранное' in driver.find_element_by_class_name("btn-wishlist-add").text

def check_cart(driver):
    driver.find_element_by_class_name("btn-cart").click()
    assert 'Ваша корзина товаров' in driver.title
    driver.find_element_by_link_text("Удалить").click()
    assert 'Корзина пуста' in driver.find_element_by_class_name("text-muted").text
    driver.find_element_by_link_text("Начать шопинг").click()
    assert 'Витрина' in driver.title

def check_callback(driver):
    driver.find_element_by_link_text("Обратная связь").click()
    assert 'Обратная связь' in driver.title
    driver.find_element_by_class_name("btn-success").click()
    assert 'Обратная связь' in driver.title
    driver.find_element_by_name("name").send_keys("Влад")
    driver.find_element_by_name("phone").send_keys("+380631234567")
    driver.find_element_by_class_name("btn-success").click()
    time.sleep(3)
    assert 'Спасибо' in driver.title
    driver.find_element_by_link_text("Вернуться на сайт").click()

def leave_the_site(driver):
    driver.find_element_by_link_text("Выйти (vladborisov)").click()
    driver.find_element_by_class_name("btn-primary").click()
    

    
    
    
def main():
    driver = init_driver()
    check_wishlist_button(driver)
    check_cart(driver)
    check_callback(driver)
    leave_the_site(driver)
          
if __name__ == "__main__":
    main()