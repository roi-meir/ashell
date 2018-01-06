#!/usr/bin/env python
import argparse
import os
import subprocess
import sys

import pexpect

LOCAL_ADBRC_PATH = os.path.expanduser("~/.adbrc")
DEVICE_ADBRC_PATH = "/data/local/tmp/.adbrc"
DEFAULT_ADBRC_PATH = os.path.join(os.path.dirname(__file__), 'adbrc')

class AdbPushError(Exception):
    pass


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', dest='serial',
                        help='directs command to the device or emulator with the given serial number or qualifier.'
                             ' Overrides ANDROID_SERIAL environment variable')
    parser.add_argument('--print-default', help='print the default adbrc', action='store_true')
    return parser.parse_args()


def push_adbrc_to_device(child, serial=None):
    if not os.path.exists(LOCAL_ADBRC_PATH):
        return

    try:
        if serial:
            serial_args = ['-s', serial]
        else:
            serial_args = []

        subprocess.check_call(['adb'] + serial_args + ["push", LOCAL_ADBRC_PATH, DEVICE_ADBRC_PATH],
                              stdout=subprocess.PIPE)
        # load adbrc
        child.send(". {adbrc_path};\r".format(adbrc_path=DEVICE_ADBRC_PATH))

    except subprocess.CalledProcessError as e:
        raise AdbPushError(e)


def print_default():
    with open(DEFAULT_ADBRC_PATH, 'rb') as f:
        print(f.read())


def main():
    args = parse_args()

    if args.print_default:
        print_default()
        return

    adb_args = ["shell"]
    if args.serial:
        adb_args = ['-s', args.serial] + adb_args

    child = pexpect.spawn('adb', adb_args, echo=True)
    child.expect(['$', '#'])
    push_adbrc_to_device(child)
    child.interact()


if __name__ == '__main__':
    sys.exit(main())
