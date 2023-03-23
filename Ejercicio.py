from dataclasses import dataclass

import self as self


@dataclass
class elemento:
    nombre: str



    def __eq__(self, other):
        if isinstance(self, other):
            return self.nombre == other.nombre
        return False


class conjunto:
    contador= 0

    def __init__(self, nombre):
        self.list_ele= []
        self.nombre= nombre
        conjunto.contador += 1
        self.__id = conjunto.contador


    @property

    def __id(self):
        return self.__id


    def conti_ele (self, elemento):
        for e in self.lista_elementos:
            if e.nombre == elemento.nombre:
                return True
        return False

    def agregar_elemento(self, elemento):
        if not self.__contiene_elemento(elemento):
            self.__elementos.append(elemento)

    def unir(self, otro_conjunto):
        for elemento in otro_conjunto.__elementos:
            if not self.__contiene_elemento(elemento):
                self.__elementos.append(elemento)

    def __add__(self, otro_conjunto):
        self.unir(otro_conjunto)
        return self

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        nombre = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        elementos = [e1 for e1 in conjunto1.__elementos for e2 in conjunto2.__elementos if e1 == e2]
        nuevo_conjunto = cls(nombre)
        for elemento in elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        return nuevo_conjunto

    def __str__(self):
        elementos_str = ", ".join([str(e.nombre) for e in self.__elementos])
        return f"Conjunto {self.nombre}: ({elementos_str})"








