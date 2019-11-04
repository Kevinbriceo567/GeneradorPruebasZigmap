class Curso():

    __cod = 0

    def __init__(self, cod):
        self.__cod = cod

    def get_cod(self):
        return self.__cod

    def set_cod(self, cod):
        self.__cod = cod

    def mostrarDatos(self):
        print(self.__cod)
