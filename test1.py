import pytest
import requests

# Позитивные тестовые сценарии

def test_geolocation_by_ip():
    ip = "8.8.8.8"  # Здесь нужно указать известный IP-адрес
    response = requests.get(f"https://ipinfo.io/{ip}/json")
    assert response.status_code == 200
    data = response.json()
    assert "city" in data
    assert "region" in data
    assert "country" in data
    assert "loc" in data

def test_provider_info_by_ip():
    ip = "8.8.8.8"  # Здесь нужно указать известный IP-адрес
    response = requests.get(f"https://ipinfo.io/{ip}/json")
    assert response.status_code == 200
    data = response.json()
    assert "org" in data
    assert "asn" in data

def test_own_ip_info():
    response = requests.get("https://ipinfo.io/json")
    assert response.status_code == 200
    data = response.json()
    assert "ip" in data
    assert "city" in data
    assert "region" in data
    assert "country" in data
    assert "loc" in data
    assert "org" in data
    assert "asn" in data

# Негативные тестовые сценарии

def test_invalid_ip_format():
    invalid_ip = "invalidip"
    response = requests.get(f"https://ipinfo.io/{invalid_ip}/json")
    assert response.status_code != 200
    assert response.status_code == 400 or response.json() == {}

def test_invalid_api_key():
    invalid_api_key = "invalidapikey"
    response = requests.get(f"https://ipinfo.io/{invalid_api_key}/json")
    assert response.status_code != 200
    assert "unauthorized" in response.text or "Invalid API key" in response.text

def test_missing_ip():
    response = requests.get("https://ipinfo.io/json")
    assert response.status_code != 200
    assert "Please provide an IP address" in response.text

@pytest.mark.skip(reason="This test requires ipinfo.io to be unavailable")
def test_unavailable_api():
    response = requests.get("https://ipinfo.io/json")
    assert response.status_code != 200
    assert "Error" in response.text









