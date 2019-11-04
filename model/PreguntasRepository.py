from model.Pregunta import *

class PreguntasRepository():

    def get_preguntas(self):

        preguntasRepo = [pregunta1, pregunta2, pregunta3, pregunta4, pregunta5, pregunta6, pregunta7, pregunta8, pregunta9, pregunta10, pregunta11, pregunta12, pregunta13, pregunta14, pregunta15, pregunta16, pregunta17, pregunta18, pregunta19, pregunta20, pregunta21, pregunta22, pregunta23, pregunta24, pregunta25]

        return preguntasRepo

# ASIGNATURA POR DEFECTO: PROGRAMACIÓN
# UNIDAD 1: PYTHON BÁSICO: (SINTAXIS, CONDICIONALES, CICLOS, COLECCIONES)
# UNIDAD 2: FUNCIONES, EXCEPCIONES, ARCHIVOS
# UNIDAD 3: POO

# REPOSITORIO DE PREGUNTAS #

# PREGUNTA 1

contenidoP1 = """Defina de forma clara lo que es una "Condicional", un "Ciclo" y una "Lista" en Python:"""

pregunta1 = Pregunta("Programación I", "Entender", 6, "COMPOSICIÓN", contenidoP1, date(1900,1, 3), "unidad1", "Condicional: if, elif, else - Ciclo: while, for - Lista: variedad de valores almacenados en una sola variable.")

# PREGUNTA 2

contenidoP2 = """a) Un espacio que se almacena en la memoria, similar a la función que cumple una neurona. Con esta definición nos referimos a una:

- 

b) Cadena de caracteres, palabras o frases ordenadas exceptuando a los números. Con esta definición nos referimos a un:

- 

c) Secuencia de instrucciones que representan un modelo de solución para determinado tipo de problemas. Con esta definición nos referimos a un:

- """

pregunta2 = Pregunta("Programación I", "Recordar", 5, "RESPUESTA CORTA", contenidoP2, date(1900,1, 3), "unidad1", "a) Variable - b)String - c)Algoritmo ")

# PREGUNTA3

contenidoP3 = """Dado el siguiente código, indique cual es la respuesta del programa: 

i = 1
while i <= 3:
    print(i)
    i += 1
print("Programa terminado")

- La respuesta del programa es: ______________"""

pregunta3 = Pregunta("Programación I", "Aplicar", 4, "TEXTO INCOMPLETO", contenidoP3, date(1900,1, 3), "unidad1", "1 2 3 Programa terminado")

# PREGUNTA 4

contenidoP4 = """

( ) Tipo de lista que no se puede modificar.          a)Lista.
( ) Permite agregar datos a una lista.                b)Tuplas.
( ) Caracter de tipo booleano.                        c)while.
( ) Permite mostrar datos en pantalla.                d)Print.
                                                      e)Append.
                                                      f)True y False."""

pregunta4 = Pregunta("Programación I", "Analizar", 5, "CORRESPONDENCIA O EMPAREJAMIENTO", contenidoP4, date(1900,1, 3), "unidad1", "a), e), f), d).")

# PREGUNTA 5

contenidoP5 = """Indique la alternativa correcta según la respuesta del siguiente programa en Python:

i = 1
while i <= 10:
    print(i, end=" ")

a) 9.
b) 10.
c) Error.
d) 1 1 1 1 1 1 1 1 1...
e) 1."""

pregunta5 = Pregunta("Programación I", "Evaluar", 4, "OPCIÓN MÚLTIPLE", contenidoP5, date(1900,1, 3), "unidad1", "d)")

# PREGUNTA 6

contenidoP6 = """Tienda ZIGMAP Play Store le solicita crear un programa donde pueda registrar clientes, artículos en venta y pedidos. Considerar los siguientes aspectos para crear el algoritmo: 

- Cada cliente debe tener nombre, rut y número de pedido asociado.

- Cada producto debe tener nombre, ID, número de pedido y precio.

El programa solicitado por ZIGMAP Play Store debe tener un menú para registrar cliente, registrar pedido, mostrar pedidos, mostrar productos y sus precios, además de modificar clientes y pedidos."""

pregunta6 = Pregunta("Programación I", "Crear", 20, "INTERPRETACIÓN", contenidoP6, date(1900,1, 3), "unidad1", "El estudiante logra crear el programa con los puntos solicitados anteriormente.")

# PREGUNTA 7

