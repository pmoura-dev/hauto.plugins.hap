import actions
from pyhap.accessory import Accessory
from pyhap.accessory_driver import AccessoryDriver

import state


class LightBulb(Accessory):

    def __init__(self, driver: AccessoryDriver, device_id: int, device_name: str) -> None:
        super().__init__(driver, device_name)
        self.device_id = device_id

        service = self.add_preload_service('Lightbulb')
        self.char_on = service.configure_char('On', getter_callback=self.get_state, setter_callback=self.switch)

    def get_state(self) -> bool:
        current_state = state.get_state(self.device_id)
        return current_state["state"]["status"] == "online"

    def switch(self, value: bool) -> None:
        if value:
            actions.turn_on(self.device_id)
        else:
            actions.turn_off(self.device_id)
