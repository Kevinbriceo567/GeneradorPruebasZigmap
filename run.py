# IMPORTAMOS DE LA LIBRERÍA flask
from flask import render_template, request, redirect, url_for, Flask
from flask_wtf import FlaskForm

# PARA DESCARGA DE ARCHIVOS
from flask import send_file, send_from_directory, safe_join, abort, current_app
from pathlib import Path

# LIBRERÍAS PARA LOS FORMULARIOS
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length

# CÁLCULO
import math
import random

# IMPORTAMOS LAS CLASES
from model.Carrera import *
from model.Asignatura import *
from model.Prueba import *
from model.Pregunta import *
from model.Curso import *
from model.PreguntasRepository import PreguntasRepository
from model.UsuariosRepository import UsuariosRepository

# ARCHIVOS
import sys, os
from os import listdir
from os.path import isfile, join

# FECHAS
from datetime import date

# INSTANCIAMOS UN OBJETO DE LA CLASE Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

# VARIABLES GLOBALES
# CARRERA
nombreC = ""
facultad = ""
carrera = Carrera

# ASIGNATURA
nombreA = ""
idA = ""
asignatura = Asignatura

# CURSO
cod = ""
curso = Curso

# PRUEBA
nombreP = ""
fechaP = ""
ponderacionP = ""
unidadP = ""
cantidad = 0
nivelesTax = []
todasCheck = ''

# PREGUNTAS
repositorio = PreguntasRepository()
preguntasRepo = repositorio.get_preguntas()

# PRUEBAS
listaPruebas = []
nombreFile = ""


# GENERACIÓN
generate = ''

# LOGIN
logded = False

# INICIAMOS UNA RUTA PARA LA WEB
@app.route("/home", methods=["GET", "POST"])
def home():

    if request.method == 'POST':

        # CARRERA
        global nombreC
        global facultad
        global carrera

        # ASIGNATURA 
        global nombreA
        global idA
        global asignatura

        # CURSO
        global cod
        global curso

        # PRUEBA
        global nombreP 
        global fechaP 
        global ponderacionP
        global unidadP
        global cantidad
        global nivelesTax
        global todasCheck
        
        # CARRERA
        nombreC = request.form['nombreC']
        facultad = request.form['facultad']

        carrera = Carrera(nombreC, facultad)

        # ASIGNATURA
        
        nombreA = request.form['nombreA']
        idA = request.form['idA']
        
        asignatura = Asignatura(nombreA, idA)

        # CURSO
        cod = request.form['cod']
        curso = Curso(cod)

        # PRUEBA
        nombreP = request.form['nombreP']
        fechaP = request.form['fechaP']
        ponderacionP = request.form['ponderacionP']
        unidadP = request.form['unidad']
        cantidad = int(request.form['cantidadP'])

        try:
            todasCheck = request.form['all']
        except BaseException as e:
            print(e)

        nivelesTax = []

        if todasCheck == 'on':
            unidadP = "Unidades: 1 & 2"


                # BUSCANDO DISPONIBLES
        disponibles = {"Entender":0, "Recordar":0, "Aplicar":0, "Analizar":0, "Evaluar":0, "Crear":0}
        fechaHoy = date.today() # date(year, month, day)

        for p in preguntasRepo:
        
            # FECHA ULTIMO USO
            fechaUlt = p.get_fecha()

            # COMPROBACION DE TIEMPO
            restaFechas = str(fechaHoy - fechaUlt)

            print("---------------------------------" + restaFechas + "-------------------------------")

            try:
                if int(restaFechas.rstrip(" days, 0:00:00")) > 730:
                    
                    if (unidadP == p.get_unidad() and nombreA == p.get_nombreAsig()) or (todasCheck == 'on' and nombreA == p.get_nombreAsig()):
                        nivelTax = p.get_nivel()

                        disponibles[nivelTax] += 1

            except ValueError as e:
                print(p.get_nivel() + " USADA")



        return render_template('preguntas.html', cantidad = cantidad, disponibles = disponibles)

        next = request.args.get('next', None)
        
        if next:
            return redirect(next)

    if logded == True:
        return render_template('home.html')

    else:
        return render_template('authorize.html')



