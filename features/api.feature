@api
Feature: Login API ReqRes

    Scenario: Login valido
        Given la API de ReqRes esta disponible
        When realiza un login valido
        Then el status code debe ser 200

    Scenario: login sin password
        Given la API de ReqRes esta disponible
        When realiza un login sin contraseña
        Then el status code debe ser 400
        And el mensaje de error debe ser 'Missing password'