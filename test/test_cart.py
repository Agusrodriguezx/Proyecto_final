from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_cart(driver_logged):
    driver = driver_logged

    # agregar producto al carrito
    driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()

    # verificar contador de carrito
    contador_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

    assert contador_cart.text == "1", "El producto no se agregó correctamente"

    # obtener nombre del primer producto 
    product_name = driver.find_elements(By.CLASS_NAME, "inventory_item_name ")[0].text

    # ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # obtener el nombre del carrito
    cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    #verificar el producto agregado en el carrito
    assert cart_item == product_name, "El producto agregado no coincide"