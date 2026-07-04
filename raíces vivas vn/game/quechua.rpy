############################################################
# LLEGADA A CHINCHERO
############################################################
label ruta_quechua:

scene black
with fade

n "Tienes una sensación extraña"

scene ciudad_cuzco

n "De pronto, en un milisegundo, ya estas en otro lugar muy diferente"

n "Ahí el aire se siente diferente, más frío."

n "Miras hacia un lado y te das cuenta que etsas en la ciudad del Cuzco"

n "No lo sabes pero este es un lugar dodne residen muchos pobladores que mantienen una cultura ancestral"

n "Luego, empiezas a caminar poco a poco, pero te sientes mareado. Más adelante hay varias agencias que te ofrecen tours. Sin embargo, no decides tomarlos"

n" Tienes el presentimiento de que lo que tienes que buscar se encuentra en otro lado, en los adentros de la ciudad"

scene minivan_enfoque

n "A lo lejos, observas una pequeña minivan y notas que se estan subiendo varios pobladores con una vestimenta diferente a la de los demás. Esto enciende tu curiosidad y tu acorazonada te conduce hacía el vehículo"

n "Al subir al vehículo sientes varias miradas sobre tí, pero solo las ignoras"

scene vehiculo_movimiento

n "Dentro de poco, el vehículo enciende y avanza. En el interior, todos hablan en un idioma diferente que no reconoces. Hasta que escuchas una palabra: Rimaykullayki"

n "Te parece haber escuchado eso antes, pero no recuerdad bien de donde. Presientes que es la lengua quechua"

n "Luego de un rato, apartas la vista y observas la ventana, vez un hermoso paisaje lleno de vegetación y lagunas que resplandecen por si solas. También, estas rodeado de altas montañas bellas"

scene bg chinchero_llegada with fade

n "Después de un tiempo, el vehículo se detiene."

n "Has llegado a Chinchero, un pueblo quechua donde las tradiciones siguen vivas en cada rincón."

n "El viento mueve telas de colores intensos colgadas frente a algunas casas. Por un instante sientes como si el propio lugar te estuviera observando."

scene bg camino_chinchero with dissolve

n "Bajas del transporte. No tienes dinero. No tienes equipaje. Tampoco encuentras tu celular."

n "No sabes en qué momento desaparecieron. Lo único que sabes es que estás completamente solo."

n "Observas el camino frente a ti sin saber hacia dónde ir."

play sound "audio/pasos.ogg"

y "Oye..."

y "Tú no eres de aquí."

show yana normal at center with dissolve

n "Te das la vuelta."

n "Frente a ti hay una joven con ropa tradicional de colores intensos y tejidos hechos a mano."

n "Su expresión mezcla curiosidad y desconfianza."

tn "Estoy buscando dónde quedarme."

n "La joven guarda silencio unos segundos antes de responder."

y "Es raro ver gente nueva por aquí."

y "Casi todos los visitantes siguen la ruta turística."

y "Tú pareces haberte perdido."

y "Ah... por cierto."

y "No me he presentado."

y "Me llamo Yana."

tn "Mucho gusto."

tn "Soy [nombre]."

n "Yana continúa observándote, como si intentara descubrir algo más que tu nombre."

y "Llegaste en un día complicado."

tn "¿Complicado?"

y "Sí."

y "Hoy comenzó el pago a la Pachamama."

tn "¿Qué significa eso?"

y "Después te lo explicaré."

y "Pero ahora mismo no deberías estar caminando solx por el pueblo."

y "Podrías perderte."

menu:

    "Seguir a Yana":
        $ confio_yana = True
        jump rama_confianza

    "Buscar alojamiento por tu cuenta":
        $ confio_yana = False
        jump rama_solitaria

############################################################
# RAMA SOLITARIA
############################################################

label rama_solitaria:

scene bg calle_noche with fade

hide yana

n "Decides agradecerle, pero prefieres buscar alojamiento por tu cuenta."

tn "Gracias... creo que podré arreglármelas."

n "Yana permanece inmóvil unos segundos."

show yana normal at center

y "Como quieras."

y "Pero ten cuidado con los caminos que elijas."

y "No todos llevan al lugar que uno espera."

hide yana with dissolve

scene bg callejones with dissolve

n "Empiezas a caminar sin un rumbo fijo."

n "Las calles parecen iguales."

n "Cada esquina conduce a otra aún más parecida."

n "El pueblo, que desde lejos parecía pequeño, ahora parece un laberinto."

scene bg callejones_noche with dissolve

n "El sol comienza a ocultarse."

n "La temperatura desciende rápidamente."

n "No encuentras hospedajes."

n "Tampoco encuentras personas."

n "Solo escuchas el viento atravesando las calles de piedra."

tn "Creo..."

tn "Creo que realmente me perdí."

scene bg escalones with dissolve

n "Después de caminar durante un largo rato, te sientas sobre un viejo escalón de piedra."

n "Empiezas a sentir hambre."

n "También frío."

n "Y por primera vez desde que llegaste, dudas de la decisión que tomaste."

play sound "audio/viento.ogg"

n "Entre el viento alcanzas a escuchar voces hablando en quechua."

n "No sabes si vienen del pueblo..."

n "O si solamente las estás imaginando."

play sound "audio/pasos.ogg"

scene bg callejones_noche with dissolve

n "A lo lejos aparece una pequeña luz."

show yana linterna at center with dissolve

y "Sabía que terminaría encontrándote aquí."

tn "..."

tn "Supongo que tenías razón."

y "No eres la primera persona que se pierde."

y "Y tampoco serás la última."

tn "Pensé que podría orientarme."

y "Este pueblo parece sencillo..."

y "Hasta que intentas recorrerlo solo."

tn "Lo siento."

y "No tienes que disculparte."

y "Solo ven."

y "Ya es tarde."

y "Puedes quedarte en mi casa esta noche."

tn "¿Estás segura?"

y "Si no lo estuviera, no habría salido a buscarte."

scene bg camino_casa with dissolve

n "Sin decir mucho más, comienzan a caminar."

n "Esta vez no intentas memorizar el camino."

n "Simplemente la sigues."


