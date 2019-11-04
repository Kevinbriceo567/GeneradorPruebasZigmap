class Carrera():

    __nombre = ""
    __facultad = ""

    def __init__(self, nombre, facultad):

        self.__nombre = nombre
        self.__facultad = facultad

    def get_nombre(self):
        return self.__nombre

    def get_facultad(self):
        return self.__facultad

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_facultad(self, facultad):
        self.__facultad = facultad