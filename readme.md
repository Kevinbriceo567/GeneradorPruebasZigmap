# GENERADOR DE EVALUACIONES ESCRITAS
## ¡El Generador de Pruebas es una herramienta que permitirá al docente crear evaluaciones tomando en cuenta diferentes atributos de sus preguntas!

Este generador está pensado para trabajar basado en la Taxonomía de Bloom.
Actualmente utiliza dos motores de generación de PDFs

> PDFKit |
> LaTeX

# Se necesitan las siguientes librerías:

- Principales
  - flask (pip)
  - flask_wtf (pip)

- Generando con PDFKit
  - pdfkit (pip)

- Generando con LaTeX
  - pylatex (pip)
  - Distribución de LaTeX instalada (Probado con TeX Live)

- En Ubuntu
  - Se recomienda instalar los binarios del archivo [wkhtmltox_0.12.5-1.bionic_amd64.deb]

#LOGIN:
-user: admin1
-pass: admin1


#Recomendaciones de uso:
- El programa completo fue desarrollado con Windows 10, por lo que la
mejor recomendación de uso es utilizar este sistema operativo, para
tener una mejor experiencia como usuario.

- Al utilizar Linux, se recomienda no utilizar el navegador “Firefox” ya que este
genera problemas con “Flask” y los formularios. Por lo tanto, es mayormente recomendable
su uso con “Google Chrome”.

- Con Linux, se recomienda generar la prueba con “LaTeX”.

- Si el programa se ejecuta Linux y quiere utilizar la opción de
PDFkit al intentar generar la prueba, debe instalar el archivo binario llamado
“wkhtmltox_0.12.5-1.bionic_amd64.deb”.