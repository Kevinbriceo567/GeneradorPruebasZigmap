# IMPORTAMOS LAS CLASES
from model.Carrera import *
from model.Asignatura import *
from model.Pregunta import *
from model.Curso import *

from pylatex import Document, PageStyle, Head, Foot, MiniPage, \
    StandAloneGraphic, MultiColumn, Tabu, LongTabu, LargeText, MediumText, \
    LineBreak, NewPage, Tabularx, TextColor, simple_page_number, Section, Figure, \
    SubFigure, NoEscape, Subsection, Tabular, Math, TikZ, Axis, Plot, Matrix, Alignat, \
    Itemize, Enumerate, Description, Command

from pylatex.utils import NoEscape, italic, bold
from pathlib import Path

from datetime import date, datetime

# CLASES DEL SISTEMA OPERATIVO
import os, glob, subprocess

class Prueba(object):

    # CONSTRUCTOR #
    def __init__(self, nombre, fecha, cantidad, nivelesTax, ponderacion, unidad, listaPreguntas):
        self.__nombre = nombre
        self.__fecha = fecha
        self.__cantPreguntas = cantidad
        self.__nivelestax = nivelesTax
        self.__ponderacion = ponderacion
        self.__unidad = unidad
        self.__listaPreguntas = listaPreguntas
        
    
    # GETTERS AND SETTERS #
    def get_nombre (self):
        return self.__nombre

    def set_nombre (self, nomp):
        self.__nombre = nomp

    def get_fecha (self):
        return self.__fecha

    def set_fecha (self, fechap):
        self.__fecha = fechap

    def get_cantPreguntas (self):
        return self.__cantPreguntas

    def set_cantPreguntas (self, cantp):
        self.__cantPreguntas = cantp

    def get_nivelestax (self):
        return self.__nivelestax

    def set_nivelestax (self,ntaxp):
        self.__nivelestax = ntaxp

    def get_ponderacion (self):
        return self.__ponderacion

    def set_ponderacion (self,pondp):
        self.__ponderacion = pondp

    def get_unidad (self):
        return self.__unidad

    def set_unidad (self,unidad):
        self.__unidad = unidad

    def get_listaP (self):
        return self.__listaP

    def set_listaP (self, listaP):
        self.__listaP = listaP

    # MOSTRAR DATOS
    def mostrarD(self):

        print(self.__nombre)
        print(self.__fecha)
        print(self.__cantPreguntas)
        print(self.__nivelestax)
        print(self.__ponderacion)
        print(self.__unidad)
        print(self.__listaPreguntas)

    # MÉTODO DE GENERACIÓN DE PDF
    def generar(self, Carrera, Asignatura, Curso, listaPreguntas, aleatorio):

        today = str(self.__fecha)

        geometry_options = {
        "head": "48pt",
        "margin": "0.5in",
        "bottom": "0.6in",
        "includeheadfoot": True}

        doc = Document(geometry_options = geometry_options)

        header = PageStyle("header") # DEFINIMOS LA VARIABLE CON ESTILO

        image_filename = os.path.join(os.path.dirname(__file__), '../static/zigmap.png') # IMAGEN UNAB

        # Generating first page style
        first_page = PageStyle("firstpage")


        # Header image
        with first_page.create(Head("L")) as header_left:

            with header_left.create(SubFigure(position='L', width=NoEscape(r'0.10\linewidth'))) as logo_wrapper:

                logo_wrapper.add_image(image_filename, width=NoEscape(r'\linewidth'))

     
        # Add document title
        with first_page.create(Head("C")) as center_header:
            with center_header.create(MiniPage(width=NoEscape(r"0.49\textwidth"),
                                    pos='c', align='c')) as title_wrapper:
                title_wrapper.append(LargeText(bold(self.__nombre)))
                '''
                title_wrapper.append(MediumText(bold("Ingeniería en Computación e Informática")))
                title_wrapper.append(LineBreak())
        '''
        # Add document title
        with first_page.create(Head("R")) as right_header:
            with right_header.create(MiniPage(width=NoEscape(r"0.49\textwidth"),
                                    pos='c', align='r')) as title_wrapper:
                #title_wrapper.append(LargeText(bold("Solemne II")))
                #title_wrapper.append(LineBreak())
                title_wrapper.append(MediumText(bold(Asignatura.get_nombreA())))
        
        # Add footer
        with first_page.create(Foot("C")) as footer:
            message = "Programación II"
            with footer.create(Tabularx("X X X X", width_argument=NoEscape(r"\textwidth"))) as footer_table:

                footer_table.add_row([MultiColumn(4, align='l', data=TextColor("black", message))])
                footer_table.add_hline(color="black")
                footer_table.add_empty_row()

                branch_address = MiniPage(width=NoEscape(r"0.45\textwidth"), pos='t', align='l')
                branch_address.append(MediumText("Facultad de " + Carrera.get_facultad()))
                branch_address.append("\n")
                branch_address.append("")

                branch_address2 = MiniPage(width=NoEscape(r"0.10\textwidth"), pos='t')
                branch_address2.append("")
                branch_address2.append("\n")
                branch_address2.append("")

                document_details = MiniPage(width=NoEscape(r"0.25\textwidth"), pos='t', align='r')
                document_details.append(self.__fecha)
                document_details.append(LineBreak())
                document_details.append("") # simple_page_number()

                footer_table.add_row([branch_address, branch_address2, branch_address2, document_details])
        '''
        with first_page.create(Foot("L")) as footer_left:
            footer_left.append(LineBreak())
            footer_left.append("\n")
            footer_left.append(MediumText(bold("Ingeniería en Computación e Informática")))

        with first_page.create(Foot("R")) as footer_left:
            footer_left.append(LineBreak())
            footer_left.append("\n")
            footer_left.append(MediumText(bold("Ingeniería en Computación e Informática")))
        '''

        doc.preamble.append(first_page)
        # End first page style

                
        ############################################
        
            
        # Add customer information
        '''
        with doc.create(Tabu("X[l]")) as first_page_table:
            customer = MiniPage(width=NoEscape(r"0.55\textwidth"), pos='t')
            customer.append(LargeText(bold("Facultad de Ingeniería")))
            customer.append("\n")
            customer.append(MediumText(bold("Ingeniería en Computación e Informática")))

            first_page_table.add_row([customer])
            first_page_table.add_empty_row()
        '''

    ####################################################
            # Add customer information
        with doc.create(Tabu("X[l] X[r]")) as first_page_table:
            customer = MiniPage(width=NoEscape(r"0.55\textwidth"), pos='h')
            customer.append("Nombre: ___________________________________")
            customer.append("\n")
            customer.append("    Rut:  _______________")
            customer.append("\n")
            customer.append(  "Nota: ______________")
            customer.append("\n")
            customer.append("\n")
            
            # Add branch information
            branch = MiniPage(width=NoEscape(r"0.35\textwidth"), pos='t!', align='r')
            branch.append("Curso")
            branch.append(LineBreak())
            branch.append(bold(Curso.get_cod()))
            branch.append(LineBreak())

            if self.__unidad == "unidad1":
                branch.append(bold("Unidad 1"))
            else:
                branch.append(bold("Unidad 2"))
            branch.append(LineBreak())

            branch.append(LineBreak())


            first_page_table.add_row([customer, branch])


        doc.append(LargeText(bold("Indicaciones:")))

        # INDICACIONES

        with doc.create(Itemize()) as itemize:
            doc.append(LineBreak())
            itemize.add_item(" Lea atentamente los enunciados de cada pregunta antes de contestar.")
            itemize.add_item(" Conteste su evaluación en silencio, está prohibido conversar o gesticulizar en la sala durante la prueba.")
            itemize.add_item(" Dispone de 90 minutos para realizar esta evaluación.")
            itemize.add_item(" Marque la alternativa con lapiz pasta, no se aceptan marcadas con lapiz grafito.")
            itemize.add_item(" Utilice solamente sus materiales, está prohibido solicitar materiales a sus compañeros.")
            # you can append to existing items
            itemize.append(Command("ldots"))


        doc.change_document_style("firstpage")
        doc.add_color(name="lightgray", model="gray", description="0.80")
        customer.append(LineBreak())

        now = str(datetime.today())


        for p in listaPreguntas:
            with doc.create(Section('Pregunta (20 Puntos)')):

                doc.append(p.get_contenido())


        doc.append(NewPage())

        nombreFile = str(self.__nombre) + " - " + self.get_fecha() + " - " + str(aleatorio)
        
        print("--------------------------ANTES DE DIR------------------------------")

        '''
        # Create directory
        dirName = 'tests/' + str(self.__nombre) + " - " + self.get_fecha() + " - " + str(aleatorio)
        
        try:
            # Create target Directory
            os.mkdir(dirName)
            print("Directory", dirName, "Created ") 
        except FileExistsError:
            print("Directory", dirName, "already exists")
        '''

        try:
            # GENERANDO PDF
            doc.generate_pdf(filepath = "tests/" + nombreFile, clean_tex=True, clean=True)
            #doc.generate_pdf(dirName + "/" + nombreFile, clean_tex=False)

        except FileNotFoundError as e:
            doc.generate_pdf(filepath = "../tests/" + nombreFile, clean_tex=True, clean=True)




    def generarPDFKit(self, Carrera, Asignatura, Curso, listaPreguntas, aleatorio):

        import pdfkit
        from jinja2 import Environment, FileSystemLoader
        from pathlib import Path

        env = Environment(loader=FileSystemLoader("templates/", encoding="utf-8"))
        template = env.get_template("testTemplate.html")

        print("PDFKITTTT")

        unidadBonita = ""
        if self.__unidad == "unidad 1":
            unidadBonita = "Unidad 1"
        else:
            unidadBonita = "Unidad 2"

        prueba = {
            'nombreA': Asignatura.get_nombreA(),
            'cod': Curso.get_cod(),
            'listaPreguntas': listaPreguntas,
            'unidad': unidadBonita,
            'nombreP': self.__nombre,
            'fechaP': self.__fecha,
            'facultad': Carrera.get_facultad()

        }

        html = template.render(prueba)
        print(html)

        nombreFile = str(self.__nombre) + " - " + self.get_fecha() + " - " + str(aleatorio) + "PDFKit"

        
        f = open("tests/" + nombreFile + ".html", "w", encoding="utf-8")
        f.write(html)
        f.close()

        f = open(nombreFile + ".txt", "w")
        f.write(html)
        f.close()
        

        p = Path("wkhtmltopdf/bin/wkhtmltopdf.exe").resolve()
        print(p)

        config = pdfkit.configuration(wkhtmltopdf=p)

        pdfkit.from_file("tests/" + nombreFile + ".html", "tests/" + nombreFile + ".pdf", configuration=config)