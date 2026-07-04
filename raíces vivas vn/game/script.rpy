# ============================================================
# RAÍCES VIVAS
# Script principal
# ============================================================

define config.name = "Raíces Vivas"

default nombre = "T/n"

default ruta = ""

default confianza_yana = False
default orden_exploracion = ""
default intencion_final = ""

default ruta_quechua = False
default ruta_aymara = False
default ruta_uro = False
default ruta_jaqaru = False

transform centroizquierda:
    xalign 0.3

transform centroderecha:
    xalign 0.7



#--------------------------------------------------------------
# PERSONAJES
#--------------------------------------------------------------

define n = Character(None)

define tn = Character("[nombre]", color="#ffffff")

define y = Character("Yana", color="#D88EFF")

define mamaqori = Character("Mama Qori", color="#FFD166")

define tayta = Character("Tayta Pillco", color="#8BC34A")

define mamasisa = Character("Mama Sisa", color="#F4A261")

define v = Character("?????", color="#aaaaaa")



#--------------------------------------------------------------
# INICIO
#--------------------------------------------------------------

label start:

    scene black
    with fade

    "Antes de comenzar..."

    "¿Cuál es tu nombre?"

    $ nombre = renpy.input("Escribe tu nombre.")

    $ nombre = nombre.strip()

    if nombre == "":
        $ nombre = "T/n"

    "Mucho gusto, [nombre]."

    jump prologo