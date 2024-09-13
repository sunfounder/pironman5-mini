import json
import time
import os
from pkg_resources import resource_filename

from pm_auto.pm_auto import PMAuto
from pm_dashboard.pm_dashboard import PMDashboard
from .logger import create_get_child_logger
from .utils import merge_dict, log_error
from .__version__ import __version__

get_child_logger = create_get_child_logger('pironman5-mini')
__package_name__ = __name__.split('.')[0]
CONFIG_PATH = resource_filename(__package_name__, 'config.json')

PERIPHERALS = [
    "storage",
    "cpu",
    "network",
    "memory",
    "history",
    "log",
    "ws2812",
    "temperature_unit",
    "pwm_fan_speed",
    "gpio_fan_state",
    "gpio_fan_mode",
    "gpio_fan_led",
]
DEVICE_INFO = {
    'name': 'Pironman Mini',
    'id': 'pironman5-mini',
    'peripherals': PERIPHERALS,
    'version': __version__,
}
AUTO_DEFAULT_CONFIG = {
    'temperature_unit': 'C',
    'rgb_led_count': 4,
    'rgb_enable': True,
    'rgb_color': '#ff00ff',
    'rgb_brightness': 100,
    'rgb_style': 'rainbow',
    'rgb_speed': 0,
    'gpio_fan_pin': 6,
}
DASHBOARD_SETTINGS = {
    "database": "pironman5-mini",
    "interval": 1,
    "spc": False,
}

class Pironman5Mini:
    @log_error
    def __init__(self):
        self.log = get_child_logger('main')
        self.config = {
            'system': AUTO_DEFAULT_CONFIG,
        }
        if not os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, 'w') as f:
                json.dump(self.config, f, indent=4)
        else:
            with open(CONFIG_PATH, 'r') as f:
                config = json.load(f)
            merge_dict(self.config, config)

        self.pm_auto = PMAuto(self.config['system'],
                              peripherals=PERIPHERALS,
                              get_logger=get_child_logger)
        self.pm_dashboard = PMDashboard(device_info=DEVICE_INFO,
                                        settings=DASHBOARD_SETTINGS,
                                        config=self.config,
                                        peripherals=PERIPHERALS,
                                        get_logger=get_child_logger)
        self.pm_auto.set_on_state_changed(self.pm_dashboard.update_status)
        self.pm_dashboard.set_on_config_changed(self.update_config)

    @log_error
    def set_debug_level(self, level):
        self.log.setLevel(level)
        self.pm_auto.set_debug_level(level)
        self.pm_dashboard.set_debug_level(level)

    @log_error
    def update_config(self, config):
        self.pm_auto.update_config(config['system'])
        merge_dict(self.config, config)
        with open(CONFIG_PATH, 'w') as f:
            json.dump(self.config, f, indent=4)

    @log_error
    @staticmethod
    def update_config_file(config):
        current = None
        with open(CONFIG_PATH, 'r') as f:
            current = json.load(f)
        merge_dict(current, config)
        with open(CONFIG_PATH, 'w') as f:
            json.dump(current, f, indent=4)

    @log_error
    def start(self):
        self.pm_auto.start()
        self.log.info('PMAuto started')
        self.pm_dashboard.start()
        self.log.info('PmDashboard started')
        while True:
            time.sleep(1)

    @log_error
    def stop(self):
        self.pm_auto.stop()
        self.pm_dashboard.stop()
