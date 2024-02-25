import signal

from pyhap.accessory import Bridge
from pyhap.accessory_driver import AccessoryDriver

from accessories.air_conditioner import AirConditioner
from accessories.light_bulb import LightBulb
from accessories.television import Television


# todo: get devices from database

def get_bridge(driver):
    bridge = Bridge(driver, 'Bridge')
    bridge.add_accessory(AirConditioner(driver, 1, 'Ar Condicionado - Sala'))
    bridge.add_accessory(AirConditioner(driver, 2, 'Ar Condicionado - Escritório'))
    bridge.add_accessory(LightBulb(driver, 3, 'Luz RGB'))
    #bridge.add_accessory(Television(driver, 4, 'Television'))

    return bridge


driver = AccessoryDriver(port=51826, persist_file='pmsa.state')
driver.add_accessory(accessory=get_bridge(driver))
signal.signal(signal.SIGTERM, driver.signal_handler)
driver.start()
