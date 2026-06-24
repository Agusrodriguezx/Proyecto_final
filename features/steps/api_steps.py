from behave import Given,When,Then
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
headers = {
    "x-api-key": API_KEY
}

@Given("la API de ReqRes esta disponible")
def step_impl(context):
    context.base_url = "https://reqres.in/api"

@When("realiza un login valido")
def step_impl(context):
    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    context.response = requests.post(
                        f"{context.base_url}/login",
                        headers=headers,
                        json=body
    )

@Then("el status code debe ser {status_code:d}")
def step_validacion_status(context,status_code):
    assert context.response.status_code == status_code

# Scenario 2
@When("realiza un login sin contraseña")
def step_impl(context):
    body = {
        "email": "eve.holt@reqres.in",
    }

    context.response = requests.post(
                        f"{context.base_url}/login",
                        headers=headers,
                        json=body
    )

@Then("el mensaje de error debe ser '{mensaje}'")
def step_impl(context,mensaje):
    body = context.response.json()

    assert body["error"] == mensaje