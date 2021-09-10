# from re import sub
import re
from re import RegexFlag
from glob import iglob
from pprint import pprint
from pandas import DataFrame
from pandas import concat
from datetime import datetime

def extract_data_pdfs(regex):
    for item in iglob('output/*.txt'):
        with open(item) as txt:
            text = txt.read()
            text = re.sub(r'\n+', '\n', text)
            text = re.sub(r'^ *', '', text, flags=re.RegexFlag.MULTILINE)
            text = re.sub(r' +', ' ', text)
            data = re.search(regex, text).groupdict()
        dataframe = DataFrame.from_records([data])
        yield dataframe

regex = (
    'Comprobante de Transferencia\n'
    'Tipo de Transferencia: *(?P<type_transference>.*)\n'
    'Fecha y Hora: *(?P<datetime>.*)\n'
    'Importe: *(?P<amount>.*)\n'
    'Cuenta Origen: *(?P<origin_account>.*)\n'
    'Nombre Originante: *(?P<origin_name>.*)\n'
    'Documento Originante: *(?P<origin_dni>.*)\n'
    'Banco Destino: *(?P<dest_bank>.*)\n'
    'Tipo de Cuenta Destino: *(?P<dest_type_account>.*)\n'
    'Cuenta Destino: *(?P<dest_account>.*)\n'
    'Nombre Destinatario: *(?P<dest_name>.*)\n'
    'CUIT/CUIL/CDI/DNI *(?P<dest_cuit_cuil_cdi_dni>.*)\n'
    'Referencia: *(?P<reference>.*)\n'
    'Motivo: *(?P<motive>.*)\n'
    'Número de Transacción: *(?P<number_transaction>.*)\n'
    'Canal: *(?P<channel>.*)\n'
)
generator = (data for data in extract_data_pdfs(regex))
dataframe = concat(generator, ignore_index=True) 
now = datetime.now().strftime('%d-%m-%y-%H-%M-%S')
name = f'transferences-{now}.csv'
dataframe.to_csv(name)