jump casa_yana 

############################################################
# RAMA DE CONFIANZA
############################################################

label rama_confianza:

scene bg camino_pueblo with fade

show yana normal at center

n "Dudas durante unos segundos."

n "Sin embargo, algo dentro de ti te dice que puedes confiar en ella."

tn "Está bien."

tn "Iré contigo."

y "Ven."

y "No está muy lejos, te lo aseguro."

scene bg calle_pueblo_noche with dissolve

n "Caminan por las estrechas calles de piedra."

n "Mientras avanzas, observas mujeres tejiendo frente a sus casas."

n "Niños corren entre las calles jugando con trompos de madera."

n "Algunos pobladores saludan a Yana en quechua mientras ella responde con naturalidad."

n "Todo el pueblo parece conocerse."

scene bg casa_exterior with dissolve

n "Después de varios minutos llegan frente a una pequeña casa de adobe."

n "Yana permanece unos segundos en silencio antes de abrir la puerta."

n "Mira discretamente hacia el camino por el que llegaron, como comprobando que nadie los siguiera."

y "Puedes quedarte aquí."

y "No es un hotel..."

y "Pero estarás segurx."

tn "Muchas gracias."

tn "No esperaba encontrar ayuda tan rápido."

y "Aquí nadie debería quedarse solo."

y "Menos un día como hoy."

jump casa_yana

############################################################
# CASA DE YANA
############################################################

label casa_yana:

scene bg casa_interior with fade

show yana normal at center

n "El interior de la casa es sencillo, pero acogedor."

n "El olor a leña invade toda la habitación."

n "Sobre las paredes cuelgan tejidos llenos de colores y figuras geométricas."

tn "Antes dijiste que hoy era un día especial."

tn "¿Qué quisiste decir?"

y "Hoy celebramos el pago a la Pachamama."

tn "¿Pachamama?"

y "Sí."

y "Es una ceremonia de agradecimiento."

y "Le damos gracias a la tierra por los alimentos, por el agua y por permitirnos vivir aquí."

y "Por eso casi todos los pobladores están reunidos en el cerro."

tn "Entonces..."

tn "¿Todo el pueblo participa?"

y "Casi todos."

y "Es una tradición que ha pasado de generación en generación."

y "Forma parte de quiénes somos."

tn "Nunca había escuchado algo así."

show yana feliz at center

y "Eso suele pasar."

y "Muchas personas conocen a los quechuas por los incas."

y "Pero nuestra historia es mucho más grande."

play sound "audio/puerta.ogg"

n "En ese momento se escucha abrir la puerta."

hide yana

scene bg casa_interior with dissolve

show tayta normal at left
show mamaqori normal at right

n "Dos personas entran cargando mantas y pequeños atados."

n "Todavía tienen tierra en las manos."

y "Ya llegaron."

y "Ellos son mis padres."

y "Mi mamá, Mama Qori."

y "Y mi papá, Tayta ."

show yana normal at center

mamaqori "Así que tenemos visita."

mamaqori "Acércate al fogón."

mamaqori "Afuera ya empezó el frío."

jump fogon

############################################################
# EL FOGÓN
############################################################

label fogon:

scene bg fogon with fade

show tayta normal at left
show mamaqori normal at right
show yana normal at center

n "Todos toman asiento alrededor del fogón."

n "El fuego ilumina lentamente la habitación mientras el frío de la noche queda del otro lado de la puerta."

play sound "audio/fuego.ogg"

n "Antes de decir una sola palabra, Tayta  toma un pequeño cántaro de barro."

n "Deja caer unas gotas sobre la tierra del piso mientras murmura unas palabras en quechua."

tn "¿Qué acaba de hacer?"

tayta "Compartir."

tn "¿Compartir?"

tayta "Antes de recibir, primero agradecemos."

tayta "La Pachamama nos sostiene todos los días."

tayta "Lo justo es ofrecerle algo antes de disfrutar nosotros."

tn "¿La Pachamama es como una diosa?"

mamaqori "No exactamente."

mamaqori "Para nosotros la Pachamama no vive en un templo."

mamaqori "Vive en la tierra que cultivamos."

mamaqori "En las montañas."

mamaqori "En los ríos."

mamaqori "En todo aquello que hace posible la vida."

n "Durante unos segundos solo se escucha el crepitar del fuego."

y "Muchas personas creen que ser quechua significa solamente haber pertenecido al Imperio Inca."

y "Pero no es así."

tn "¿No?"

y "El quechua ya existía mucho antes."

y "Era hablado por otros pueblos andinos incluso antes del Tahuantinsuyo."

y "Cuando los incas expandieron su territorio, adoptaron el runasimi como lengua principal."

y "Así pudo extenderse por gran parte de los Andes."

tn "Entonces..."

tn "¿Los quechuas no comenzaron con los incas?"

tayta "Exactamente."

tayta "Los imperios aparecen..."

tayta "Y algún día desaparecen."

tayta "Pero un pueblo permanece mientras conserve su lengua, sus costumbres y su memoria."

n "Las palabras de Tayta  quedan resonando en tu cabeza."

tn "¿Y cómo se organiza una comunidad como esta?"

show mamaqori feliz at right

mamaqori "Con algo llamado ayllu."

tn "¿Qué es un ayllu?"

tayta "Una comunidad."

tayta "No solo de familias."

tayta "También de responsabilidad."

tayta "Aquí nadie vive completamente solo."

tayta "Todos dependemos unos de otros."

y "Cuando una familia necesita ayuda para sembrar..."

y "...las demás ayudan."

y "Y cuando otra familia necesita apoyo..."

y "...esa ayuda regresa."

tn "¿Eso tiene algún nombre?"

y "Sí."

y "Se llama ayni."

tayta "Hoy trabajamos contigo."

tayta "Mañana tú trabajas conmigo."

tayta "Así nadie queda abandonado."

tn "Me gusta esa idea."

mamaqori "También existe la minka."

tn "¿Cuál es la diferencia?"

mamaqori "El ayni ayuda a una familia."

mamaqori "La minka ayuda a toda la comunidad."

tayta "Construir caminos."

tayta "Reparar canales."

