from datetime import date

class Pregunta(object):
	def __init__(self, nombreAsig, nuevoNiv, nuevoTiempo, nuevoTipo, nuevoCont, nuevaFecha, nuevaUnidad, nuevaSolucion):
		self.__nivTax = nuevoNiv
		self.__tiempoRes = nuevoTiempo
		self.__tipo = nuevoTipo
		self.__contenido = nuevoCont
		self.__fecha = nuevaFecha
		self.__unidad = nuevaUnidad
		self.__solucion = nuevaSolucion
		self.__nombreAsig = nombreAsig

	def get_nivel(self):
		return self.__nivTax

	def set_nivel(self, nuevoNiv):
		self.__nivTax = nuevoNiv

	def get_tiempo(self):
		return self.__tiempoRes

	def set_tiempo(self, nuevoTiempo):
		self.__tiempo_res = nuevoTiempo

	def get_tipo(self):
		return self.__tipo

	def set_tipo(self, nuevoTipo):
		self.__tipo = nuevoTipo

	def get_contenido(self):
		return self.__contenido

	def set_contenido(self, nuevoCont):
		self.__contenido = nuevoCont

	def get_fecha(self):
		return self.__fecha

	def set_fecha(self, nuevaFecha):
		self.__fecha = nuevaFecha

	def get_unidad(self):
		return self.__unidad

	def set_unidad(self, nuevaUnidad):
		self.__unidad = nuevaUnidad

	def get_solucion(self):
		return self.__solucion

	def set_solucion(self, nuevaSolucion):
		self.__solucion = nuevaSolucion

	def get_nombreAsig(self):
		return self.__nombreAsig

	def set_nombreAsig(self, nombreAsig):
		self.__nombreAsig = nombreAsig

	def mostrardatos(self):
		print(self.__nivTax)
		print(self.__tiempoRes)
		print(self.__tipo)
		print(self.__contenido)
		print(self.__fecha)
		print(self.__unidad)
		print(self.__nombreAsig)


