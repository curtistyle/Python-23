import cmath


class Par:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __repr__(self):
        return f"({self.x},{self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Conjunto:
    def __init__(self, name, elementos = list()):
        self.name = name
        self.elementos = elementos

    def __str__(self):
        elementos_str = ', '.join(str(e) for e in self.elementos)
        return elementos_str

class Operaciones:
    @staticmethod
    def Universal(*args):
        conjunto_universal = Conjunto(name="U")
        if len(args) == 1:
            for x in args[0]:
                for y in args[0]:
                    conjunto_universal.elementos.append(Par(x,y))
        return conjunto_universal

    @staticmethod
    def matriz_binaria(relacion : Conjunto, universal : Conjunto):
        temp = relacion.elementos.copy()
        nueva_matriz = [[0] * int(cmath.sqrt(len(universal.elementos)).real) ] * int(cmath.sqrt(len(universal.elementos)).real)
        c=0
        for fila in range(len(nueva_matriz)):
            for columna in range(len(nueva_matriz[0])):
                print(f"{fila=},{columna=}, {c=}",universal.elementos[fila+columna],relacion.elementos, universal.elementos[c] in temp)

                if (universal.elementos[c] in temp):
                    nueva_matriz[columna][fila] = 1
                else:
                    nueva_matriz[columna][fila] = 0
                c+=1

        return nueva_matriz









if __name__=="__main__":

    R = Conjunto("R", [Par(1,1),Par(2,2), Par(3,3)])

    u = Operaciones.Universal([1, 2, 3])


    print(cmath.sqrt(len(u.elementos)).real)

    print(u)
    input()

    print(Operaciones.matriz_binaria(R, u))





