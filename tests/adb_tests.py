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

from adb import device_manager
from adb.device_manager import NoDeviceError
from adb.device_manager import MultipleDeviceError

if __name__ == "__main__":
    print('Adb tests begin ...')
    cwd = os.getcwd()
    root = os.path.abspath(os.path.join(cwd, os.pardir))
    bin_path = os.path.join(root, "bin")
    print("Current working dir is %s" % bin_path)
    try:
        device_manager.get_device(bin_path)
    except NoDeviceError:
        print("No device found")
    except MultipleDeviceError:
        print("Multiple devices found, only one device is allowed")
    print('Adb tests end ...')