tayta "Levantar una casa."

tayta "Cuando el trabajo es demasiado grande para una sola persona..."

tayta "...todo el pueblo participa."

n "Miras nuevamente el fuego."

n "Piensas en la ciudad de donde vienes."

n "En cuántas personas viven una al lado de la otra sin siquiera conocerse."

tn "Creo que nunca había escuchado una forma de vivir así."

show yana feliz at center

y "Mañana podrás verla con tus propios ojos."

y "Las palabras ayudan."

y "Pero entenderás mucho más cuando camines con nosotros."

tn "Me gustaría."

mamaqori "Entonces mañana conocerás nuestra chacra."

tayta "Y también algunos lugares que muy pocos visitantes llegan a ver."

n "Por primera vez desde que llegaste, sientes que el miedo empieza a desaparecer."

n "Sin darte cuenta, comienzas a sentirte bienvenido."

jump chullo

############################################################
# EL CHULLO Y LA NOCHE
############################################################

label chullo:

scene bg fogon with dissolve

show yana normal at center
show tayta normal at left
show mamaqori normal at right

n "La conversación continúa durante un buen rato."

n "Sin darte cuenta, el cansancio del viaje empieza a hacerse evidente."

mamaqori "Debe estar agotadx."

mamaqori "Ha sido un día muy largo."

y "Ven."

y "Te mostraré dónde vas a dormir."

scene bg habitacion with fade

hide tayta
hide mamaqori

show yana normal at center

n "La habitación es pequeña, sencilla y cálida."

n "Una cama de madera ocupa un rincón."

n "Junto a ella descansa un pequeño telar y varias mantas tejidas a mano."

play sound "audio/tela.ogg"

n "Yana toma un gorro tejido cuidadosamente doblado sobre una silla."

y "Toma."

y "Las noches aquí son muy frías."

tn "Gracias."

tn "Es muy bonito."

show yana feliz at center

y "Se llama chullo."

y "Mi mamá lo tejió cuando yo era pequeña."

y "Aquí casi todo lo que usamos está hecho por nuestras propias manos."

tn "Los dibujos se parecen mucho a los que vi en el libro."

n "yana mira el tejido unos segundos"

y "No son solo dibujos."

y "Cada comunidad tiene sus propios diseños."

y "Los colores."

y "Las figuras."

y "Incluso la forma de tejer."

y "Todo cuenta una historia."

tn "¿Como si fuera un idioma?"

show yana feliz at center

y "Exactamente."

y "Antes, una persona podía saber de qué comunidad eras solo mirando tu ropa."

y "Los tejidos también guardan recuerdos."

n "Observas nuevamente el chullo."

n "Por un instante los patrones geométricos parecen demasiado familiares."

n "Casi iguales a los símbolos grabados en el viejo libro."

tn "...Qué extraño."

y "¿Sucede algo?"

tn "No..."

tn "Solo me dio una sensación rara."

y "Descansa."

y "Mañana entenderás muchas cosas."

y "Buenas noches."

hide yana with dissolve

play sound "audio/puerta.ogg"

n "La puerta se cierra lentamente."

scene bg habitacion_noche with dissolve

n "Te acuestas."

n "El silencio del pueblo es muy distinto al de la ciudad."

n "No hay motores."

n "No hay bocinas."

n "Solo el viento recorriendo las montañas."

n "Aprietas el chullo entre las manos."

n "Sin darte cuenta..."

n "Te quedas dormidx."

jump sueno_inkarri

############################################################
# EL SUEÑO DE INKARRÍ
############################################################

label sueno_inkarri:

scene bg negro with fade
play music "audio/misterio.ogg" fadein 2.0

n "El sueño comienza sin avisar."

scene bg valle_niebla with dissolve

n "Te encuentras de pie en un inmenso valle cubierto por la niebla."

n "No sientes frío."

n "No sientes miedo."

n "Solo un extraño silencio."

n "Frente a ti se alzan montañas gigantescas."

n "Tan antiguas que parecen haber existido desde antes del tiempo."

scene bg cueva_dorada with dissolve

n "La tierra comienza a temblar suavemente."

play sound "audio/rumble.ogg"

n "Una cueva se abre lentamente entre las rocas."

n "Desde su interior emergen dos figuras."

show manco normal at left
show mamaocllo normal at right

n "Un hombre y una mujer."

n "Ambos visten prendas doradas que reflejan la luz como si estuvieran hechas de sol."

n "Caminan lentamente."

n "No hablan."

n "Simplemente continúan avanzando."

n "Sin saber por qué..."

n "Sabes quiénes son."

n "Manco Cápac."

n "Mama Ocllo."

scene bg lago_sagrado with dissolve

hide manco
hide mamaocllo

n "Detrás de ellos aparece un inmenso lago."

n "Su superficie permanece completamente inmóvil."

n "Como si el tiempo hubiera dejado de existir."

n "El reflejo del cielo y del agua es exactamente el mismo."

n "Es imposible distinguir dónde termina uno y comienza el otro."

play sound "audio/viento.ogg"

voice "audio/voz.ogg"

"Las historias nacen..."

"Pero también pueden desaparecer."

scene bg conquista with dissolve

play music "audio/tension.ogg" fadeout 1.0 fadein 2.0

n "Todo cambia de golpe."

n "El paisaje desaparece."

n "Ahora solo hay humo."

n "Gritos."

n "Metal chocando contra metal."

show atahualpa normal at center

n "Frente a ti un hombre permanece arrodillado."

n "Sus manos están atadas."

n "Soldados con armaduras rodean el lugar."

n "No puedes mover el cuerpo."

n "Solo observar."

play sound "audio/golpe.ogg"

n "Un instante después..."

n "Todo termina."

hide atahualpa

scene bg tierra_abierta with dissolve

play sound "audio/rumble.ogg"

n "Pero la tierra comienza a abrirse."

n "Algo se mueve debajo de ella."

n "No puedes verlo completamente."

n "Solo sientes su presencia."

voice "audio/voz.ogg"

"Inkarrí no ha muerto."

play sound "audio/latido.ogg"

voice "audio/voz.ogg"

"Su cuerpo continúa creciendo bajo la tierra."

