import requests

from config import API_GATEWAY_HOST, API_GATEWAY_PORT

base_url = f"http://{API_GATEWAY_HOST}:{API_GATEWAY_PORT}"


def turn_on(device_id: int) -> None:
    """Turn device on."""
    requests.post(base_url + f"/devices/{device_id}/action/turn_on")


def turn_off(device_id: int) -> None:
    """Turn device off."""
    requests.post(base_url + f"/devices/{device_id}/action/turn_off")


def set_heater_cooler_mode(device_id: int, mode: str) -> None:
    """Set heater/cooler mode."""
    requests.post(base_url + f"/devices/{device_id}/action/set_heater_cooler_mode",
                  json={"mode": mode})


def set_heating_threshold_temperature(device_id: int, value: int) -> None:
    """Set heating temperature."""
    requests.post(base_url + f"/devices/{device_id}/action/set_heating_threshold_temperature",
                  json={"value": value})


def set_cooling_threshold_temperature(device_id: int, value: int) -> None:
    """Set cooling temperature."""
    requests.post(base_url + f"/devices/{device_id}/action/set_cooling_threshold_temperature",
                  json={"value": value})