contenidoP7 = """Desarrolle una función en Python que permita calcular números primos hasta el máximo de entrada por el usuario:"""

pregunta7 = Pregunta("Programación I", "Recordar", 10, "ANALOGÍAS O DIFERENCIAS", contenidoP7, date(1900,1, 3), "unidad2", "Desarrollo del estudiante correctamente.")

# PREGUNTA 8

contenidoP8 = """Crear un programa en Python que pueda almacenar una lista de personas. Los datos de las personas debe llevar su Nombre, Apellido, Rut y Fecha de nacimiento. Una vez tenga la lista de personas, debe crear un archivo que almacene toda la lista de personas en orden."""

pregunta8 = Pregunta("Programación I", "Entender", 10, "INTERPRETACIÓN", contenidoP8, date(1900,1, 3), "unidad2", "Desarrollo del estudiante correctamente.")

# PREGUNTA 9

contenidoP9 = """Defina lo que es una función en Python y indique ejemplos de como utilizarlo en código. Se solicita utilizar correctamente la identación."""

pregunta9 = Pregunta("Programación I", "Aplicar", 8, "COMPOSICIÓN", contenidoP9, date(1900,1, 3), "unidad2", "Desarrollo del estudiante correctamente.")

# PREGUNTA 10

contenidoP10 = """a) Cuando utilizamos "def" en nuestro código de Python, hacemos referencia a utilizar una:

___________________________________________________

b) Al importar la librería "from tkinter import *", estamos haciendo clara referencia a:

___________________________________________________

c) Para que nos sirve la línea de código "archivo.write("Hola mundo")" en Python:

___________________________________________________"""

pregunta10 = Pregunta("Programación I", "Analizar", 5, "RESPUESTA CORTA", contenidoP10, date(1900,1, 3), "unidad2", "a) Función, b) Interfaz gráfica, c) Escribir un archivo")

# PREGUNTA 11

contenidoP11 = """Marque "V" (Verdadero) o "F" (Falso) según corresponda:

______ From datetime import date. Esta información es útil para desarrollar interfaz gráfica en Python.
______ La siguiente línea de código permite iniciar la creación de una función: "def funcion():".
______ La siguiente línea de código nos permite crear un archivo .txt en Python: "f = open ('holamundo.txt','w')".
______ La siguiente línea de código nos permite crear una función en Python: "Root = Tk()"."""

pregunta11 = Pregunta("Programación I", "Evaluar", 5, "VERDADERO Y FALSO", contenidoP11, date(1900,1, 3), "unidad2", "F, V, V, F")

# PREGUNTA 12

contenidoP12 = """Desarrolle un programa en Python con interfaz gráfica. El programa debe ser el juego del gato y debe tener una casilla de 6x6.while

La interfaz debe incluir el nombre de jugador 1 y 2. Además debe indicar cuando es el turno de cada jugador y una alerta del ganador."""

pregunta12 = Pregunta("Programación I", "Crear", 20, "INTERPRETACIÓN", contenidoP12, date(1900,1, 3), "unidad2", "Desarrollo correcto del estudiante.")

# PREGUNTA 13

contenidoP13 = """Mecanismo que consiste en organizar datos y métodos de una estructura, conciliando el modo en que el objeto se implementa, es decir, evitando el acceso a datos por cualquier otro medio distinto a los especificados.

Esta definición corresponde a:

a) Herencia.
b) Polimorfismo.
c) Encapsulamiento.
d) Ninguna de las anteriores."""

pregunta13 = Pregunta("Programación II", "Recordar", 4, "OPCIÓN MÚLTIPLE", contenidoP13, date(1900,1, 3), "unidad1", "c) Encapsulamiento")

# PREGUNTA 14

contenidoP14 = """Marque "V" (Verdadero) o "F" (Falso) según corresponda:

______ La herencia simple consiste en que una clase hereda unicamente de otra.
______ La relacion de herencia hace posible utilizar, desde la instancia, los atributos de la clase padre.
______ En Java, al definir una clase, indicaremos entre parentesis de la clase que hereda.
______ Los atributos de la clase padre pasan a ser heredados por la clase hija."""

pregunta14 = Pregunta("Programación II", "Entender", 4, "VERDADERO O FALSO", contenidoP14, date(1900,1, 3), "unidad2", "V V F V")

# PREGUNTA 15 