voice "audio/voz.ogg"

"Esperando."

voice "audio/voz.ogg"

"Esperando a que alguien termine de contar su historia."

scene bg negro with Dissolve(2.0)

n "Las palabras resuenan una y otra vez."

voice "audio/voz.ogg"

"Las historias..."

voice "audio/voz.ogg"

"No deben desaparecer..."

voice "audio/voz.ogg"

"Encuentra los hilos..."

voice "audio/voz.ogg"

"Antes de que sea demasiado tarde..."

play sound "audio/latido.ogg"

scene bg habitacion_noche with vpunch

stop music fadeout 2.0

n "Abres los ojos de golpe."

n "Respiras con dificultad."

n "Todo vuelve a estar en silencio."

play sound "audio/viento.ogg"

n "La habitación permanece completamente oscura."

n "Intentas convencerte de que solo fue un sueño."

n "Entonces..."

scene bg habitacion_sombra with dissolve

n "Algo llama tu atención."

n "Sobre la pared de adobe aparece una sombra."

n "Tiene exactamente la misma forma que las páginas arrancadas del libro."

n "Permanece inmóvil."

n "Como si te estuviera observando."

play sound "audio/latido.ogg"

n "Parpadeas."

scene bg habitacion_noche with dissolve

n "La sombra desaparece. No queda absolutamente nada."

n "No sabes cuánto tiempo permaneces sentado.Pero decides no contarle a nadie lo que acabas de ver."

n "Hay cosas que todavía no puedes explicar."


scene bg casa_puerta
with dissolve

play sound "audio/puerta.ogg"

n "Un ruido en la puerta interrumpe la conversación."

n "Dos personas entran cargando atados de tela. Sus manos aún conservan restos de tierra y hojas secas."

n  "Al ver a T/n, ninguno parece sorprenderse."

show mamaqori normal at centroizquierda
show taytapillco normal at centroderecha
with dissolve

mamaqori "Vaya... así que tenemos visita."

mamaqori "Acércate al fogón. Afuera ya empieza a hacer frío."

scene bg fogon
with fade

show yana normal at left
show taytapillco normal at right

"Todos toman asiento alrededor del fuego."

"Antes de decir una sola palabra, Tayta Pillco toma un pequeño cántaro de chicha."

"Derrama unas gotas sobre la tierra y murmura unas palabras en quechua."

tn "¿Qué fue eso?"

tayta "Un gesto de agradecimiento."

tayta "Antes de compartir nuestros alimentos, compartimos primero con la Pachamama."

tayta "Ella nos sostiene durante todo el año."

tn "¿La Pachamama es como... una diosa?"

mamaqori "Es la Tierra misma."

mamaqori "No vive en un templo."

mamaqori "Está en las montañas, en los ríos, en cada cultivo."

mamaqori "Para nosotros, no está separada de la vida."

mamaqori "Ella es la vida."

n "El sonido de la leña crepitando llena la habitación."

y "Muchas personas creen que nuestra historia comenzó con los incas."

y "Pero el pueblo quechua existía mucho antes."

y "Nuestra lengua, el runasimi, ya era hablada por otros pueblos antiguos."

y "Los incas la adoptaron y la llevaron por gran parte de los Andes."

y "El imperio desapareció..."

y "Pero nosotros seguimos aquí."

tn "Entonces... ser quechua no significa solamente haber pertenecido al Imperio Inca."

tayta "Exactamente."

tayta "Lo que realmente nos mantiene unidos es el ayllu."

tn "¿Qué es un ayllu?"

mamaqori "Una comunidad."

mamaqori "Un lugar donde las familias trabajan juntas."

mamaqori "Aquí nadie cultiva completamente solo."

mamaqori "Hoy ayudamos a nuestros vecinos."

mamaqori "Mañana ellos nos ayudan a nosotros."

tayta "A eso lo llamamos ayni."

tayta "Y cuando todo el pueblo trabaja unido para una tarea grande..."

tayta "Eso es una minka."

tn "Nunca había escuchado algo así."

y "Mañana puedo enseñarte."

y "Es muy distinto verlo con tus propios ojos."

tn "Me gustaría."

show yana feliz at center
y "Entonces mañana saldremos temprano."

scene bg habitacion_simple
with fade

"Esa noche, antes de dormir, Yana entra con un pequeño gorro tejido entre las manos."

show yana normal
with dissolve

y "Toma."

y "Las noches aquí son muy frías."

y "Es un chullo."

tn "Gracias."

y "Mira bien los colores."

y "Cada comunidad tiene patrones distintos."

y "Si sabes leerlos, puedes descubrir de dónde viene una persona."

tn "¿Lo hiciste tú?"

y "Mi mamá me enseñó."

y "Ella aprendió de mi abuela."

y "Y ella de la suya."

y "Aquí muchas cosas se enseñan observando."

"T/n pasa lentamente los dedos por los tejidos."

"Por un instante..."

"Los dibujos le recuerdan exactamente a los símbolos que vio dentro del misterioso libro de la biblioteca."

stop music fadeout 2.0

scene black
with Fade(1.0, 2.0, 1.0)
    
"Esa noche, el sueño volvió."

############################################################
# EL SUEÑO
############################################################

scene bg sueno_valle
with Fade(1.0, 2.0, 1.0)

play music "audio/misterio.ogg" fadein 2.0

"Esa noche, agotadx, T/n se queda dormidx casi de inmediato."

"Pero el descanso nunca llega."

"Sueña con un valle inmenso cubierto por una espesa niebla."

"Las montañas parecen interminables."

"El silencio resulta tan profundo que incluso respirar se siente extraño."

scene bg cueva
with dissolve

"Desde el interior de una enorme cueva comienzan a salir dos figuras."

"Un hombre."

"Y una mujer."

"Sus vestimentas doradas brillan con una luz que no pertenece a este mundo."

"No dicen una sola palabra."

"Simplemente avanzan lentamente hacia T/n."

scene bg conquista
with dissolve

"Sin previo aviso..."

"El paisaje cambia."

"Ahora se encuentra frente a un hombre arrodillado."

"Soldados con armaduras de metal lo rodean."

