from partida import Partida
from jugador import Jugador
from pregunta import Pregunta
from modo import Modo
from respuesta import Respuesta

def main():
    pass

p1 = Pregunta(1,'¿Es verano?')
r1 = Respuesta(1,'Si',False)
r2 = Respuesta(2,'No',True)

p1.respuestas = [r1,r2]
col_preguntas = [p1]

j = Jugador('Rafa')
m = Modo()

mi_partida = Partida(j,m,col_preguntas)

mi_partida.iniciar()

preguntas = mi_partida.preguntas
for preg in preguntas:
    print(preg.cuerpo)
    for resp in preg.respuestas:
        print(resp.cuerpo)