contenidoP15 = """Mencione cómo declarar en python que se recibirá en un input un número entero, un arreglo de caracteres y un número decimal, respectivamente"""

pregunta15 = Pregunta("Programación II", "Aplicar", 5, "ANALOGÍAS O DIFERENCIAS", contenidoP15, date(1900,1, 3), "unidad1", "int, str, float")

# PREGUNTA 16

contenidoP16 = """¿Por qué una clase padre es "padre" de una clase hija?"""

pregunta16 = Pregunta("Programación II", "Analizar", 5, "INTERPRETACIÓN", contenidoP16, date(1900,1, 3), "unidad2", "Debido a que la clase hija hereda atributos de la clase padre")

# PREGUNTA 17

contenidoP17 = """¿Cuál es la principal diferencia entre Java y Python?"""

pregunta17 = Pregunta("Programación II", "Evaluar", 5, "COMPOSICIÓN", contenidoP17, date(1900,1, 3), "unidad1", " Python se tipea dinámicamente mientras que Java está tipado estáticamente")

# PREGUNTA 18

contenidoP18 = """Con respecto al tipo de paradigma, Python es un lenguaje ______________ """

pregunta18 = Pregunta("Programación II", "Recordar", 4, "RESPUESTA CORTA", contenidoP18, date(1900,1, 3), "unidad2", "Multiparadigma")

# PREGUNTA 19

contenidoP19 = """Para declarar que se recibirá un valor entero en un input se utiliza: ______________"""

pregunta19 = Pregunta("Programación II", "Recordar", 4, "TEXTO INCOMPLETO", contenidoP19, date(1900,1, 3), "unidad1", "int")

# PREGUNTA 20

contenidoP20 = """Asigne cada letra según el ejemplo que le corresponde:
( ) Paradigma Imperativo                              a)Compoosiciones Bash
( ) Paradigma Funcional                               b)Scheme
( ) Paradigma Lógico                                  c)Prolog
( ) Paradigma Estructurado                            d)C                                           
                                                      f)Java"""

pregunta20 = Pregunta("Programación II", "Entender", 5, "CORRESPONDENCIA O EMPAREJAMIENTO", contenidoP20, date(1900,1, 3), "unidad2", "d) a) b) c) f)")

# PREGUNTA 21

contenidoP21 = """ Marque la afirmación correcta:

a) La funcion str() devuelve representaciones de los valores que son bastante legibles por humanos.
b) La funcion str() hace que se puedan hacer operaciones aritméticas con dos números
c) La función str() no existe
d) La función str() añade elementos a una lista"""

pregunta21 = Pregunta("Programación II", "Aplicar", 4, "OPCIÓN MÚLTIPLE", contenidoP21, date(1900,1, 3), "unidad1", "a")

# PREGUNTA 22

contenidoP22 = """El valor asociado a la llave k en el diccionario d se puede obtener mediante d[k]."""

pregunta22 = Pregunta("Programación II", "Analizar", 4, "VERDADERO O FALSO", contenidoP22, date(1900,1, 3), "unidad1", "Verdadero")

# PREGUNTA 23

contenidoP23 = """Mencione los signos de agrupación usados en python para declarar una tupla, una lista y un diccionario, respectivamente"""

pregunta23 = Pregunta("Programación II", "Evaluar", 5, "ANALOGÍAS O DIFERENCIAS", contenidoP23, date(1900,1, 3), "unidad1", "para una tupla(),para una lista [], para un diccionario{}")

# PREGUNTA 24

contenidoP24 = """Una empresa llamada YaTuSae necesita desarrollar un sistema que registre a todas las personas que se inscriben en una asociacion. De cada persona interesa saber sus datos basicos: RUN, nombre completo y fecha de nacimiento. Cuando cada nuevo socio se inscribe, se le asigna un codigo de asociado, y se anota la fecha de inscripción. Realice el diagrama de clases asociado al problema."""

pregunta24 = Pregunta("Programación II", "Crear", 15, "INTERPRETACIÓN", contenidoP24, date(1900,1, 3), "unidad2", "El estudiante logra hacer satisfactoriamente el diagrama de clases")

# PREGUNTA 25

contenidoP25 = """Mencione las relaciones que pueden existir entre clases"""

pregunta25 = Pregunta("Programación II", "Recordar", 10, "COMPOSICIÓN", contenidoP25, date(1900,1, 3), "unidad2", "<< dependencia, generalización, asociación, agregación, composición>>")