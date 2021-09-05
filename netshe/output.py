#! python3

import re

class Output(object):
    """maneja las expresiones regulares para la extraccion de los datos demandados"""
    def __init__(self, text, criterion):
        self.text = text
        self.criterion = criterion
        self.subs = []

    # return List of Strings
    def extracta(self, text):
        """extrae el grupo definido en el patron apartir del la salida del comando"""
        pattern = re.compile(self.criterion.format(text=text))
        results = pattern.findall(self.text)
        return results

    # return String
    def extractu(self, text):
        """retorna el primer elemento de la lista"""
        results = self.extracta(text)
        result = results[0] if results else ''
        return result

    def generate_subs(self, separator, criterion):
        """genera los subs apartir de un separador"""
        pattern = re.compile(separator)
        outputs = pattern.findall(self.text)
        self.subs = [Output(output, criterion) for output in outputs]
