@login
Feature: Inicio de sesion
    Background:
        Given que el usuario está en la página de login

    @positivo
    Scenario: Login exitoso
        When ingresa el usuario 'standard_user' y la contraseña 'secret_sauce'
        And hace click en el botón Login
        Then debería ingresar al inventario

    @negativo
    Scenario: Login inválido con contraseña incorrecta
        When ingresa el usuario 'standard_user' y la contraseña '1234'
        And hace click en el botón Login
        Then debería ver el mensaje de error 'Epic sadface: Username and password do not match any user in this service'

    @negativo @regression
    Scenario Outline: Login inválido con diferetes usuarios.
        When ingresa el usuario '<usuario>' y la contraseña '<password>'
        And hace click en el botón Login
        Then debería ver el mensaje de error '<mensaje>'

        Examples:
            |usuario|password|mensaje|
            |standard_user|1234|Epic sadface: Username and password do not match any user in this service|
            |standart_user|secret_sauce|Epic sadface: Username and password do not match any user in this service|
            |VACIO|secret_sauce|Epic sadface: Username is required|
            |standard_user|VACIO|Epic sadface: Password is required|