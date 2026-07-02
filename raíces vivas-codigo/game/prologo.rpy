label prologo:

    stop music fadeout 1.0
    play music "audio/prologo.ogg" fadein 2.0

    scene bg_ciudad_dia
    with fade

    n "El mundo avanza rápido. Las ciudades no duermen. Todo cambia sin que te des cuenta."

    n "Pero no todo cambia."

    n "En los altos Andes del Perú existen pueblos que siguen viviendo de una manera distinta."

    n "Pueblos que recuerdan lo que el resto del mundo ha preferido olvidar."

    n "[nombre] era una persona con mucha curiosidad, sentía mucha intriga por todo lo que le rodeaba"

    n "De esos que observan más de lo que hablan, que notan detalles que otros ignoran."

    n "Ese día no tenía planes especiales. Caminaba sin rumbo fijo cuando, sin saber cómo, terminó frente a una biblioteca. No recordaba haber decidido entrar. Pero ahí estaba."

    scene bg_biblioteca
    with dissolve


    n "El lugar olía a papel viejo y madera húmeda. El tiempo allí parecía moverse más despacio que afuera."

    n "Recorrió los pasillos sin buscar nada en particular."

    n "Hasta que algo lo detuvo."

    scene bg_estante_libro
    with dissolve

    n "Casi al fondo, entre libros descuidados, había uno fuera de lugar. Viejo y cubierto de polvo."

    n "Además estaba sin título en la tapa."

    n "[nombre] lo tomó entre sus manos con delicadeza."

    n "Las marcas de la cubierta parecían haber sido grabadas a mano hacía muchísimo tiempo."

    play sound "audio/page.ogg"

    scene bg_libro_abierto
    with dissolve

    n "Al abrirlo, las páginas crujieron como si llevaran años esperando ser tocadas."

    n "Hablaba de los pueblos originarios andinos del Perú: Quechua, Aymara, Uro y Jaqaru"

    n "Había dibujos de montañas, tejidos con patrones geométricos, lagos inmensos y personas de mirada tranquila."

    n " También vió historias, fiestas, lenguas y tradiciones"

    scene bg_paginas_arrancadas
    with dissolve

    n "Pero al llegar al final del libro..."

    n "Algo estaba mal. Había numerosas páginas arrancadas."

    n "No parecían haberse desprendido con el tiempo. Alguien las había arrancado. Como si hubiese querido impedir que fueran leídas."

    n "[nombre] pasó lentamente los dedos sobre el borde rasgado del papel."

    play sound "audio/heartbeat.ogg"

    pause 0.8

    n "Y entonces lo vio..."

    n "Su propio nombre. Escrito con una letra que jamás había visto."

    n "Parpadeó y lo volvió a mirar. Seguía allí. No parecía un error."

    n "Pasó la siguiente hoja."

    scene black
    with fade

    centered "«No puedes prepararte para lo que encontrarás»"

    pause 2.0

    scene bg_libro_abierto
    with dissolve

    n "Un escalofrío recorrió todo su cuerpo."

    play sound "audio/book_close.ogg"

    n "Cerró el libro de golpe. Y salió de la biblioteca sin mirar atrás."

    jump prologo_parte2

    label prologo_parte2:

    scene bg_ciudad_tarde
    with fade

    stop sound

    n "El aire afuera se sentía distinto. Más pesado y más frío."

    n "Aunque la calle seguía exactamente igual. La gente caminaba. Los autos avanzaban. Nadie parecía haber notado lo que acababa de ocurrir."

    n "[nombre] intentó convencerse de que todo había sido una coincidencia. Un libro extraño."

    n "Nada más..."

    scene bg_avenida_atardecer
    with dissolve

    n "Pero antes de llegar a casa, algo lo obligó a detenerse."

    play sound "audio/misterio.ogg"

    scene bg_cartel
    with fade

    n "Un cartel se alzaba junto a la avenida. No recordaba haberlo visto nunca."

    n "Estaba cubierto de símbolos antiguos. No parecían letras. Parecían marcas talladas sobre piedra."

    pause 1.0

    centered "«La tierra ya escuchó tu nombre.»"

    pause 1.0

    centered "«Tú pediste esto.»"

    pause 1.0

    centered "«Nada es casualidad...»"

    pause 2.0

    scene bg_cartel
    with dissolve

    n "La respiración de [nombre] se detuvo por un instante. Aquellas palabras parecían dirigidas únicamente a él."

    play sound "audio/viento.ogg"

    n "Entonces..."

    n "Escuchó voces muy lejanas. Como si viajaran con el viento. No entendía lo que decían."

    n "Pero, por alguna razón... Sentía que debía escucharlas."

    scene bg_avenida_vacia
    with dissolve

    n "Apartó la vista apenas un segundo."

    pause 0.5

    n "Cuando volvió a mirar... El cartel había desaparecido."

    n "No quedaba absolutamente nada. Ni el poste. Ni las luces. Ni una sola señal de que hubiera estado allí."

    pause 1.0

    n "[nombre] retrocedió un paso."

    n "Quiso preguntarle a alguien. Pero las personas seguían caminando con total normalidad. Como si nunca hubiera existido ningún cartel."

    scene bg_habitacion_noche
    with fade

    stop music fadeout 2.0
    play music "audio/noche.ogg" fadein 2.0

    n "Esa noche no pudo dormir."

    n "Cada vez que cerraba los ojos... Veía las páginas arrancadas,su nombre y aquella advertencia."

    n "Intentó distraerse. Pensó en escribirle a alguien. Pero ¿qué iba a decir?"

    centered "«Encontré mi nombre en un libro y un cartel imposible me habló.»"

    pause 1.5

    n "Nadie le creería. Tal vez ni él mismo."

    scene bg_puerta
    with dissolve

    n "Sin saber por qué... Se levantó. Fue hasta la puerta y comprobó el seguro."

    pause 0.5

    n "Una vez."

    pause 0.5

    n "Dos veces."

    pause 1.0

    scene bg_habitacion_noche
    with dissolve

    n "Volvió a acostarse. El silencio del cuarto era diferente."

    n "Como si algo... También estuviera despierto."

    pause 1.5

    scene black
    with Fade(2.0, 2.0, 2.0)

    n "Finalmente, el cansancio venció."

    n "Y entonces... Comenzaron los sueños..."

    jump prologo_parte3

