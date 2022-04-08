class Modo():
    def __init__(self, tmax_juego=600,tmax_pregunta=60, num_pregunta=10, num_jugadores=1) -> None:
        self.__tmax_juego = tmax_juego
        self.__tmax_pregunta = tmax_pregunta
        self.__num_pregunta = num_pregunta
        self.__num_jugadores = num_jugadores

    @property
    def tmax_juego(self):
        return self.__tmax_juego

    @property
    def tmax_pregunta(self):
        return self.__tmax_pregunta

    @property
    def num_pregunta(self):
        return self.__num_pregunta

    @property
    def num_jugadores(self):
        return self.__num_jugadores