"Levantan sus armas."

"Todo ocurre en absoluto silencio."

"Un instante después..."

play sound "audio/golpe.ogg"

"El hombre cae."

"La tierra comienza a temblar."

scene bg tierra
with hpunch

"Aunque su cuerpo desaparece bajo el suelo..."

"T/n siente algo imposible de explicar."

"Sabe que sigue vivo."

"Que continúa creciendo bajo la tierra."

"Esperando."

voice "audio/voz.ogg"

v "Inkarrí no ha muerto..."

v "Solo espera a que alguien termine de contar su historia."

stop sound

scene bg habitacion_simple_noche
with Fade(1.0, 1.5, 1.0)

play sound "audio/respiro.ogg"

"T/n despierta sobresaltadx."

"Respira con dificultad."

"Tiene el cuerpo cubierto de sudor."

"La habitación permanece completamente oscura."

"Todo parece tranquilo."

"...Hasta que algo llama su atención."

scene bg pared
with dissolve

"Sobre una de las paredes aparece una sombra."

"Tiene exactamente la misma forma que las páginas arrancadas del libro."

"No parece una persona."

"No parece un objeto."

"Simplemente está ahí."

"Observándolo."

"T/n parpadea."

scene bg pared_vacia
with dissolve

"La sombra desaparece."

"Como si jamás hubiera existido."

stop music fadeout 2.0

scene black
with dissolve

"A la mañana siguiente..."

scene bg exterior_casa
with fade

play music "audio/pueblo.ogg" fadein 2.0

show yana normal
with dissolve

"y ya lo esperaba afuera."

"Llevaba un pequeño atado de tela sobre el hombro."

y "Buenos días."

y "Dormiste bastante."

tn "Tuve un sueño muy extraño..."

"T/n duda por un momento."

"Pero decide guardar silencio."

tn "Nada... olvídalo."

y "¿Listx?"

y "Hoy conocerás el pueblo de verdad."

y "No el que ven los turistas."

scene bg calle_pueblo_noche
with dissolve

"Ambos comienzan a caminar."

"Pasan junto a mujeres tejiendo frente a sus casas."

"Niños jugando en las calles."

"Ancianos conversando en quechua."

"yana saluda a casi todas las personas que encuentra."

scene bg bifurcacion
with fade

"Después de varios minutos llegan a una bifurcación."

"Un sendero asciende hacia las montañas."

"El otro continúa entre los pastizales."

show yana normal

y "¿Por dónde quieres comenzar?"

y "Por arriba está la chacra de mi familia."

y "Por el otro camino hay una laguna que me gustaría enseñarte."

menu:
    "Ir primero a la chacra":
        $ profundidad = "basica"
        jump chacra_primero

    "Ir primero a la laguna":
        $ profundidad = "profunda"
        jump laguna_primer

############################################################
# RUTA 1 - CHACRA PRIMERO
############################################################

label chacra_primero:

scene bg chacra
with fade

show yana feliz at center

y "Entonces iremos a la chacra."

"Comienzan a subir por un sendero de tierra."

"Con cada paso, el pueblo va quedando más abajo."

"Frente a T/n aparecen enormes andenes que cubren las montañas como si fueran escaleras gigantes."

scene bg chacra_familia
with dissolve

show taytapillco normal at right
show mamaqori normal at left

"En uno de ellos trabajan Tayta Pillco, Mama Qori y varias personas más."

tayta "Llegaron."

mamaqori "Buenos días."

tn "Buenos días."

"T/n observa cómo todos trabajan juntos."

"Nadie parece recibir órdenes."

"Cada persona sabe exactamente qué hacer."

tn "Pensé que solo trabajaría su familia."

y "Ellos no son familia."

y "Son vecinos."

y "Hoy ellos nos ayudan."

y "Otro día nosotros iremos a ayudarlos."

y "Eso es el ayni."

tn "Entonces todos colaboran entre sí..."

tayta "Así ha sido durante generaciones."

tayta "Cuando alguien necesita ayuda, nunca trabaja solo."

scene bg andenes
with dissolve

tayta "Mira la montaña."

tayta "¿Notas que está dividida en niveles?"

tn "Sí."

tayta "Cada uno tiene una temperatura distinta."

tayta "Gracias a eso podemos sembrar diferentes cultivos."

tayta "Abajo crece el maíz."

tayta "Más arriba la papa."

tayta "Y todavía más arriba la quinua."

tn "Nunca imaginé que una montaña pudiera aprovecharse de esa manera."

tayta "Nuestros abuelos lo descubrieron hace siglos."

scene bg chakitaqlla
with dissolve

n "yana toma una herramienta de madera."

y "Esto se llama chakitaqlla."

y "Con ella removemos la tierra."

y "Pruébala."

n "T/n intenta utilizarla."

play sound "audio/tierra.ogg"

n "La primera vez pierde el equilibrio."

n "La segunda tampoco sale muy bien."

n "Después de varios intentos consigue abrir un pequeño surco."

tayta "Nada mal."

tayta "Todos empezamos igual."

scene bg papas
with dissolve

n "Más adelante, Mama Qori muestra diferentes variedades de papa."

mamaqori "Muchas personas creen que solo existe un tipo."

mamaqori "Pero nosotros cultivamos cientos."

tn "Jamás había visto tantos colores."

mamaqori "Cada una sirve para algo distinto."

mamaqori "Y cuando queremos conservarlas durante mucho tiempo..."

mamaqori "Las convertimos en chuño."

tn "¿Cómo?"

mamaqori "Las dejamos varias noches bajo el intenso frío."

mamaqori "Luego el sol termina de secarlas."

mamaqori "Así pueden durar años."

tn "Increíble..."

"T/n observa nuevamente las montañas."

"Empieza a comprender que todo cuanto lo rodea existe gracias al conocimiento transmitido durante generaciones."

scene bg sendero_laguna
with fade

y "Todavía falta un lugar."

y "Ven."

jump laguna_despues_chacra

############################################################
# LAGUNA (después de la chacra)
############################################################

label laguna_despues_chacra:

scene bg sendero_laguna
with fade

"Se alejan poco a poco de los cultivos."

