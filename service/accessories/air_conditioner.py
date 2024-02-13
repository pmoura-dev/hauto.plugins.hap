from pyhap.accessory import Accessory
from pyhap.accessory_driver import AccessoryDriver

import actions

AUTOMATIC_MODE = 0
HEATING_MODE = 1
COOLING_MODE = 2


class AirConditioner(Accessory):

    def __init__(self, driver: AccessoryDriver, device_id: int, device_name: str) -> None:
        super().__init__(driver, device_name)
        self.device_id = device_id

        service = self.add_preload_service(
            'HeaterCooler',
            chars=['CoolingThresholdTemperature', 'HeatingThresholdTemperature']
        )

        self.char_active = service.configure_char('Active', setter_callback=self.switch)
        self.char_temp = service.configure_char('CurrentTemperature', value=-1)
        self.char_current_state = service.configure_char('CurrentHeaterCoolerState')
        self.char_target_state = service.configure_char('TargetHeaterCoolerState', setter_callback=self.set_mode)
        self.char_set_cooling_temperature = service.configure_char('CoolingThresholdTemperature',
                                                                   setter_callback=self.set_cooling_temperature)
        self.char_set_cooling_temperature.override_properties({'minStep': 1, 'minValue': 18})
        self.char_set_heating_temperature = service.configure_char('HeatingThresholdTemperature',
                                                                   setter_callback=self.set_heating_temperature)
        self.char_set_heating_temperature.override_properties({'minStep': 1, 'minValue': 20})

    def switch(self, value: bool) -> None:
        if value:
            actions.turn_on(self.device_id)
        else:
            actions.turn_off(self.device_id)

    def set_mode(self, mode: int) -> None:
        if mode == AUTOMATIC_MODE:
            actions.set_heater_cooler_mode(self.device_id, "automatic")
        elif mode == HEATING_MODE:
            actions.set_heater_cooler_mode(self.device_id, "heating")
        elif mode == COOLING_MODE:
            actions.set_heater_cooler_mode(self.device_id, "cooling")

    def set_heating_temperature(self, value: float) -> None:
        actions.set_heating_threshold_temperature(self.device_id, value=int(value))

    def set_cooling_temperature(self, value: float) -> None:
        actions.set_cooling_threshold_temperature(self.device_id, value=int(value))