# PÁGINA QUE RECIBE DATOS DEL FORMULARIO
@app.route("/result", methods=["GET", "POST"])
def result():

    global generate

    if request.method == 'POST':

        global nombreFile

        if generate == 'latex':
            return download(filename = nombreFile)

        else:
            return download(filename = nombreFile + "PDFKit")

        next = request.args.get('next', None)
        
        if next:
            return redirect(next)



    return render_template('result.html')


@app.route('/download/<path:filename>', methods=["GET", "POST"]) # /<path:filename>
def download(filename):

    global aleatorio
    global nombreFile

    p = Path("tests/" + filename + ".pdf").resolve()

    try:
        return send_file(p, attachment_filename=nombreFile + ".pdf")
	
    except Exception as e:
        return str(e)


# PÁGINA DE LOGIN
@app.route("/", methods=["GET", "POST"])
def login():
        
    global logded

    if request.method == 'POST':

        usuariosRepo = UsuariosRepository() # CREANDO OBJETO DE LA CLASE
        listaUsuarios = usuariosRepo.get_usuarios() # USANDO MÉTODO PARA OBTENER OBJETOS DE LA CLASE Usuario

        usuario = request.form['usuario']
        contrasena = request.form['password']

        for user in listaUsuarios:
            if usuario == user.get_nombreU() and contrasena == user.get_contrasena():

                logded = True
                return render_template('home.html')

        if logded == False:
            return render_template('login.html', alerta = "Usuarios o contraseña incorrectos")


        next = request.args.get('next', None)
        
        if next:
            return redirect(next)

    return render_template('login.html')

# PÁGINA DE ABOUT
@app.route("/help")
def help():
    return render_template('help.html')


@app.route("/about")
def about():
    return render_template('about_us.html')


@app.route("/pruebas")
def pruebas():

    global listaPruebas

    if logded == True:
        return render_template('pruebas.html', listaPruebas = listaPruebas)

    else:
        return render_template('authorize.html')



@app.route("/newQ", methods=["GET", "POST"])
def newQ():

    if request.method == 'POST':

        global preguntasRepo

        asignatura = request.form['nombreA']
        nivel = request.form['nivelP']
        tipo = request.form['tipoP']
        contenido = request.form['contenidoP']
        tiempo = request.form['tiempoP']
        solucion = request.form['solucionP']
        fecha = date(1900, 10, 10)
        unidad = request.form['unidadP']

        pregunta = Pregunta(asignatura, nivel, tiempo, tipo, contenido, fecha, unidad, solucion)

        preguntasRepo.append(pregunta)

        return render_template('home.html')

        next = request.args.get('next', None)
        
        if next:
            return redirect(next)

    if logded == True:
        return render_template('newQuestion.html')

    else:
        return render_template('authorize.html')




# LISTA DE PREGUNTAS DISPONIBLES
@app.route("/disponibles", methods=["GET"])
def disponibles():
    disponibles = []

#### preguntasRepo

    fechaHoy = date.today() # date(year, month, day)

    for p in preguntasRepo:
    
        # FECHA ULTIMO USO
        fechaUlt = p.get_fecha()

        # COMPROBACION DE TIEMPO
        restaFechas = str(fechaHoy - fechaUlt)

        if int(restaFechas.rstrip(" days, 0:00:00")) > 730: # 2019-10-08 | COMPROBAMOS LA FECHA
            disponibles.append(p)
            
    if logded == True:
        return render_template('disponibles.html', disponibles = disponibles)

    else:
        return render_template('authorize.html')

     