"El sendero atraviesa extensos pastizales movidos por el viento."

"Solo se escucha el sonido de los pasos y el canto lejano de algunas aves."

y "Este lugar siempre ha sido uno de mis favoritos."

y "Cuando era niña venía con mi abuelo."

y "Él decía que aquí la tierra todavía guarda muchos recuerdos."

scene bg laguna
with dissolve

"Tras varios minutos de caminata, llegan a una pequeña laguna."

"El agua permanece completamente quieta."

"Las montañas se reflejan en ella como si fueran un espejo."

tn "Es... hermosa. Es simplemente magnífico"

show yana feliz at center
y "Aún no has visto lo más interesante."

scene bg waruwaru
with dissolve

n "Yana señala varios rectángulos de tierra separados por pequeños canales de agua."

tn "¿Qué son?"

y "Se llaman waru waru."

y "También los conocen como camellones."

tn "Nunca había visto algo parecido."

y "Son una técnica agrícola muy antigua."

y "Durante el día el agua almacena calor."

y "Y por la noche lo libera lentamente."

y "Así protege los cultivos de las heladas."

tn "Entonces... utilizan el agua para controlar la temperatura."

y "Exacto."

y "Nuestros antepasados aprendieron a trabajar con la naturaleza."

y "No contra ella."

tn "¿Todavía se siguen usando?"

y "Algunos sí."

y "Muchos dejaron de construirse hace años."

y "Pero varias comunidades están intentando recuperarlos."


n "T/n se acerca lentamente a la orilla."

n "Observa su reflejo sobre el agua inmóvil."

n "Por un instante recuerda las ilustraciones del misterioso libro."

tn "Yana..."

tn "¿Crees que un lugar pueda recordar lo que ocurrió aquí hace siglos?"

n "Yana permanece unos segundos en silencio."

y "Aquí solemos decir que el agua nunca olvida."

y "Solo espera a que alguien vuelva a preguntarle."

n "El viento sopla suavemente."

n "Las palabras de Yana permanecen dando vueltas en la mente de T/n."

n "Las páginas arrancadas."

n "La biblioteca."

n "El sueño."

n "Todo comienza a sentirse conectado."

play sound "audio/viento.ogg"

n "Por un instante... Una pequeña onda aparece en el centro de la laguna."

n "No hay peces."

n "No cae ninguna piedra."

n "El agua simplemente se mueve."

tn "(¿Lo imaginé...?)"

scene bg sendero_regreso
with fade

y "Será mejor volver."

y "Hoy hay feria en la plaza."

y "Quiero presentarte a alguien."

n "Ambos emprenden el camino de regreso al pueblo."

jump plaza

############################################################
# LA PLAZA
############################################################

label plaza:

scene bg plaza_feria
with fade

play music "audio/feria.ogg" fadein 2.0

n "Al caer la tarde, Yana conduce a T/n de regreso al centro del pueblo."

n "La plaza se encuentra completamente transformada."

n "Puestos de artesanía, tejidos de todos los colores, cerámica, instrumentos musicales y alimentos tradicionales llenan cada rincón."

n "El ambiente está lleno de conversaciones, risas y música."

y "Cuando hay una celebración importante, la plaza siempre se llena así."

y "Aquí no solo vendemos cosas."

y "También compartimos historias."

scene bg telar
with dissolve

show mamaqori normal
with dissolve

"A un lado de la plaza, Mama Qori trabaja frente a un telar de cintura."

"Sus manos se mueven con una precisión impresionante."

"Los hilos parecen acomodarse solos."

tn "Esos dibujos..."

tn "Se parecen mucho a los que vi en aquel libro."

show mamaqori feliz at center
mamaqori "Los tejidos también cuentan historias."

mamaqori "Cada figura representa algo."

mamaqori "Una montaña."

mamaqori "Un río."

mamaqori "Una familia."

mamaqori "Un recuerdo."

tn "¿Quién te enseñó?"

mamaqori "Mi madre."

mamaqori "Y ella aprendió de mi abuela."

mamaqori "Así es como el conocimiento sigue vivo."

scene bg mama_sisa
with dissolve

n "No muy lejos de allí, un pequeño grupo de personas rodea a una anciana."

n "Niños, jóvenes y adultos la escuchan con atención."

y "Ella es Mama Sisa."

y "Nadie conoce más historias que ella."

scene bg telar

show mamasisa normal
with dissolve

mamasisa "Acérquense."

mamasisa "Las historias nunca deben contarse desde lejos."

n "T/n y Yana se sientan junto al resto."

mamasisa "Hace muchos años..."

mamasisa "Un gran gobernante fue derrotado."

mamasisa "Los invasores separaron su cabeza de su cuerpo."

mamasisa "Pero cuentan que su cuerpo sigue creciendo bajo la tierra."

mamasisa "Esperando el momento de reunirse nuevamente."

n "El corazón de T/n se acelera."

n "Es exactamente el mismo hombre que vio en su sueño."

tn "(Inkarrí...)"

mamasisa "Mientras exista alguien que recuerde su historia..."

mamasisa "Jamás desaparecerá."

n "Mama Sisa hace una breve pausa."

mamasisa "Y ahora otra historia."

mamasisa "Hace muchísimo tiempo..."

mamasisa "Dos hermanos salieron de las aguas de un lago."

mamasisa "Ellos guiaron a su pueblo hasta encontrar el lugar donde construirían un nuevo hogar."

"T/n permanece completamente inmóvil."

"No sabe por qué, pero siente que esas historias le resultan familiares."

"Como si ya las hubiera escuchado antes."

scene bg telar
with dissolve

show mamaqori normal
with dissolve

"Cuando la narración termina, Mama Qori vuelve a llamar a T/n."

mamaqori "Ven un momento."

"El telar aún no está terminado."

"Entre los hilos existe un pequeño espacio vacío."

mamaqori "Necesito que me ayudes."

tn "¿Yo?"

mamaqori "Solo debes pasar este hilo."

mamaqori "Pero antes..."

mamaqori "Quiero hacerte una pregunta."

stop music fadeout 2.0

