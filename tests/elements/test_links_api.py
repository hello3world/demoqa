import requests
import logging

BASE_URL = "https://demoqa.com/"

def test_api_created():
    try:
        response = requests.get(BASE_URL + "created")
        assert response.status_code == 201
    except Exception as e:
        logging.error(f"Error in test_api_created: {e}")
        raise
    
def test_api_no_content():
    try:
        response = requests.get(BASE_URL + "no-content")
        assert response.status_code == 204
    except Exception as e:
        logging.error(f"Error in test_api_no_content: {e}")
        raise

def test_api_moved():
    try:
        response = requests.get(BASE_URL + "moved")
        assert response.status_code == 301
    except Exception as e:
        logging.error(f"Error in test_api_moved: {e}")
        raise

def test_api_unauthorized():
    try:
        response = requests.get(BASE_URL + "unauthorized")
        assert response.status_code == 401
    except Exception as e:
        logging.error(f"Error in test_api_unauthorized: {e}")
        raise

def test_api_forbidden():
    try:
        response = requests.get(BASE_URL + "forbidden") 
        assert response.status_code == 403
    except Exception as e:
        logging.error(f"Error in test_api_forbidden: {e}")
        raise

def test_api_not_found():
    try:
        response = requests.get(BASE_URL + "invalid-url")
        assert response.status_code == 404
    except Exception as e:
        logging.error(f"Error in test_api_not_found: {e}")
        raise
