label seleccion_ruta:

    scene black
    with fade

    "Frente a ti aparecen cuatro senderos."

    menu:

        "Ruta Quechua":

            $ ruta = "quechua"

            jump ruta_quechua


        "Ruta Aymara":

            $ ruta = "aymara"

            jump ruta_aymara


        "Ruta Uro":

            $ ruta = "uro"

            jump ruta_uro


        "Ruta Jaqaru":

            $ ruta = "jaqaru"

            jump ruta_jaqaru