menu:
    "¿Que intención llevas contigo?"
    "Quiero entender." :
        $ intencion = "entender"
        jump final_entender

    "Quiero ser parte de esto." :
        $ intencion = "quedarme"
        jump final_quedarse

    "Quiero volver y contarlo." :
        $ intencion = "contarlo"
        jump final_contarlo
              
############################################################
# FINAL 1 - EL HILO QUE ENTIENDE
############################################################

label final_entender:

    scene bg telar_cerca
    with fade

    play music "audio/final_mistico.ogg" fadein 2.0

    n "T/n toma el hilo entre sus dedos."

    n "Piensa en el libro."

    n "En las páginas arrancadas."

    n "En la advertencia escrita con aquella extraña letra."

    n "Piensa también en todo lo que ha visto desde que llegó."

    tn "Quiero entender."

    tn "No quiero que todo esto desaparezca."

    n "Con cuidado pasa el hilo por el espacio vacío del telar."

    play sound "audio/brillo.ogg"

    scene white
    with Dissolve(1.0)

    "En ese mismo instante..."

    stop music fadeout 1.0

    scene bg vision_telar
    with Fade(1.0,1.0,1.0)

    play music "audio/misterio.ogg" fadein 2.0

    "Todo el ruido de la plaza desaparece."

    "Ya no escucha personas."

    "Ni viento."

    "Ni música."

    "Solo existe el telar frente a él."

    "Los hilos comienzan a moverse lentamente."

    "Como si alguien invisible los estuviera tejiendo."

    "Uno tras otro aparecen cientos de manos."

    "Manos jóvenes."

    "Manos ancianas."

    "Manos que pertenecieron a personas de distintas épocas."

    "Todas continúan el mismo tejido."

    "Generación tras generación."

    "El telar parece no tener principio ni final."

    "Entonces algunos hilos empiezan a romperse."

    play sound "audio/hilo.ogg"

    "Uno."

    "Luego otro."

    "Y otro más."

    "Cada hilo que desaparece borra un color del tejido."

    "Una v resuena alrededor."

    v "Cada historia olvidada..."

    v "Es un hilo menos."

    v "Cada lengua que deja de hablarse..."

    v "Es un hilo menos."

    v "Cada tradición abandonada..."

    v "Es un hilo menos."

    n "El enorme tejido comienza a perder su forma."

    n "Cada vez quedan más espacios vacíos."

    tn "(No...)"

    tn "(No puede terminar así...)"

    v "Por eso fuiste llamado."

    v "No para cambiar el pasado."

    v "Sino para impedir que el olvido siga creciendo."

    scene bg vision_hilos
    with dissolve

    "Frente a T/n aparecen cuatro enormes hilos de distintos colores."

    "Cada uno se dirige hacia un horizonte diferente."

    "Cada uno representa un pueblo distinto."

    "Quechua."

    "Aymara."

    "Uro."

    "Jaqaru."

    v "Aún quedan historias por escuchar."

    v "Aún quedan caminos por recorrer."

    scene white
    with Dissolve(1.5)

    stop music fadeout 2.0

    scene bg plaza_feria
    with Fade(1.5,1.0,1.5)

    play music "audio/feria.ogg" fadein 2.0

    "El ruido de la plaza vuelve de golpe."

    "Como si nada hubiera ocurrido."

    show mamasisa normal
    with dissolve

    "Mama Sisa lo observa con una pequeña sonrisa."

    mamasisa "Ahora sí..."

    mamasisa "Has comenzado a escuchar."

    scene bg noche_casa
    with fade

    show yana normal
    with dissolve

    "Más tarde, ya de noche, T/n permanece sentado mirando el cielo."

    "Yana se acerca en silencio."

    y "Viste algo en la plaza..."

    y "¿Verdad?"

    tn "Sí."

    tn "No sé cómo explicarlo."

    tn "Sentí que todas esas historias siguen vivas."
    
    show yana feliz at center
    y "Porque nunca desaparecieron."

    y "Solo esperaban a alguien dispuesto a escucharlas."

    tn "¿Cómo sabías que ocurriría?"

    y "Porque hace muchos años..."

    y "Mi abuela también pasó un hilo por ese mismo telar."

    y "Y desde entonces jamás dejó de contar historias."

    tn "Entonces..."

    tn "¿Todo esto era real?"

    show yana feliz at center
    y "Tal vez."

    y "O tal vez algunas cosas solo pueden entenderse viviéndolas."

    "T/n levanta nuevamente la mirada."

    "Las estrellas parecen más brillantes que nunca."

    "Y por primera vez desde que encontró aquel libro..."

    "Ya no siente miedo."

    scene black
    with fade

    centered "{size=+15}FINAL 1{/size}"

    centered "{size=+20}El hilo que entiende{/size}"

    return

############################################################
# FINAL 2 - EL HILO QUE SE QUEDA
############################################################

