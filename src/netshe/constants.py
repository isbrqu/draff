#! python3

CODING = '865'
RE_CRITERION = r'\s+{text}\s+: ([^\r\n]+)\r\n'
RE_INTERFACE_SEPARATOR = r'((?:[-:% \.\(\)\w]+\r\n)+[-:% \.\(\)\w]+)\r\n\r\n'

# palabras claves de INTERFAZ en espaniol
WKISPA = {
	'name': 'Nombre',
	'description': 'Descripción',
	'guid': 'GUID',
	'mac': 'Dirección física'
}

# palabras claves de PERFIL en espaniol
WKPSPA = {
	'type_network': 'Tipo de red',
	'connection_mode': 'Modo de conexión',
	'authentication': 'Autenticación',
	'encryption': 'Cifrado',
	'presence_password': 'Clave de seguridad',
    'password': 'Contenido de la clave'
}

# estructura de interfaz
SINTERFACE = {
    'name': '',
    'description': '',
    'guid': '',
    'mac': '',
    'profiles': []
}

# estructura de perfil
SPROFILE = {
    'name': '',
    'type_network': '',
    'connection_mode': '',
    'authentication': '',
    'encryption': '',
    'presence_password': '',
    'password': ''
}
