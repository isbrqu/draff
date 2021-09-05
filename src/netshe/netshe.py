#! python3

import json
import subprocess
from secrets import token_hex

# estructuras
from constants import SINTERFACE
from constants import SPROFILE

# expresiones regulares
from constants import RE_CRITERION
from constants import RE_INTERFACE_SEPARATOR

# constantes idiomaticas
from constants import WKISPA
from constants import WKPSPA

from command import Command

# asigna de forma dinamica los valores segun con conjunto de llaves
def asingdicts(dict1, dict2, obj):
    for key in dict2.keys():
        dict1[key] = obj.extractu(dict2[key])

# crea una lista de clones de un diccionario
createdicts = lambda dct, lst: [dct.copy() for _ in range(len(lst))]

# ejecuta los comandos y decodifica y empaqueta la salida en un objeto Output
command = Command()

if __name__ == '__main__':
    # contruye las instancias de las interfaces
    output = command.show_interfaces()
    output.generate_subs(RE_INTERFACE_SEPARATOR, RE_CRITERION)
    # crea tantos diccionarios como numeros de interfaces sean
    interfaces = createdicts(SINTERFACE, output.subs)
    for interface, output in zip(interfaces, output.subs):
        asingdicts(interface, WKISPA, output)
        output = command.show_profiles(interface['name'])
        names = output.extracta('Perfil de todos los usuarios')
        # crea tantos diccionarios com numeros de perfiles sean
        profiles = createdicts(SPROFILE, names)
        for profile, pname in zip(profiles, names):
            profile['name'] = pname
            output = command.show_profile(interface['name'], pname)
            asingdicts(profile, WKPSPA, output)
        interface['profiles'] = profiles
    # conversiona a json todos los datos
    interfaces = json.dumps(interfaces, indent=4)
    # escribe en archivo lo empaquetado
    fname = f'netshe-{token_hex(8)}.json'
    with open(fname, 'w') as file:
        file.write(interfaces)
    # oculta el archivo
    # subprocess.run(['attrib', '+h', '+s', fname])
