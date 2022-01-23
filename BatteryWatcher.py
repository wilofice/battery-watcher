#!/usr/bin/env python3

import subprocess

class BatteryWatcher:
    info: str
    battery_state: Dict[str, str]

    def __init__(self):
        self.battery_state = []
        self.info = self.get_info()
        

    def get_info(self):
        command = "acpi -b"
        return subprocess.check_output(command, stderr=subprocess.PIPE, shell=True)



