import pytest
import requests

BASE_URL = "https://ipinfo.io"

@pytest.mark.parametrize("ip_address", ["8.8.8.8", "192.168.0.1"])
def test_valid_ip_address(ip_address):
    response = requests.get(f"{BASE_URL}/{ip_address}")
    assert response.status_code == 200
    assert "country" in response.json()
    assert "city" in response.json()
    assert "loc" in response.json()


def test_own_ip_address():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert "ip" in response.json()


def test_additional_parameters():
    response = requests.get(f"{BASE_URL}/8.8.8.8?format=json&lang=en")
    assert response.status_code == 200
    assert "country" in response.json()
    assert "city" in response.json()
    assert "loc" in response.json()


def test_invalid_ip_address():
    response = requests.get(f"{BASE_URL}/123.456.789.0")
    assert response.status_code != 200


def test_empty_ip_address():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code != 200


def test_invalid_additional_parameters():
    response = requests.get(f"{BASE_URL}/8.8.8.8?invalid_param=value")
    assert response.status_code == 200
    assert "country" in response.json()
    assert "city" in response.json()
    assert "loc" in response.json()


def test_request_limit():
    for i in range(100):  # Выполняем 100 запросов
        response = requests.get(BASE_URL)
        assert response.status_code == 200