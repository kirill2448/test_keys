import pytest
import requests

# Параметры запроса
base_url = "https://ipinfo.io/products/asn-api"
valid_ip = "8.8.8.8"
valid_domain = "google.com"
valid_asn = "AS15169"
invalid_ip = "999.999.999.999"
invalid_asn = "AS12345-6"


def test_positive_scenario_01():
    response = requests.get(base_url, params={"ip": valid_ip})
    assert response.status_code == 200
    assert "organization" in response.json()


def test_positive_scenario_02():
    response = requests.get(base_url, params={"domain": valid_domain})
    assert response.status_code == 200
    assert "organization" in response.json()


def test_positive_scenario_03():
    response = requests.get(base_url, params={"asn": valid_asn})
    assert response.status_code == 200
    assert "ip_prefixes" in response.json()


def test_negative_scenario_04():
    response = requests.get(base_url, params={"ip": invalid_ip})
    assert response.status_code == 404


def test_negative_scenario_05():
    response = requests.get(base_url, params={})
    assert response.status_code == 400


def test_negative_scenario_06():
    response = requests.get(base_url, params={"asn": invalid_asn})
    assert response.status_code == 400