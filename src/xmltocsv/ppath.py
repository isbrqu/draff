import os

class PPath(object):
    
    def __init__(self, root=None, ext_input=None, ext_output=None, exist_ok=False, 
        delete=None):
        self.root = f'{root}/' if root else None
        self.ext_input = ext_input
        self.ext_output = ext_output
        self.exist_ok = exist_ok
        self.__delete = delete.copy()
        self.__change_folder_input = True
        self.__folder_input = None
        self.__folder_output = None

    @property
    def folder_output(self):
        self.__update_folder_output()
        path = f'{self.root}{self.__folder_output}'
        return path

    @property
    def folder_input(self):
        return self.__folder_input

    @folder_input.setter
    def folder_input(self, value):
        self.__change_folder_input = True
        self.__folder_input = f'{value}/'

    @property
    def file_input(self):
        ext = f'.{self.ext_input}' if self.ext_input else ''
        return f'{self.folder_input}{self.filename}{ext}'

    @property
    def file_output(self):
        ext = f'.{self.ext_output}' if self.ext_output else ''
        return f'{self.folder_output}{self.filename}{ext}'

    @property
    def delete(self):
        return self.__delete.copy()

    @delete.setter
    def delete(self, value):
        self.__delete = value.copy()

    def mkdir_folder_output(self, exist_ok=None):
        if exist_ok == None:
            exist_ok = self.exist_ok
        os.makedirs(name=self.folder_output, exist_ok=exist_ok)

    def __update_folder_output(self):
        if not self.__folder_output or self.__change_folder_input:
            self.__change_folder_input = False
            folder = self.__folder_input
            for d in self.__delete:
                folder = folder.replace(f'{d}/', '', 1)
            self.__folder_output = folder

