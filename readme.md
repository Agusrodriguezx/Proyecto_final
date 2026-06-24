# Proyecto de Automatización QA - Agustina Rodriguez

## Descripción

Proyecto de automatización de pruebas funcionales desarrollado con Python, Selenium WebDriver y Pytest.

Las pruebas cubren los flujos principales de la aplicación web Swag Labs: login, visualización del inventario y manejo del carrito de compras.

El proyecto implementa el patrón Page Object Model (POM) y diferentes enfoques de automatización, incluyendo Data-Driven Testing mediante archivos CSV y JSON, generación de reportes HTML, logging, capturas de pantalla automáticas y pruebas BDD utilizando Gherkin y Behave.

## Tecnologías usadas
- Python
- Selenium WebDriver
- Pytest
- Behave
- Gherkin
- Pytest HTML
- Logging
- CSV y JSON (Data-Driven Testing)
- Google Chrome + ChromeDriver
- Git
- GitHub Actions (CI/CD)

## CI/CD

El proyecto utiliza GitHub Actions para ejecutar las pruebas automáticamente en cada push o pull request a la rama principal.

El workflow corre los tests con Pytest en un entorno Ubuntu con Chrome en modo headless, y genera un reporte HTML como artefacto descargable desde la pestaña Actions de GitHub.

## Instalación
`git clone https://github.com/Agusrodriguezx/Proyecto_final.git
cd Proyecto_final`


## Instalación de Dependencias
pip install -r requirements.txt


## Ejecutar pruebas

### Con Pytest
```
pytest
```

### Con Behave
```
python3 -m behave
```

## Generar reporte HTML
pytest --html=report.html --self-contained-html


## Funcionamiento de las pruebas

### test_login.py — Pruebas de autenticación

- `test_login_ok`
    - Verifica que el usuario sea redirigido correctamente al inventario después de iniciar sesión.

- `test_login_invalid_password`
    - Verifica que se muestre el mensaje de error correspondiente al ingresar una contraseña inválida.

- Implementa logging para registrar la ejecución de las pruebas.
- Genera reportes HTML mediante pytest-html
- Captura automáticamente una imagen de la pantalla en caso de fallo.

---

### test_login_csv.py — Pruebas de automatización con datos parametrizados

- Implementa Data-Driven Testing mediante `pytest.mark.parametrize()`.

- Utiliza datos externos almacenados en `data/users.csv`.

- Lee los datos de prueba a través de `utils/data_reader.py`.

- Ejecuta múltiples escenarios de autenticación utilizando un único caso de prueba.

- Valida tanto escenarios positivos como negativos:
    - Credenciales válidas → acceso exitoso al inventario.
    - Credenciales inválidas → visualización del mensaje de error correspondiente.

---

### login.feature — Pruebas BDD con Gherkin y Behave

- Implementa escenarios de autenticación utilizando sintaxis Gherkin.

- Define escenarios positivos y negativos de login.

- Utiliza 'Scenario Outline' para ejecutar múltiples conjuntos de datos.

- Separa la descripción de los escenarios de su implementación en 'login_steps.py'.

---

### login_steps.py

- Implementa los pasos definidos en `login.feature`.

- Reutiliza la clase `LoginPage` para interactuar con la aplicación.

---

### environment.py

- Configura y administra el WebDriver para las pruebas ejecutadas con Behave.

---

### test_inventory.py — Pruebas del inventario

- `test_inventory_title`
    - Verifica que el título de la página sea "Swag Labs".

- `test_productos_visibles`
    - Verifica que exista al menos un producto visible en el inventario.

- `test_ui_elements` 
    - Verifica la presencia del menú hamburguesa y del filtro de productos.

---

### test_cart.py — Pruebas del carrito

- `test_cart`
    - Agrega un producto al carrito.
    - Verifica la actualización del contador del carrito.
    - Navega al carrito
    - Comprueba que el producto agregado sea el esperado.

---

### test_cart_json.py — Pruebas del carrito con datos externos

- Implementa Data-Driven Testing utilizando un archivo JSON.
- Utiliza datos almacenados en `data/products.json`.
- Lee los datos de prueba mediante `utils/data_reader.py`.
- Agrega múltiples productos al carrito utilizando información externa al test.
- Navega al carrito y valida que los productos agregados coincidan con los definidos en el archivo JSON.
- Verifica tanto el nombre como el precio de cada producto.


## Patrón de diseño utilizado

### Page Object Model (POM)
Se implementó el patrón Page Object Model para separar los elementos y acciones de cada página de las validaciones realizadas en los tests.

Las páginas se representan mediante clases independientes:
- LoginPage
- InventoryPage
- CartPage

Esto permite mejorar la reutilización del código y facilitar el mantenimiento de las pruebas automatizadas.