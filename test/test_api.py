import requests

from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

headers = {
    "x-api-key": API_KEY
}

def test_login_valido():
    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
        
    }

    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)

    assert response.status_code == 200

def test_login_sin_password():
    body = {
        "email": "eve.holt@reqres.in",
    }

    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)

    assert response.status_code == 400

def test_create_user():
    body = {
        "name": "Agustina",
        "email": "agustinarstudy@gmail.com",
        "password": "12345678"
    }

    response = requests.post("https://reqres.in/api/users", headers=headers, json=body)

    data = response.json()

    assert response.status_code == 201

    assert data["name"] == body["name"]
    assert data["email"] == body["email"]

    assert response.elapsed.total_seconds() < 1

def test_delete_user():
    response = requests.delete("https://reqres.in/api/users/2", headers=headers)

    assert response.status_code == 204

def test_get_user():
    response = requests.get("https://reqres.in/api/users/2", headers=headers)

    assert response.status_code == 200
    print(response.elapsed.total_seconds())
    assert response.elapsed.total_seconds() < 1, "El tiempo de ejecución tardó más de lo esperado"