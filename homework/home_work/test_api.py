import requests
import pytest

# URL для тестирования
url = "https://backend.belurk.ru/api/tools/get-ip-address-information"
@pytest.mark.smoke
def test_api_response_body():
    response = requests.get(url)
    # Проверяем, что статус-код ответа 200 (успешный запрос)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    print(response)
    # Преобразуем тело ответа в JSON-формат
    response_json = response.json()
    # Проверяем, что тело ответа содержит ключи 'userId', 'id', 'title', 'body'
    assert "data" in response_json, "data' key not found in response"
    # Ожидаемая структура данных
    expected_data = {
        "country": "Нидерланды",
        "country_code": "NL",
        "country_icon": "https://storage.belurk.com/icons/iconNL.svg",
        "region": "North Holland",
        "provider": "Serverel Inc.",
        "city": "Amsterdam",
        "zip_code": 1012,
        "latitude": 52.374,
        "longitude": 4.8897,
        "ip_address": "95.47.138.133"
    }

    # Получаем данные из 'data'
    data = response_json['data']

# Перебираем ключи и проверяем, что они присутствуют и имеют правильные значения
    for key in expected_data.keys():
        assert key in data, f"Expected key '{key}' not found in 'data'"
        assert data[key] == expected_data[key], f"Expected '{key}' to be '{expected_data[key]}', but got '{data[key]}'"