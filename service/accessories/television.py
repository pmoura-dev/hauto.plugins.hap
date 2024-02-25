from pyhap.accessory import Accessory
from pyhap.accessory_driver import AccessoryDriver


class Television(Accessory):

    def __init__(self, driver: AccessoryDriver, device_id: int, device_name: str) -> None:
        super().__init__(driver, device_name)
        self.device_id = device_id

        service = self.add_preload_service(
            'Television'
        )

        self.char_active = service.configure_char('Active', setter_callback=self.switch)
        self.char_active_identifier = service.configure_char('ActiveIdentifier', value=123)
        self.char_configured_name = service.configure_char('ConfiguredName', value='Samsung TV')
        self.char_sleep_discovery_mode = service.configure_char('SleepDiscoveryMode', value=1)

    def switch(self, value: int) -> None:
        if value:
            print("TV on")
        else:
            print("TV off")
