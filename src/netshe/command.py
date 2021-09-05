#! python3

import subprocess

from constants import RE_CRITERION
from constants import CODING
from output import Output

class Command(object):
    """Crea los comandos"""
    def __init__(self):
        command = []

    def show_interfaces(self):
        command = ['netsh', 'wlan', 'show', 'interface']
        return self.__execute(command)

    def show_profiles(self, interface):
        command = ['netsh', 'wlan', 'show', 'profiles', 'interface=', interface]
        return self.__execute(command)

    def show_profile(self, interface, profile):
        command = ['netsh', 'wlan', 'show', 'profile', profile, interface, 'clear']
        return self.__execute(command)

    # return Output
    def __execute(self, command):
        """ejecuta el comando, decodifica el resultado y crea un objeto Output"""
        try:
            output = subprocess.check_output(command, shell=True)
            output = output.decode(CODING)
            return Output(output, RE_CRITERION)
        except subprocess.CalledProcessError:
            return Output('', RE_CRITERION)
