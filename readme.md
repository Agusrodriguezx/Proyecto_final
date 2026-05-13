# Proyecto de Automatizacion QA - Agustina Rodriguez

## Descripcion

Proyecto de automatización de pruebas funcionales desarrollado con Python, Selenium WebDriver y Pytest.

Las pruebas cubren los flujos principales de la aplicación web Swag Labs: login, visualización del inventario y manejo del carrito de compras.


## Tecnologias usadas
- Python
- Selenium WebDriver
- Pytest
- Pytest HTML
- Google Chrome + ChromeDriver
- Git

## Instalacion

`git clone https://github.com/Agusrodriguezx/Pre-Proyecto.git
cd Pre-Proyecto`


## Instalacion Dependencias
pip install -r requirements.txt


## Fucionamiento de las pruebas

- test_login.py — Pruebas de autenticación
test_login_validation: Verifica que tras el login el usuario es redirigido a /inventory.html

- test_inventory.py — Pruebas del catálogo
test_inventory_title: Verifica que el título de la página sea "Swag Labs"
test_productos_visibles: Verifica que se muestre al menos un producto en el catálogo
test_ui_elements: Verifica que el menú hamburguesa y el filtro de productos estén visibles

- test_cart.py — Pruebas del carrito
test_cart: Agrega el primer producto al carrito, verifica el contador, navega al carrito y comprueba que el producto agregado coincida