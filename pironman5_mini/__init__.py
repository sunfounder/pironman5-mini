from .version import __version__

TRUE_LIST = ['true', 'True', 'TRUE', '1', 'on', 'On', 'ON']
FALSE_LIST = ['false', 'False', 'FALSE', '0', 'off', 'Off', 'OFF']

def main():
    import argparse
    from .pironman5_mini import Pironman5Mini
    from pm_auto.ws2812 import RGB_STYLES
    from pm_auto.fan_control import GPIO_FAN_MODES
    from pkg_resources import resource_filename
    import json
    import sys
    from os import path

    CONFIG_PATH = resource_filename('pironman5_mini', 'config.json')

    current_config = None
    new_auto = {}

    parser = argparse.ArgumentParser(description='Pironman Mini')
    parser.add_argument("command",
                        choices=["start", "stop"],
                        nargs="?",
                        help="Command")
    parser.add_argument("-v", "--version", action="store_true", help="Show version")
    parser.add_argument("-c", "--config", action="store_true", help="Show config")
    parser.add_argument("-rc", "--rgb-color", nargs='?', default='', help='RGB color in hex format without # (e.g. 00aabb)')
    parser.add_argument("-rb", "--rgb-brightness", nargs='?', default='', help="RGB brightness 0-100")
    parser.add_argument("-rs", "--rgb-style", choices=RGB_STYLES, nargs='?', default='', help="RGB style")
    parser.add_argument("-rp", "--rgb-speed", nargs='?', default='', help="RGB speed 0-100")
    parser.add_argument("-re", "--rgb-enable", nargs='?', default='', help="RGB enable True/False")
    parser.add_argument("-rl", "--rgb-led-count", nargs='?', default='', help="RGB LED count int")
    parser.add_argument("-u", "--temperature-unit", choices=["C", "F"], nargs='?', default='', help="Temperature unit")
    parser.add_argument("-gm", "--gpio-fan-mode", nargs='?', default='', help=f"GPIO fan mode, {', '.join([f'{i}: {mode}' for i, mode in enumerate(GPIO_FAN_MODES)])}")
    parser.add_argument("-gp", "--gpio-fan-pin", nargs='?', default='', help="GPIO fan pin")
    parser.add_argument("--background", nargs='?', default='', help="Run in background")

    args = parser.parse_args()

    if not (len(sys.argv) > 1):
        parser.print_help()
        quit()
    
    if not path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, 'w') as f:
            json.dump({'auto': {}}, f, indent=4)
    else:
        with open(CONFIG_PATH, 'r') as f:
            current_config = json.load(f)

    if args.config:
        print(json.dumps(current_config, indent=4))
        quit()

    if args.command == "stop":
        import os
        os.system('kill -9 $(pgrep -f "pironman5-mini start")')
        os.system('kill -9 $(pgrep -f "pironman5-mini-service start")')
        pironman5_mini = Pironman5Mini()
        pironman5_mini.stop()
        quit()

    if args.version:
        print(__version__)
        quit()
    if args.rgb_color != '':
        if args.rgb_color == None:
            hex = current_config['system']['rgb_color']
            if hex[0] == '#':
                hex = hex[1:]
            r = int(hex[0:2], 16)
            g = int(hex[2:4], 16)
            b = int(hex[4:6], 16)
            print(f"RGB color: #{hex} ({r}, {g}, {b})")
        else:
            if len(args.rgb_color) != 6:
                print(f'Invalid value for RGB color, it should be in hex format without # (e.g. 00aabb)')
                quit()
            if len(args.rgb_color) == 6:
                try:
                    r = int(args.rgb_color[0:2], 16)
                    g = int(args.rgb_color[2:4], 16)
                    b = int(args.rgb_color[4:6], 16)
                except ValueError:
                    print(f'Invalid value for RGB color, it should be in hex format without # (e.g. 00aabb)')
                    quit()
            new_auto['rgb_color'] = args.rgb_color
    if args.rgb_brightness != '':
        if args.rgb_brightness == None:
            print(f"RGB brightness: {current_config['system']['rgb_brightness']}")
        else:
            try:
                args.rgb_brightness = int(args.rgb_brightness)
            except ValueError:
                print(f"Invalid value for RGB brightness, it should be an integer between 0 and 100")
                quit()
            if args.rgb_brightness < 0 or args.rgb_brightness > 100:
                print(f"Invalid value for RGB brightness, it should be between 0 and 100")
                quit()
            new_auto['rgb_brightness'] = args.rgb_brightness
    if args.rgb_style != '':
        if args.rgb_style == None:
            print(f"RGB style: {current_config['system']['rgb_style']}")
        else:
            if args.rgb_style not in RGB_STYLES:
                print(f"Invalid value for RGB style, it should be one of {RGB_STYLES}")
                quit()
            new_auto['rgb_style'] = args.rgb_style
    if args.rgb_speed != '':
        if args.rgb_speed == None:
            print(f"RGB speed: {current_config['system']['rgb_speed']}")
        else:
            try:
                args.rgb_speed = int(args.rgb_speed)
            except ValueError:
                print(f"Invalid value for RGB speed, it should be an integer between 0 and 100")
                quit()
            if args.rgb_speed < 0 or args.rgb_speed > 100:
                print(f"Invalid value for RGB speed, it should be between 0 and 100")
                quit()
            new_auto['rgb_speed'] = args.rgb_speed
    if args.rgb_enable != '':
        if args.rgb_enable == None:
            print(f"RGB enable: {current_config['system']['rgb_enable']}")
        else:
            if args.rgb_enable in TRUE_LIST:
                new_auto['rgb_enable'] = True
            elif args.rgb_enable in FALSE_LIST:
                new_auto['rgb_enable'] = False
            else:
                print(f"Invalid value for RGB enable, it should be True or False")
                quit()
    if args.rgb_led_count != '':
        if args.rgb_led_count == None:
            print(f"RGB LED count: {current_config['system']['rgb_led_count']}")
        else:
            try:
                args.rgb_led_count = int(args.rgb_led_count)
            except ValueError:
                print(f"Invalid value for RGB LED count, it should be an integer greater than 0")
                quit()
            if args.rgb_led_count < 1:
                print(f"Invalid value for RGB LED count, it should be greater than 0")
                quit()
            new_auto['rgb_led_count'] = args.rgb_led_count
    if args.temperature_unit != '':
        if args.temperature_unit == None:
            print(f"Temperature unit: {current_config['system']['temperature_unit']}")
        else:
            if args.temperature_unit not in ['C', 'F']:
                print(f"Invalid value for Temperature unit, it should be C or F")
                quit()
            new_auto['temperature_unit'] = args.temperature_unit
    if args.gpio_fan_mode != '':
        if args.gpio_fan_mode == None:
            print(f"GPIO fan mode: {current_config['system']['gpio_fan_mode']}")
        else:
            try:
                args.gpio_fan_mode = int(args.gpio_fan_mode)
            except ValueError:
                print(f"Invalid value for GPIO fan mode, it should be an integer between 0 and {len(GPIO_FAN_MODES) - 1}, {', '.join([f'{i}: {mode}' for i, mode in enumerate(GPIO_FAN_MODES)])}")
                quit()
            if args.gpio_fan_mode < 0 or args.gpio_fan_mode >= len(GPIO_FAN_MODES):
                print(f"Invalid value for GPIO fan mode, it should be between 0 and {len(GPIO_FAN_MODES) - 1}, {', '.join([f'{i}: {mode}' for i, mode in enumerate(GPIO_FAN_MODES)])}")
                quit()
            new_auto['gpio_fan_mode'] = args.gpio_fan_mode
    if args.gpio_fan_pin != '':
        if args.gpio_fan_pin == None:
            print(f"GPIO fan pin: {current_config['system']['gpio_fan_pin']}")
        else:
            try:
                args.gpio_fan_pin = int(args.gpio_fan_pin)
            except ValueError:
                print(f"Invalid value for GPIO fan pin, it should be an integer")
                quit()
            new_auto['gpio_fan_pin'] = args.gpio_fan_pin
    if args.background != '':
        print("This is a placeholder for pironman5 binary help, you should run pironman5 instead")
        quit()

    new_config = {
        'system': new_auto,
    }

    Pironman5Mini.update_config_file(new_config)
    if args.command == "start":
        pironman5_mini = Pironman5Mini()
        pironman5_mini.start()