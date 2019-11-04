# IMPORTAMOS LAS CLASES
from Carrera import *
from Asignatura import *
from Pregunta import *
from Curso import *

import reportlab

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
        nombreFile = str(self.__nombre) + " - " + self.get_fecha() + " - " + str(aleatorio)




from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4

pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))
 
logo = "logo.png"
im = Image(logo, 0.7*inch, 0.7*inch, hAlign='LEFT')

canvas = canvas.Canvas("form.pdf", pagesize=(595.27,805.89))
canvas.setLineWidth(.3)
canvas.setFont("Times-Roman", 11)
 
canvas.drawImage("logo.png", 30, 750, 40, 40)
#canvas.drawString(30,750,'OFFICIAL COMMUNIQUE')
canvas.drawString(30,735,'OF ACME INDUSTRIES')


canvas.drawString(480,750,"Programación II")
canvas.drawString(480,730,"Curso 606")
canvas.drawString(480,710,"Unidad 1")

canvas.setFont("Times-Roman", 15)
canvas.drawString(250,760,"Solemne I")

canvas.setFont("Times-Roman", 11)
 
canvas.drawString(30,725,'Rut:')
canvas.line(60,723,180,723)
 
canvas.drawString(30,703,'Nombre:')
canvas.line(80,700,250,700)
canvas.drawString(120,703,"")

canvas.drawString(30,681,'Nota:')
canvas.line(60,678,180,678)
canvas.drawString(120,681,"")


W, h = A4
text = canvas.beginText(40, h - 200)
text.setFont("Times-Roman", 11)
text.textLine("¡Hola, mundo!")
text.textLine("¡Desde ReportLab y Python!")
canvas.drawText(text)

 
canvas.save()















doc = SimpleDocTemplate("form_letter.pdf",pagesize=letter,
                        rightMargin=60,leftMargin=60,
                        topMargin=50,bottomMargin=18)
Story=[]
logo = "logo.png"
magName = "Pythonista"
issueNum = 12
subPrice = "99.00"
limitedDate = "03/05/2010"
freeGift = "tin foil hat"
 
formatted_time = time.ctime()
full_name = "Mike Driscoll"
address_parts = ["411 State St.", "Marshalltown, IA 50158"]
 
im = Image(logo, 0.7*inch, 0.7*inch, hAlign='LEFT')
Story.append(im)
 
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
ptext = '<font size=12>%s</font>' % formatted_time
 
Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 12))
 
# Create return address
ptext = '<font size=12>%s</font>' % full_name
Story.append(Paragraph(ptext, styles["Normal"]))       
for part in address_parts:
    ptext = '<font size=12>%s</font>' % part.strip()
    Story.append(Paragraph(ptext, styles["Normal"]))   
 
Story.append(Spacer(1, 12))
ptext = '<font size=12>Dear %s:</font>' % full_name.split()[0].strip()
Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 12))
 
ptext = '<font size=12>We would like to welcome you to our subscriber base for %s Magazine! \
        You will receive %s issues at the excellent introductory price of $%s. Please respond by\
        %s to start receiving your subscription and get the following free gift: %s.</font>' % (magName, 
                                                                                                issueNum,
                                                                                                subPrice,
                                                                                                limitedDate,
                                                                                                freeGift)
Story.append(Paragraph(ptext, styles["Justify"]))
Story.append(Spacer(1, 12))
 
 
ptext = '<font size=12>Thank you very much and we look forward to serving you.</font>'
Story.append(Paragraph(ptext, styles["Justify"]))
Story.append(Spacer(1, 12))
ptext = '<font size=12>Sincerely,</font>'
Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 48))
ptext = '<font size=12>Ima Sucker</font>'
Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 12))
doc.build(Story)










from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph
from functools import partial

styles = getSampleStyleSheet()
styleN = styles['Normal']
styleH = styles['Heading1']

def header(canvas, doc, content):
    canvas.saveState()
    w, h = content.wrap(doc.width, doc.topMargin)
    content.drawOn(canvas, 40, doc.height + 120 - h)
    canvas.restoreState()

doc = BaseDocTemplate('test.pdf', pagesize=(595.27,805.89))
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height-2*inch, id='normal')

header_content = Image('logo.png', 45, 45, hAlign="LEFT")
#header_content = Paragraph("This is a multi-line header.  It goes on every page.  " , styleN)

template = PageTemplate(id='test', frames=frame, onPage=partial(header, content=header_content))
doc.addPageTemplates([template])


text = []
for i in range(60):
    text.append(Paragraph("This is line %d. dfiofdjiogbjroigjeriogjreoigjeroigjreigojriojregoerjgioerjgiorejgeirogjeriogjeiojreiogjreoigjergiojrgiojregoijrogie" % i, styleN))
doc.build(text)
















