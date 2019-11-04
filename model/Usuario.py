class Usuario(object):

    def __init__(self, nombreU, contrasena):
        self.__nombreU = nombreU
        self.__contrasena = contrasena

    def get_nombreU(self):
        return self.__nombreU

    def set_nombreU(self, nombreU):
        self.__nombreU = nombreU
    
    def get_contrasena(self):
        return self.__contrasena

    def set_contrasena(self, contrasena):
        self.__contrasena = contrasena

    def m_datos(self):
        print(self.__nombreU)
        print(self.__contrasena)



