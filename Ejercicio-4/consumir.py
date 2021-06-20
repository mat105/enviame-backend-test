import json
from datetime import datetime
import requests

API_KEY = 'ea670047974b650bbcba5dd759baf1ed'


def post_delivery(content):
    url = 'https://stage.api.enviame.io/api/s2/v2/companies/401/deliveries'
    headers = {
        'api-key': API_KEY,
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }

    return requests.post(url, json=content, headers=headers)


def log_post_delivery(content):
    delivery = post_delivery(content)

    with open(f'response_{datetime.now().strftime("%Y%m%d-%H%M%S")}_{delivery.status_code}.json', 'w') as outfile:
        json.dump(delivery.json(), outfile, indent=4, sort_keys=True)


body = {
    "shipping_order": {
        "n_packages": "1",
        "content_description": "ORDEN 255826267",
        "imported_id": "255826267",
        "order_price": "24509.0",
        "weight": "0.98",
        "volume": "1.0",
        "type": "delivery",
    },
    "shipping_origin": {
        "warehouse_code": "401"
    },
    "shipping_destination": {
        "customer": {
            "name": "Bernardita Tapia Riquelme",
            "email": "b.tapia@outlook.com",
            "phone": "977623070",
        },
        "delivery_address": {
            "home_address": {
                "place": "Puente Alto",
                "full_address": "SAN HUGO 01324, Puente Alto, Puente Alto",
            }
        },
    },
    "carrier": {
        "carrier_code": "",
        "tracking_number": ""
    },
}

log_post_delivery(body)
