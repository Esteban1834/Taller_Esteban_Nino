# La clase unidad, define el comportamiento de las unidades,(Soldado, Arquero, Caballero)
class Unidad:
    def __init__(self, nombre, ataque, movimiento):
        self.nombre = nombre
        self.ataque = ataque
        self.movimiento = movimiento

    def ejecutar_ataque(self):
        pass

    def ejecutar_movimiento(self):
        pass


# Describe el comportamiento de ataque para los Soldados
class AtaqueSoldado:
    def ejecutar_ataque(self):
        print("Soldado ataca con espada.")


# Comportamiento de movimiento para los Soldados
class MovimientoSoldado:
    def ejecutar_movimiento(self):
        print("Soldado camina.")


# Comportamiento de ataque para los Arqueros
class AtaqueArquero:
    def ejecutar_ataque(self):
        print("Arquero dispara flechas.")


# Comportamiento de movimiento para los Arqueros
class MovimientoArquero:
    def ejecutar_movimiento(self):
        print("Arquero corre.")


# Comportamiento de ataque para los Caballeros
class AtaqueCaballero:
    def ejecutar_ataque(self):
        print("Caballero ataca con espada y lanza.")


# Comportamiento de movimiento para los Caballeros
class MovimientoCaballero:
    def ejecutar_movimiento(self):
        print("Caballero monta a caballo y galopa.")


# Clase Soldado que hereda de Unidad
class Soldado(Unidad):
    def __init__(self):
        super().__init__("Soldado", AtaqueSoldado(), MovimientoSoldado())


# Clase Arquero que hereda de Unidad
class Arquero(Unidad):
    def __init__(self):
        super().__init__("Arquero", AtaqueArquero(), MovimientoArquero())


# Clase Caballero que hereda de Unidad
class Caballero(Unidad):
    def __init__(self):
        super().__init__("Caballero", AtaqueCaballero(), MovimientoCaballero())


# Ejemplo de uso
soldado = Soldado()
arquero = Arquero()
caballero = Caballero()

# Soldado realiza ataque y movimiento
soldado.ataque.ejecutar_ataque()
soldado.movimiento.ejecutar_movimiento()

# Arquero realiza ataque y movimiento
arquero.ataque.ejecutar_ataque()
arquero.movimiento.ejecutar_movimiento()

# Caballero realiza ataque y movimiento
caballero.ataque.ejecutar_ataque()
caballero.movimiento.ejecutar_movimiento()

#Como podemos ver, las clases heredan de la clase Unidad, que define el comportamiento de las unidades en la batalla.
#Los usuarios podran seleccionar los tipos de unidades (Soldado, Arquero, Caballero), basandose en sus habilidades de moviemiento y habilidades de ataque.