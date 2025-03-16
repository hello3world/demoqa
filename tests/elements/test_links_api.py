import requests

BASE_URL = "https://demoqa.com/"

def test_api_created():
    response = requests.get(BASE_URL + "created")
    assert response.status_code == 201
    
def test_api_no_content():
    response = requests.get(BASE_URL + "no-content")
    assert response.status_code == 204

def test_api_moved():
    response = requests.get(BASE_URL + "moved")
    assert response.status_code == 301

def test_api_unauthorized():
    response = requests.get(BASE_URL + "unauthorized")
    assert response.status_code == 401

def test_api_forbidden():
    response = requests.get(BASE_URL + "forbidden") 
    assert response.status_code == 403

def test_api_not_found():
    response = requests.get(BASE_URL + "invalid-url")
    assert response.status_code == 404
