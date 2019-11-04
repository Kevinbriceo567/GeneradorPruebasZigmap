class Asignatura(object):
	def __init__(self, nuevoNombreA, nuevoId):
		self.__nombreA = nuevoNombreA
		self.__id = nuevoId

	def get_nombreA(self):
		return self.__nombreA

	def set_nombreA(self, nuevoNombreA):
		self.__nombreA = nuevoNombreA

	def get_id(self):
		return self.__id

	def set_id(self, nuevoId):
		self.__id = nuevoId

	def mostrar_datos(self):
		print(self.__nombre)
		print(self.__id)