# SELECCIÓN DE PREGUNTAS
@app.route("/preguntas", methods=["GET", "POST"])
def preguntas():

    if request.method == 'POST':

        # CARRERA
        global nombreC
        global facultad

        # ASIGNATURA 
        global nombreA
        global idA

        # CURSO
        global cod 

        # PRUEBA
        global nombreP 
        global fechaP 
        global ponderacionP
        global unidadP
        global cantidad
        global nivelesTax

        global preguntasRepo
        global nombreFile
        global todasCheck

        global generate

        listaPreguntas = []

        tiempoResTotal = 0

        reportes = []

        indices = []

        generate = request.form['generate']


        # REVISANDO MOTOR DE GENERACIÓN
        try:
            cLatex = request.form['cLatex']
            cPDFKit = request.form['cPDFKit']
        except BaseException as e:
            print(e)



        for i in range(0, cantidad):
            indices.append('pregunta' + str(i))

        for i in indices:
            
            for p in preguntasRepo:

                    if request.form[i] == p.get_nivel():

                        reportes.append("NIVEL RECONOCIDO")

                        if (unidadP == p.get_unidad() and nombreA == p.get_nombreAsig()) or (todasCheck == 'on' and nombreA == p.get_nombreAsig()):

                            reportes.append("UNIDAD RECONOCIDA")
                            reportes.append("ASIGNATURA RECONOCIDA")

                            # FECHA ACTUAL
                            anno = fechaP[0:4]
                            mes = fechaP[5:7]
                            dia = fechaP[8:10]

                            fechaAct = date(int(anno), int(mes), int(dia)) # date(year, month, day)

                            # FECHA ULTIMO USO
                            fechaUlt = p.get_fecha()

                            # COMPROBACION DE TIEMPO
                            restaFechas = str(fechaAct - fechaUlt)

                            print("---------------------------------" + restaFechas + "-------------------------------")

                            if int(restaFechas.rstrip(" days, 0:00:00")) > 730: # 2019-10-08 | COMPROBAMOS LA FECHA
                                    
                                reportes.append(p.get_unidad() + p.get_nivel() + " FECHA RECONOCIDA")

                                if p.get_nivel() not in nivelesTax:
                                    nivelesTax.append(p.get_nivel())

                                if p not in listaPreguntas and len(listaPreguntas) < cantidad :

                                    reportes.append(p.get_unidad() + p.get_nivel() + " PREGUNTA AGREGADA")

                                    listaPreguntas.append(p)

                                    tiempoResTotal += int(p.get_tiempo())

                                else:
                                    reportes.append(p.get_unidad() + p.get_nivel() + " PREGUNTA NO AGREGADA")


        if cantidad == len(listaPreguntas):

            for p in listaPreguntas:
                p.set_fecha(date(int(anno), int(mes), int(dia))) # ACTUALIZAMOS LA FECHA

            print("GENERADAAAAAAAAAAAAA")

            resultado = "Generada"

            prueba = Prueba(nombreP, fechaP, cantidad, nivelesTax, ponderacionP, unidadP, listaPreguntas)

            listaPruebas.append(Prueba(nombreP, fechaP, cantidad, nivelesTax, ponderacionP, unidadP, listaPreguntas))

            aleatorio = random.randint(1, 10001)

            nombreFile = nombreP + " - " + fechaP + " - " + str(aleatorio)

            if generate == 'latex':
                try:
                    prueba.generar(carrera, asignatura, curso, listaPreguntas, aleatorio)

                except UnicodeDecodeError as e:
                    print(e)
                except BaseException as e:
                    print(e)

            else:
                prueba.generarPDFKit(carrera, asignatura, curso, listaPreguntas, aleatorio)


            return render_template('result.html', resultado = resultado, reportes = reportes, tiempoResTotal = tiempoResTotal,
            niveles = len(nivelesTax), cantidad = len(listaPreguntas), ponderacion = ponderacionP, nombreFile = nombreFile)

        else:

            resultado = "No Generada"

            return render_template('result.html', listaPreguntas = listaPreguntas, resultado = resultado, reportes = reportes)




        next = request.args.get('next', None)
        
        if next:
            return redirect(next)

        return render_template('result.html', listaPreguntas = listaPreguntas)
        
    return render_template("preguntas.html")







@app.route("/authorize")
def authotize():
    return render_template('authorize.html')





# EJECUTAMOS LA APLICACIÓN
if __name__ == "__main__":

    app.run(port=5001, debug=True)