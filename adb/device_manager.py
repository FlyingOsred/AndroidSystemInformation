# Copyright (C) 2018 osred.brockhoist@hotmail.com

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import re
import sys

from adb.device import AdbDevice
from adb.command import AdbCommand
from utils.string import String


class MultipleDeviceError(RuntimeError):
    def __init__(self):
        super(MultipleDeviceError, self).__init__('Multiple device found')


class NoDeviceError(RuntimeError):
    def __init__(self):
        super(NoDeviceError, self).__init__('No device found')


def __get_adb_path__(bin_path=None):
    if bin_path is not None and sys.platform.startswith('win32'):
        adb_path = os.path.join(bin_path, "windows", "adb.exe")
    else:
        adb_path = "adb"
    return adb_path


def get_device(bin_path=None):
    adb_path = __get_adb_path__(bin_path)
    commander = AdbCommand(adb_path)
    commander.exec(AdbCommand.COMMAND_START_SERVER)
    commander.exec(AdbCommand.COMMAND_WAIT_FOR_DEVICE, timeout=AdbCommand.DEFAULT_TIMEOUT)
    output = String(commander.exec(AdbCommand.COMMAND_DEVICES).decode('utf-8').strip()).split_lines()
    devices = []
    for line in output[1:]:
        if 'device' not in line:
            continue

        serial, _ = re.split(r'\s+', line, maxsplit=1)
        devices.append(serial)

    if len(devices) <= 0:
        raise NoDeviceError()
    if len(devices) != 1:
        raise MultipleDeviceError()

    return AdbDevice(devices[0], adb_path)
