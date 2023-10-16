from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):
    _listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista._listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self._golesMarcados
    
    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados = golesMarcados

    def getTarjetasRojas(self):
        return self._tarjetasRojas
    
    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas

    def getPiernaHabil(self):
        return self._piernaHabil
    
    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil = piernaHabil

    def __str__(self):
        return "Nombre: " + self._nombre + "\nEdad: " + str(self._edad) + "\nAltura: " + str(self._altura) + "\nSexo: " + self._sexo + "\nAños Practicando: " + str(self._añosPracticando) + "\nGoles Marcados: " + str(self._golesMarcados) + "\nTarjetas Rojas: " + str(self._tarjetasRojas) + "\nPierna Habil: " + self._piernaHabil
    
    @staticmethod
    def getListaFutbolistas():
        return Futbolista._listaFutbolistas
    
    @staticmethod
    def setListaFutbolistas(listaFutbolistas):
        Futbolista._listaFutbolistas = listaFutbolistas

    @staticmethod
    def agregarFutbolista(futbolista):
        Futbolista._listaFutbolistas.append(futbolista)

    @staticmethod
    def eliminarFutbolista(futbolista):
        Futbolista._listaFutbolistas.remove(futbolista)