label prologo_parte3:

    scene black
    with Dissolve(2.0)

    play music "audio/sueno.ogg" fadein 2.0

    n "Al principio solo fueron imágenes sueltas."

    n "Montañas."

    n "Ríos."

    n "Senderos de piedra que parecían no tener final."

    n "Después llegaron las voces."

    play sound "audio/voces.ogg"

    n "Todos hablaban al mismo tiempo en lenguas que nunca había escuchado."

    n "No entendía ninguna palabra. Y, aun así... Sentía que todas intentaban decirle algo."

    scene black
    with Dissolve(2.0)

    pause 1.5

    n "De pronto..."

    n "Todo quedó en silencio."

    stop sound

    pause 1.5

    scene bg_sueno
    with Fade(2.0, 1.0, 2.0)

    n "Frente a él apareció un paisaje inmenso. Miles de estrellas iluminaban el cielo. Las montañas parecían tocar el firmamento."

    n "A lo lejos, un lago reflejaba la luz como si fuera un espejo."

    pause

    n "Nunca había estado allí."

    n "Y, sin embargo... Sentía que aquel lugar lo conocía."

    scene bg_cuatro_senderos
    with dissolve

    n "En medio del paisaje había cuatro senderos. Cada uno conducía hacia una dirección distinta."

    n "Cada uno parecía esperar su llegada."

    pause

    play sound "audio/viento.ogg"

    v "Las historias están desapareciendo..."

    pause 1.5

    v "Y cuando una historia desaparece..."

    pause

    v "...también desaparece una parte de quienes la vivieron."

    pause 2.0

    n "Los senderos comenzaron a iluminarse lentamente y cada uno parecía tener una energía distintiva"

    n "Sobre cada uno había su respectivo nombre grabado en piedra"

    show text "QUECHUA" with dissolve

    pause 1.2

    hide text

    show text "AYMARA" with dissolve

    pause 1.2

    hide text

    show text "URO"

    with dissolve

    pause 1.2

    hide text

    show text "JAQARU"

    with dissolve

    pause 2.0

    hide text

    v "Cada camino guarda una historia."

    pause

    v "Cada decisión cambiará aquello que descubrirás."

    pause

    v "Elige..."

    pause 1.5

    stop music fadeout 2.0

    menu:

        "Seguir el sendero Quechua":

            jump ruta_quechua

        "Seguir el sendero Aymara":

            jump ruta_aymara

        "Seguir el sendero Uro":

            jump ruta_uro

        "Seguir el sendero Jaqaru":

            jump ruta_jaqaru

    jump seleccion_ruta
