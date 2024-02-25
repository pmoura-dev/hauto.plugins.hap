import requests

from config import API_GATEWAY_HOST, API_GATEWAY_PORT

base_url = f"http://{API_GATEWAY_HOST}:{API_GATEWAY_PORT}"


def get_state(device_id: int) -> dict:
    """Get device state"""
    response = requests.get(base_url + f"/devices/{device_id}/state")
    return response.json()
