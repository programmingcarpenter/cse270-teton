import pytest
import requests

# Test function that sends a GET request to the endpoint with username=admin and password=admin
def test_get_users_with_invalid_credentials(mocker):
    url = "https://127.0.0.1:8000/users"
    params = {
        "username": "admin",
        "password": "admin"
    }
    
    # Mock the response from the server for invalid credentials
    mock_response = requests.Response()
    mock_response.status_code = 401
    mock_response._content = b""  # Empty content for 401 response
    
    mocker.patch("requests.get", return_value=mock_response)
    
    # Make a synchronous GET request using requests
    response = requests.get(url, params=params, verify=False)
    
    # Assert the response status code is 401 (Unauthorized)
    assert response.status_code == 401
    assert response.text == ""


# Test function that sends a GET request to the endpoint with username=admin and password=qwerty
def test_get_users_with_valid_credentials(mocker):
    url = "https://127.0.0.1:8000/users"
    params = {
        "username": "admin",
        "password": "qwerty"
    }

    # Mock the response from the server for valid credentials
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = b""  # Empty content for 200 response
    
    mocker.patch("requests.get", return_value=mock_response)
    
    # Make a synchronous GET request using requests
    response = requests.get(url, params=params, verify=False)
    
    # Assert the response status code is 200 (OK)
    assert response.status_code == 200
    assert response.text == ""
