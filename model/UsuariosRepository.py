from model.Usuario import *

class UsuariosRepository(object):

    def get_usuarios(self):

        usuarioAdmin1 = Usuario("admin1", "admin1")
        usuarioAdmin2 = Usuario("admin2", "admin2")

        listaUsuarios = [usuarioAdmin1, usuarioAdmin2]

        return listaUsuarios
