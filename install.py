#!/usr/bin/env python3

from tools.sf_installer import SF_Installer

installer = SF_Installer(
    name='pironman-mini',
    friendly_name='Pironman Mini',

    # - Setup install command description if needed, default to "Installer for {friendly_name}""
    # description='Installer for Pironman Mini',

    # - Setup venv options if needed, default to []
    venv_options=[
        '--system-site-packages',
    ],

    # - Setup Work Dir if needed, default to /opt/{name}
    # work_dir='/opt/pironman-mini',

    # - Setup log dir if needed, default to /var/log/{name}
    # log_dir='/var/log/pironman-mini',

    # - Install from apt
    apt_dependencies=[
        'influxdb',
        'python3-gpiozero', # for pm_auto fan control
    ],

    # - Install from pip
    # pip_dependencies=[
    #     'influxdb',
    #     'Pillow',
    #     'adafruit-circuitpython-ssd1306',
    # ]

    # - Install python source code from git
    python_source={
        'pironman-mini': './',
        'pm_auto': 'git+http://github.com/sunfounder/pm_auto.git',
        'pm_dashboard': 'git+http://github.com/sunfounder/pm_dashboard.git',
        'sf_rpi_status': 'git+http://github.com/sunfounder/sf_rpi_status.git',
    },

    # - Setup config txt
    # config_txt = {
    #     'dtparam=spi': 'on',
    #     'dtparam=i2c_arm': 'on',
    #     'dtoverlay=gpio-ir,gpio_pin': '13',
    # },

    # add modules
    # sudo modprobe xxx
    # modules = [
    #     "i2c-dev",
    # ],

    # - Autostart settings
    # - Set service filenames
    service_files = ['pironman-mini.service'],
    # - Set bin files
    bin_files = ['pironman-mini'],

    # - Copy device tree overlay to /boot/overlays
    dtoverlay = ['sunfounder-pironmanmini.dtbo'],
)
installer.install()