label final_quedarse:

    scene bg telar_cerca
    with fade

    play music "audio/final_emotivo.ogg" fadein 2.0

    "T/n toma el hilo con cuidado."

    "Piensa en todo lo que ha vivido desde que llegó."

    "Cuando llegó no tenía dinero."

    "No tenía celular."

    "Ni siquiera sabía dónde dormir."

    "Sin embargo..."

    "Una familia que nunca había visto antes le abrió las puertas de su casa."

    "Le compartieron comida."

    "Le enseñaron su historia."

    "Lo hicieron sentir parte de su comunidad."

    tn "Quiero ser parte de esto."

    tn "No quiero ser solo alguien que pasó por aquí."

    play sound "audio/brillo.ogg"

    "Con delicadeza pasa el hilo por el espacio vacío del telar."

    scene white
    with Dissolve(1.0)

    stop music fadeout 1.0

    scene bg vision_telar
    with Fade(1.0,1.0,1.0)

    play music "audio/final_emotivo.ogg" fadein 2.0

    "Todo desaparece."

    "La plaza."

    "La feria."

    "Las voces."

    "Solo permanece el tejido."

    "Miles de hilos comienzan a moverse lentamente."

    "Entre todos ellos aparece uno nuevo."

    "Un hilo distinto."

    "Más claro."

    "Más brillante."

    "Avanza lentamente."

    "No rompe ninguno de los otros."

    "No ocupa el lugar de nadie."

    "Simplemente..."

    "Encuentra el suyo."

    v "Nadie pertenece a un lugar por haber nacido en él."

    v "Se pertenece cuando aprende a cuidar aquello que otros le confiaron."

    "El nuevo hilo termina de entrelazarse."

    "Ahora forma parte del tejido."

    "Como si siempre hubiera estado ahí."

    scene white
    with Dissolve(1.5)

    stop music fadeout 2.0

    scene bg plaza_feria
    with Fade(1.5,1.0,1.5)

    play music "audio/feria.ogg" fadein 2.0

    show mamaqori normal

    mamaqori "Ya está."

    mamaqori "Ahora ese hilo siempre será parte del tejido."

    mamaqori "Aunque después lleguen cientos más."

    show mamasisa normal at right

    mamasisa "Algunas personas llegan buscando respuestas."

    mamasisa "Otras llegan buscando un lugar."

    mamasisa "Tú encontraste ambas cosas."

    scene bg noche_casa
    with fade

    show yana normal at center

    y "Te vi sonreír."

    tn "Sentí..."

    tn "Como si perteneciera aquí."
    show yana feliz at center
    y "Porque comenzaste a mirar este lugar como nosotros."

    tn "No quiero irme todavía."

    y "Nadie te está echando."

    y "Siempre hace falta alguien dispuesto a aprender."

    y "La chacra."

    y "Los telares."

    y "Las historias."

    y "Siempre necesitan una v más."

    tn "Pero aún me falta muchísimo por aprender."
 
    show yana feliz at center
    y "Todos empezamos así."

    y "Nadie nace sabiendo."

    y "Lo importante es querer escuchar."

    "Ambos levantan la vista."

    scene bg estrellas
    with dissolve

    "El cielo de los Andes se encuentra completamente despejado."

    "Miles de estrellas iluminan la montaña."

    "Por primera vez desde que salió de aquella biblioteca..."

    "T/n siente que dejó de estar perdido."

    scene black
    with fade

    centered "{size=+15}FINAL 2{/size}"

    centered "{size=+20}El hilo que se queda{/size}"

    jump epilogo_general

    ############################################################
# FINAL 3 - EL HILO QUE VUELVE A CASA
############################################################

label final_contarlo:

    scene bg telar_cerca
    with fade

    play music "audio/final_esperanza.ogg" fadein 2.0

    "T/n sostiene el hilo entre sus manos."

    "Piensa en el libro."

    "En las páginas arrancadas."

    "En todo lo que ha aprendido desde que llegó."

    "Comprende que muchas personas nunca tendrán la oportunidad de conocer estas historias."

    tn "Quiero volver."

    tn "Quiero contar lo que aprendí aquí."

    tn "No quiero que estas historias se pierdan."

    play sound "audio/brillo.ogg"

    "Con cuidado pasa el hilo por el espacio vacío del telar."

    scene white
    with Dissolve(1.0)

    stop music fadeout 1.0

    scene bg vision_telar
    with Fade(1.0,1.0,1.0)

    play music "audio/misterio.ogg" fadein 2.0

    "El mundo desaparece."

    "Solo permanece el inmenso telar."

    "Miles de hilos atraviesan el horizonte."

    "Pero esta vez..."

    "Los patrones no terminan en la tela."

    "Continúan más allá."

    "Cruzan montañas."

    "Atraviesan ríos."

    "Llegan hasta ciudades lejanas."

    v "No todos los hilos permanecen en el mismo lugar."

    v "Algunos nacieron para viajar."

    v "Para unir aquello que el tiempo intentó separar."

    "Uno de los hilos comienza a extenderse."

    "Avanza hacia un horizonte desconocido."

    "Mientras más lejos llega..."

    "Más brillante se vuelve el tejido."

    v "Cada historia compartida..."

    v "Es un hilo que nunca volverá a romperse."

    scene bg cuatro_senderos
    with dissolve

    "Frente a T/n aparecen nuevamente los cuatro senderos."

    "Cada uno conduce hacia un pueblo distinto."

    "Quechua."

    "Aymara."

    "Uro."

    "Jaqaru."

    v "Aún quedan muchas historias esperando ser escuchadas."

    v "Tu viaje apenas comienza."

    scene white
    with Dissolve(2.0)

    stop music fadeout 2.0

    scene bg plaza_feria
    with Fade(1.5,1.0,1.5)

    play music "audio/feria.ogg" fadein 2.0

    show mamasisa normal
    with dissolve

    mamasisa "Hay quienes permanecen cuidando las historias."

    mamasisa "Y hay quienes las llevan a lugares donde nadie las conoce."

    mamasisa "Ambas tareas son igual de importantes."

    show mamaqori normal at left
    with dissolve

    "Mama Qori corta un pequeño trozo del hilo que acaba de colocar."

    mamaqori "Quiero que lo conserves."

    mamaqori "No como un recuerdo."

    mamaqori "Sino como una promesa."

    "Entrega el pequeño hilo a T/n."

    tn "Lo guardaré."

    scene bg noche_casa
    with fade

    show yana normal
    with dissolve

    y "¿Sabes qué harás cuando regreses?"

    tn "Sí."

    tn "Voy a contar todo lo que viví."

    tn "Quiero que más personas conozcan esta cultura."
    show yana feliz at center
    y "Eso también es una forma de quedarse."

    tn "¿Crees que alguien me crea?"

    y "Tal vez no todos."

    y "Pero bastará con que una sola persona quiera escuchar."

    y "Así empiezan todas las historias."

    "T/n observa el pequeño hilo que sostiene entre sus manos."

    "Por un instante siente que todavía conserva el calor del telar."

    scene bg estrellas
    with dissolve

    "Una estrella fugaz cruza lentamente el cielo."

    "Luego otra."

    "Y otra más."

    "Como si los cuatro caminos siguieran llamándolo desde algún lugar."

    scene black
    with fade

    centered "{size=+15}FINAL 3{/size}"

    centered "{size=+20}El hilo que vuelve a casa{/size}"

    jump epilogo_general