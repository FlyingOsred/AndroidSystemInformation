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

import logging
import subprocess


class AdbCommand(object):
    DEFAULT_TIMEOUT = 30

    COMMAND_START_SERVER = "start-server"

    COMMAND_WAIT_FOR_DEVICE = "wait-for-device"

    COMMAND_DEVICES = "devices"

    COMMAND_ROOT = "root"

    SHELL_COMMAND_GET_PROP = "getprop"

    SHELL_COMMAND_CAT = "cat"

    SHELL_COMMAND_DUMPSYS = "dumpsys"

    def __init__(self, adb_path='adb', serial=None):
        self.logger = logging.getLogger(__name__)
        self.adb_path = adb_path
        self.serial = serial

    def __exec(self, *commands, is_shell=False, timeout=None):
        self.logger.info("handling command [%s] shell %s timeout %s" % (commands, is_shell, timeout))
        adb_cmd = self.__combine_command(*commands, is_shell=is_shell)
        self.logger.debug("adb_cmd is  %s" % adb_cmd)
        try:
            output = subprocess.check_output(adb_cmd, stderr=subprocess.STDOUT, timeout=timeout)
        except subprocess.TimeoutExpired:
            self.logger.warning("Timeout handling %s" % adb_cmd)
            return None
        self.logger.debug("output is %s " % output)
        return output

    def exec(self, *commands, timeout=None, is_shell=False):
        return self.__exec(*commands, timeout=timeout, is_shell=is_shell)

    def shell(self, *commands):
        return self.__exec(*commands, is_shell=True)

    def __combine_command(self, *cmds, is_shell=False):
        adb_cmd = self.adb_path
        if self.serial is not None:
            adb_cmd += " -s " + self.serial
        if is_shell is True:
            adb_cmd += " shell"
        for cmd in cmds:
            self.logger.debug("cmd is %s" % cmd)
            adb_cmd += " " + cmd
        return adb_cmd
