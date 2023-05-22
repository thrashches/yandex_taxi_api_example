import requests

CLIENT_ID = ""

API_KEY = ""

PARK_ID = ""


def car_list(client_id=CLIENT_ID, api_key=API_KEY, park_id=PARK_ID):
    """
    Список авто
    """
    url = 'https://fleet-api.taxi.yandex.net/v1/parks/cars/list'
    headers = {
        "X-Client-ID": client_id,
        "X-API-Key": api_key,
    }
    query_data = {
        "fields": {
            "car": [
                "color"
            ]
        },
        "limit": 100,
        "offset": 0,
        "query": {
            "park": {
                "car": {
                    # "amenities": [
                    #     "wifi"
                    # ],
                    "categories": [
                        "econom"
                    ],
                    # "id": [
                    #     "5011ade6ba054dfdb7143c8cc9460dbc"
                    # ],
                    "is_rental": True,
                    "status": [
                        "working"
                    ]
                },
                "id": park_id
            },
            "text": ""
        }
    }
    response = requests.post(
        url=url,
        headers=headers,
        json=query_data
    )
    print(response.status_code)
    response_data = response.json()
    print(response_data)


def car(car_id, client_id=CLIENT_ID, api_key=API_KEY, park_id=PARK_ID):
    """
    Информация о машине
    """
    url = 'https://fleet-api.taxi.yandex.net/v2/parks/vehicles/car'
    headers = {
        "X-Client-ID": client_id,
        "X-API-Key": api_key,
        "X-Park-ID": park_id,
    }
    response = requests.get(
        url=url,
        headers=headers,
        params={
            "vehicle_id": car_id,
        }
    )
    print(response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    car_list(CLIENT_ID, API_KEY, PARK_ID)
    car("661c48eb176649a9adc7553dd83b039a")
