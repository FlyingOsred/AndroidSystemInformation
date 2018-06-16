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

from adb.command import AdbCommand


class AdbDevice(object):
    def __init__(self, serial_no, adb_path):
        self.serial_no = serial_no
        self.adb_path = adb_path
        self.commander = AdbCommand(adb_path)

    def get_serialno(self):
        return self.serial_no

    def cat(self, path):
        if path is not None:
            return self.commander.shell("cat", path)
        return None
